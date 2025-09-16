from pathlib import Path
from pydantic_settings import BaseSettings


ROOT_DIR = Path(__file__).parent


class AppSettings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_file = ".env"


settings = AppSettings(_env_file=ROOT_DIR / ".env")  # type:ignore
