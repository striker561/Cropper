import os
import json
from .logger import logger


class TrackLoader:
    """
    Loads track crop instructions from crop.json or provides defaults.
    """

    def __init__(self, crop_json_path="crop.json"):
        self.crop_json_path = crop_json_path

    def load_tracks(self):
        """
        Loads tracks from crop.json if present. If not, logs a message and returns an empty list.
        :return: List of track dicts
        """
        if os.path.exists(self.crop_json_path):
            logger.info(f"Loading crop instructions from {self.crop_json_path}")
            try:
                with open(self.crop_json_path, "r", encoding="utf-8") as f:
                    tracks = json.load(f)
                if not isinstance(tracks, list):
                    logger.error("crop.json must contain a list of track dicts.")
                    return []
                return tracks
            except Exception as e:
                logger.error(f"Failed to load crop.json: {e}")
                return []
        else:
            logger.error(
                "No crop.json found. Please create one as described in the README and try again."
            )
            return []
