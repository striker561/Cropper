import os
import time
from typing import List, Dict
from .audio_processor import AudioProcessor
from .logger import logger


class TeaserBatcher:
    """
    Handles batch processing of multiple audio tracks for teaser generation.
    """

    def __init__(self, input_folder: str, output_folder: str, fade_ms: int = 500):
        """
        Initialize the batch processor.
        :param input_folder: Directory containing input audio files.
        :param output_folder: Directory to save output teasers.
        :param fade_ms: Fade-in/out duration in milliseconds.
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.audio_processor = AudioProcessor(fade_ms=fade_ms)
        os.makedirs(self.output_folder, exist_ok=True)

    def process_tracks(self, tracks: List[Dict]):
        """
        Process a list of track dictionaries, cropping and fading each, and saving to output folder.
        :param tracks: List of dicts with keys 'filename', 'start', 'end'.
        """
        total = len(tracks)
        if total == 0:
            logger.warning("No tracks to process.")
            return
        logger.info(f"Starting batch processing of {total} tracks...")
        start_time = time.time()
        processed = 0
        for idx, track in enumerate(tracks, 1):
            filename = track.get("filename")
            start = track.get("start")
            end = track.get("end")
            if not filename or start is None or end is None:
                logger.warning(f"Skipping invalid track entry: {track}")
                continue
            input_path = os.path.join(self.input_folder, filename)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(self.output_folder, f"{name}_teaser{ext}")
            logger.info(
                f"[{idx}/{total}] Processing: {filename} ({start}s - {end}s)..."
            )
            # Crop and fade the audio, ensuring high quality
            success = self.audio_processor.crop_and_fade(
                input_path, output_path, start, end
            )
            if success:
                logger.info(f"Done: {output_path}")
                processed += 1
            else:
                logger.error(f"Failed: {filename}")
        elapsed = time.time() - start_time
        logger.info(
            f"\nBatch processing complete.\nTracks processed: {processed}/{total}\nTotal time: {elapsed:.2f} seconds\n"
        )
