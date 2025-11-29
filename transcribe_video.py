#!/usr/bin/env python3
import sys
import subprocess
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

def transcribe_video(video_path):
    """Convert video to audio and transcribe to text."""
    video_file = Path(video_path)
    if not video_file.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    # Extract audio using ffmpeg
    audio_file = video_file.with_suffix('.wav')
    subprocess.run([
        'ffmpeg', '-i', str(video_file), '-vn', '-acodec', 'pcm_s16le',
        '-ar', '16000', '-ac', '1', str(audio_file), '-y'
    ], check=True, capture_output=True)
    
    # Transcribe using whisper
    import whisper
    model = whisper.load_model("base")
    result = model.transcribe(str(audio_file))
    
    # Save transcription
    output_file = video_file.with_suffix('.txt')
    output_file.write_text(result['text'])
    
    print(f"Transcription saved to: {output_file}")
    return result['text']

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe_video.py <video_file>")
        sys.exit(1)
    
    transcribe_video(sys.argv[1])
