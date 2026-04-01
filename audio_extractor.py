from distutils.command.install import install


pip install pytube # type: ignore
pip install openai-whisper
pip install torch torchvision torchaudioimport pytube

import whisper
import os

class AudioExtractor:
    def __init__(self):
        self.model = whisper.load_model("base")

    def download_audio(self, youtube_url: str, output_path: str = "temp") -> str:
        """Download audio from YouTube video"""
        try:
            # Create temp directory if it doesn't exist
            os.makedirs(output_path, exist_ok=True)
            
            # Download YouTube video audio
            yt = pytube.YouTube(youtube_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_file = audio_stream.download(output_path)
            
            return audio_file
        except Exception as e:
            raise Exception(f"Error downloading audio: {str(e)}")

    def transcribe_audio(self, audio_file: str) -> str:
        """Convert audio to text using Whisper"""
        try:
            # Transcribe audio to text
            result = self.model.transcribe(audio_file)
            
            # Clean up temporary audio file
            os.remove(audio_file)
            
            return result["text"]
        except Exception as e:
            raise Exception(f"Error transcribing audio: {str(e)}")

    def process_video(self, youtube_url: str) -> str:
        """Process YouTube video: download audio and transcribe to text"""
        audio_file = self.download_audio(youtube_url)
        transcript = self.transcribe_audio(audio_file)
        return transcript