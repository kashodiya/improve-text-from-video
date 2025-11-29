# Video Transcription Tool

Converts video files to audio and transcribes to text using OpenAI Whisper.

## Installation

```bash
# Install ffmpeg (system dependency)
sudo apt-get install ffmpeg  # Ubuntu/Debian
# or: brew install ffmpeg     # macOS

# Install Python dependencies
pip install -r requirements.txt
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
python transcribe_video.py video.mp4

# Improve transcript using Bedrock
python improve_transcript.py video.txt
```

Output will be saved as `video.txt` and `video_improved.txt` in the same directory.
