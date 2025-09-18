import logging

# Configure a single logger for the whole package
logger = logging.getLogger("cropper")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "\n[%(asctime)s] [%(levelname)s]\n%(message)s\n", datefmt="%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)
