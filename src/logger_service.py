from loguru import logger
import os
import pathlib
import sys

ROOT_DIR = pathlib.Path(__file__).parent.absolute()
LOG_FILE_PATH = os.path.join(ROOT_DIR, '../logs/loguru.log')

logger.remove()
logger.add(LOG_FILE_PATH, level="INFO", rotation="1 MB")
logger.add(sys.stderr, level="INFO")
