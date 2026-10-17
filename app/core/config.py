from typing import Literal
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

__all__ = ["Settings", "get_settings"]

class Settings(BaseSettings):
    APP_NAME: str = "My Production grade FastAPI app"
    DATABASE_URL: SecretStr
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    ENVIRONMENT: Literal["development", "production"] = "production"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings():
    return Settings()
