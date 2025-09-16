import sys
from pathlib import Path
import logging

PROJ_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJ_DIR))
from src.shared.alert import IAlertManager


class StdAlertManager(IAlertManager):
    def alert(self, msg: str) -> None:
        print(f"[ALERT] {msg}")
