from pathlib import Path
import json
import re
from typing import Any
from urllib.parse import parse_qs, urlparse

import yt_dlp
from faster_whisper import WhisperModel
from tickers import TICKER_ALIASES, TICKER_TAGS


DEFAULT_OUTPUT_DIR = Path("outputs")
LOCAL_CONFIG_PATH = Path("config.local.json")

def sanitize_filename(name: str) -> str:
    """Make a safe filename from a video title."""
    safe_name = re.sub(r'[\\/*?:"<>|]', "", name).strip()
    return safe_name or "youtube_note"


def format_upload_date(raw_date: str | None) -> str:
    """Convert yyyymmdd to yyyy-mm-dd."""
    if not raw_date or len(raw_date) != 8 or not raw_date.isdigit():
        return "Unknown"
    return f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"


def get_output_dir() -> Path:
    """
    Read output_dir from config.local.json if available.
    Falls back to outputs/ when config is missing or invalid.
    """
    if not LOCAL_CONFIG_PATH.exists():
        return DEFAULT_OUTPUT_DIR

    try:
        config_data = json.loads(LOCAL_CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Warning: config.local.json is not valid JSON. Using outputs/.")
        return DEFAULT_OUTPUT_DIR

    if not isinstance(config_data, dict):
        print("Warning: config.local.json must be a JSON object. Using outputs/.")
        return DEFAULT_OUTPUT_DIR

    output_dir_value = config_data.get("output_dir")
    if not isinstance(output_dir_value, str) or not output_dir_value.strip():
        return DEFAULT_OUTPUT_DIR

    return Path(output_dir_value.strip())


def download_audio(youtube_url: str, output_dir: Path) -> dict[str, Any]:
    """
    Download YouTube audio and convert it to mp3.
    Returns a small metadata dict for later markdown output.
    """
    ydl_opts = {
        "format": "bestaudio/best",
        "noplaylist": True,
        "outtmpl": str(output_dir / "%(id)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        title = info.get("title") or "YouTube Video"
        video_id = info.get("id") or "audio"
        channel = info.get("channel") or info.get("uploader") or "Unknown"
        upload_date = format_upload_date(info.get("upload_date"))

    audio_path = output_dir / f"{video_id}.mp3"
    return {
        "title": title,
        "audio_path": audio_path,
        "channel": channel,
        "published_date": upload_date,
    }


def format_timestamp(seconds: int) -> str:
    """Convert seconds to a compact mm:ss timestamp."""
    safe_seconds = max(0, int(seconds))
    minutes = safe_seconds // 60
    remaining_seconds = safe_seconds % 60
    return f"{minutes:02d}:{remaining_seconds:02d}"


def transcribe_chinese_audio(audio_path: Path) -> list[tuple[int, str]]:
    """Transcribe audio with faster-whisper and keep segment start times."""
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(audio_path), language="zh", task="transcribe")

    transcript_entries = []
    for segment in segments:
        text = segment.text.strip()
        if text:
            start_seconds = max(0, int(segment.start))
            transcript_entries.append((start_seconds, text))

    return transcript_entries


def contains_cjk(text: str) -> bool:
    """Return True if text contains Chinese characters."""
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def is_ticker_symbol(alias: str) -> bool:
    """Simple check: symbol-like aliases (e.g. NVDA, BRK.B, BRK-B)."""
    return bool(re.fullmatch(r"[A-Z][A-Z0-9.\-]{0,9}", alias))


def detect_tickers_with_matches(transcript: str) -> tuple[list[str], dict[str, list[str]]]:
    """
    Detect canonical tickers using alias rules in tickers.py.
    - Chinese aliases: substring match
    - English names: case-insensitive substring match
    - Ticker symbols: strict boundary-style match
    """
    transcript_upper = transcript.upper()
    transcript_lower = transcript.lower()
    detected = set()
    matched_aliases: dict[str, set[str]] = {}

    for canonical_ticker, aliases in TICKER_ALIASES.items():
        for alias in aliases:
            alias = alias.strip()
            if not alias:
                continue

            # Chinese alias: simple substring matching.
            if contains_cjk(alias):
                if alias in transcript:
                    detected.add(canonical_ticker)
                    matched_aliases.setdefault(canonical_ticker, set()).add(alias)
                    break
                continue

            # Ticker symbol alias: strict matching to avoid false positives.
            alias_upper = alias.upper()
            if is_ticker_symbol(alias_upper):
                pattern = rf"(?<![A-Z0-9]){re.escape(alias_upper)}(?![A-Z0-9])"
                if re.search(pattern, transcript_upper):
                    detected.add(canonical_ticker)
                    matched_aliases.setdefault(canonical_ticker, set()).add(alias)
                    break
                continue

            # English name alias: case-insensitive substring matching.
            if alias.lower() in transcript_lower:
                detected.add(canonical_ticker)
                matched_aliases.setdefault(canonical_ticker, set()).add(alias)
                break

    sorted_tickers = sorted(detected)
    readable_matches = {
        ticker: sorted(matched_aliases.get(ticker, set()), key=str.lower)
        for ticker in sorted_tickers
    }
    return sorted_tickers, readable_matches


def detect_tickers(transcript: str) -> list[str]:
    """Detect canonical tickers only (without debug details)."""
    tickers, _ = detect_tickers_with_matches(transcript)
    return tickers


def generate_ticker_tags(tickers: list[str]) -> list[str]:
    """Collect unique tags from detected tickers and sort them."""
    tags = set()
    for ticker in tickers:
        for tag in TICKER_TAGS.get(ticker, []):
            tags.add(tag)
    return sorted(tags)


def extract_video_id(youtube_url: str) -> str | None:
    """Extract video id from common YouTube URL formats."""
    parsed = urlparse(youtube_url)
    host = parsed.netloc.lower()
    path = parsed.path.strip("/")

    if "youtu.be" in host:
        return path.split("/")[0] if path else None

    if "youtube.com" in host:
        query_video_ids = parse_qs(parsed.query).get("v", [])
        if query_video_ids:
            return query_video_ids[0]

        path_parts = [part for part in path.split("/") if part]
        if len(path_parts) >= 2 and path_parts[0] in {"shorts", "live", "embed"}:
            return path_parts[1]

    return None


def build_timestamp_link(youtube_url: str, seconds: int) -> str:
    """Build a stable YouTube timestamp URL."""
    video_id = extract_video_id(youtube_url)
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}&t={seconds}s"

    join_char = "&" if "?" in youtube_url else "?"
    return f"{youtube_url}{join_char}t={seconds}s"


def save_markdown(
    title: str,
    source_url: str,
    channel: str,
    published_date: str,
    transcript_entries: list[tuple[int, str]],
    transcript_text: str,
    tickers: list[str],
    output_dir: Path,
) -> Path:
    """Save the final note as a Markdown file."""
    markdown_filename = f"{sanitize_filename(title)}.md"
    markdown_path = output_dir / markdown_filename

    ticker_tags = generate_ticker_tags(tickers)

    tags_text = " ".join(f"#{tag}" for tag in ticker_tags)
    tickers_text = "\n".join(f"- {ticker}" for ticker in tickers) if tickers else "None detected."
    if transcript_entries:
        raw_transcript_text = "\n".join(
            f"- [{format_timestamp(seconds)}]({build_timestamp_link(source_url, seconds)}) {text}"
            for seconds, text in transcript_entries
        )
    else:
        raw_transcript_text = transcript_text

    markdown_content = (
        f"# {published_date} | {channel}\n\n"
        f"Source URL: {source_url}\n"
        f"Video Title: {title}\n"
        f"Channel: {channel}\n"
        f"Published Date: {published_date}\n\n"
        f"Tags: {tags_text}\n\n"
        f"---\n\n"
        f"## Mentioned Tickers\n\n"
        f"{tickers_text}\n\n"
        f"---\n\n"
        f"## Raw Transcript\n\n"
        f"{raw_transcript_text}\n"
    )

    markdown_path.write_text(markdown_content, encoding="utf-8")
    return markdown_path


def main() -> None:
    output_dir = get_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)

    youtube_url = input("Please enter a YouTube URL: ").strip()
    if not youtube_url:
        print("URL is empty. Exiting.")
        return

    print("1) Downloading audio with yt-dlp...")
    video_data = download_audio(youtube_url, output_dir)
    title = video_data["title"]
    audio_path = video_data["audio_path"]

    print("2) Transcribing audio with faster-whisper...")
    transcript_entries = transcribe_chinese_audio(audio_path)
    transcript_text = "\n".join(text for _, text in transcript_entries)
    if not transcript_text.strip():
        transcript_text = "No speech detected."

    detected_tickers, matched_aliases = detect_tickers_with_matches(transcript_text)
    if detected_tickers:
        print("Detected ticker aliases:")
        for ticker in detected_tickers:
            alias_text = ", ".join(matched_aliases.get(ticker, []))
            print(f"- {ticker} <- {alias_text}")
    else:
        print("Detected ticker aliases: none")

    print("3) Saving Markdown note...")
    markdown_path = save_markdown(
        title=title,
        source_url=youtube_url,
        channel=video_data["channel"],
        published_date=video_data["published_date"],
        transcript_entries=transcript_entries,
        transcript_text=transcript_text,
        tickers=detected_tickers,
        output_dir=output_dir,
    )

    print(f"Done! Markdown saved to: {markdown_path}")


if __name__ == "__main__":
    main()
