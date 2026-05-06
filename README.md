# youtube-learning-capture

Minimal MVP pipeline:

YouTube URL -> download audio with `yt-dlp` -> transcribe with `faster-whisper` -> save a Markdown note.

## Project structure

```text
youtube-learning-capture/
├── transcribe_youtube.py
├── outputs/
├── requirements.txt
├── README.md
└── .gitignore
```

## 1) Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Also install FFmpeg (required by `yt-dlp` audio conversion):

```bash
brew install ffmpeg
```

## 2) Run

```bash
python transcribe_youtube.py
```

Then paste a YouTube URL when prompted.

## 3) Output

The script generates a Markdown file in `outputs/` with:

- title
- source URL
- transcript
