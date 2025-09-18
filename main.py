"""
Main entry point for the audio teaser generator.
"""

from cropper.teaser_batcher import TeaserBatcher
from cropper.track_loader import TrackLoader

INPUT_FOLDER = "input_audio"
OUTPUT_FOLDER = "output_teasers"
FADE_DURATION_MS = 500  # 0.5 seconds


def main():
    loader = TrackLoader()
    tracks = loader.load_tracks()
    if not tracks:
        from cropper.logger import logger

        logger.error("No tracks to process. Exiting.")
        return
    batcher = TeaserBatcher(INPUT_FOLDER, OUTPUT_FOLDER, fade_ms=FADE_DURATION_MS)
    batcher.process_tracks(tracks)


if __name__ == "__main__":
    main()
