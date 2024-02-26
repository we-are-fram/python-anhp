import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")
    DB_NAME: str = os.getenv("DB_NAME", "postgres")

    DB_TYPE: str = os.environ.get("DB_TYPE", "postgresql")
    DB_URI: str = f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    BACKEND_CORS_ORIGINS: list = ["http://localhost:8000"]


settings = Settings()
