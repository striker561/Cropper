"""
Main entry point for the audio teaser generator.
"""

import os
import json
from cropper.logger import logger
from cropper.teaser_batcher import TeaserBatcher

INPUT_FOLDER = "input_audio"
OUTPUT_FOLDER = "output_teasers"
FADE_DURATION_MS = 500  # 0.5 seconds
CROP_JSON = "crop.json"


def load_tracks():
    if os.path.exists(CROP_JSON):
        logger.info(f"Loading crop instructions from {CROP_JSON}")
        try:
            with open(CROP_JSON, "r", encoding="utf-8") as f:
                tracks = json.load(f)
            if not isinstance(tracks, list):
                logger.error("crop.json must contain a list of track dicts.")
                return []
            return tracks
        except Exception as e:
            logger.error(f"Failed to load crop.json: {e}")
            return []
    else:
        logger.warning("No crop.json found. Using default example tracks.")
        return [
            {"filename": "song1.mp3", "start": 30, "end": 60},
            {"filename": "song2.wav", "start": 10, "end": 25},
        ]


def main():
    tracks = load_tracks()
    if not tracks:
        logger.error("No tracks to process. Exiting.")
        return
    batcher = TeaserBatcher(INPUT_FOLDER, OUTPUT_FOLDER, fade_ms=FADE_DURATION_MS)
    batcher.process_tracks(tracks)


if __name__ == "__main__":
    main()
