import sys
from pathlib import Path
import logging

PROJ_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJ_DIR))
from src.shared.logger import ILogger


class StdLogger(ILogger):
    def __init__(self, name: str = "app") -> None:
        self._logger = logging.getLogger(name)

    def debug(self, msg: str) -> None:
        self._logger.debug(msg)

    def info(self, msg: str) -> None:
        self._logger.info(msg)

    def warning(self, msg: str) -> None:
        self._logger.warning(msg)

    def error(self, msg: str) -> None:
        self._logger.error(msg)

    def critical(self, msg: str) -> None:
        self._logger.critical(msg)
