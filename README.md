# Video Transcription Tool

Converts video files to audio and transcribes to text using OpenAI Whisper.

## Installation

```bash
# Install ffmpeg (system dependency)
sudo apt-get install ffmpeg  # Ubuntu/Debian
# or: brew install ffmpeg     # macOS

# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Edit `.env` to set your AWS region and Bedrock model ID if needed.

## Usage

```bash
# Transcribe video
uv run transcribe_video.py video.mp4

# Improve transcript using Bedrock
uv run improve_transcript.py video.txt
```

Output will be saved as `video.txt` and `video_improved.txt` in the same directory.
