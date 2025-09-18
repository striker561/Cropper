import os
from .logger import logger
from pydub import AudioSegment


class AudioProcessor:
    """
    Handles cropping and fading of audio files.
    """

    def __init__(self, fade_ms: int = 500):
        """
        Initialize the audio processor.
        :param fade_ms: Fade-in and fade-out duration in milliseconds.
        """
        self.fade_ms = fade_ms

    def crop_and_fade(
        self, input_path: str, output_path: str, start_sec: float, end_sec: float
    ) -> bool:
        """
        Crop an audio file between start_sec and end_sec, apply fade-in/out, and export at high quality.
        :param input_path: Path to the input audio file.
        :param output_path: Path to save the cropped teaser.
        :param start_sec: Start time in seconds.
        :param end_sec: End time in seconds.
        :return: True if successful, False otherwise.
        """
        if not os.path.exists(input_path):
            logger.error(f"File not found: {input_path}")
            return False

        try:
            # Load the audio file
            audio = AudioSegment.from_file(input_path)
            start_ms = int(start_sec * 1000)
            end_ms = int(end_sec * 1000)
            # Crop and apply fades
            snippet = audio[start_ms:end_ms]
            snippet = snippet.fade_in(self.fade_ms).fade_out(self.fade_ms)
            ext = os.path.splitext(output_path)[1].lower()
            format_ = ext[1:] if ext.startswith(".") else ext
            # Export with high quality settings for both mp3 and wav
            export_args = {}
            if format_ == "mp3":
                export_args["bitrate"] = "320k"  # High quality for mp3
            elif format_ == "wav":
                # Use pydub's set_frame_rate and set_channels for optimal WAV export
                snippet = snippet.set_frame_rate(44100).set_channels(2)
            snippet.export(output_path, format=format_, **export_args)
            return True
        except Exception as e:
            logger.error(f"Error processing {input_path}: {e}")
            return False
