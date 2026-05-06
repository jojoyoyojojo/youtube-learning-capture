# youtube-learning-capture

一个轻量的 YouTube 学习笔记 MVP：

YouTube URL -> `yt-dlp` 下载音频 -> `faster-whisper` 转写 -> 生成 Markdown 笔记

## 功能概览

- 输入 YouTube 链接，自动下载音频
- 使用 `faster-whisper` 做中文转写
- 自动识别提到的 ticker（基于 `tickers.py` 规则）
- 自动生成标签（基于 `TICKER_TAGS`）
- 转写附带可点击时间戳链接（适配 Obsidian，跳转到 YouTube 指定秒数）

## 项目结构

```text
youtube-learning-capture/
├── transcribe_youtube.py
├── tickers.py
├── config.example.json
├── outputs/
├── requirements.txt
├── README.md
└── .gitignore
```

## 环境准备

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

安装 FFmpeg（`yt-dlp` 音频转换依赖）：

```bash
brew install ffmpeg
```

## 运行方式

```bash
python transcribe_youtube.py
```

运行后粘贴一个 YouTube URL 即可。

## 输出目录配置（可选）

默认输出到 `outputs/`。  
如果你希望直接输出到本地 Obsidian Vault，可创建 `config.local.json`：

```json
{
  "output_dir": "/your/local/path/to/obsidian/folder"
}
```

说明：

- `config.local.json` 仅用于本地，不会提交到 Git（已在 `.gitignore`）
- 如果 `config.local.json` 不存在或格式无效，脚本会自动回退到 `outputs/`

## 生成的 Markdown 内容

- 标题：`Published Date | Channel`
- `Source URL`
- `Video Title`
- `Channel`
- `Published Date`
- `Tags`（由检测到的 ticker 自动聚合）
- `Mentioned Tickers`
- `Raw Transcript`（每行带 YouTube 时间戳链接）
