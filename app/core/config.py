from typing import Literal, Any
from pydantic import SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

__all__ = ["Settings", "get_settings"]

class Settings(BaseSettings):
    app_name: str = "My Production grade FastAPI app"
    database_url: SecretStr
    access_token_expire_minutes: int
    refresh_token_expire_days: int
    environment: Literal["development", "production"] = "production"
    allow_origins: str | list[str] = ["*"] # settup using comma separated string of allowed origins from env var

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @field_validator("allow_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, v: Any) -> list[str] | Any:
        if isinstance(v, str):
            return [s.strip() for s in v.split(",")]
        return []


@lru_cache
def get_settings():
    return Settings()
