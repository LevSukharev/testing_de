import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=("/.env.dev"),#, "../src/.env.secret"),
        env_file_encoding="utf-8",
    )

    # row_reports_path: str

    host: str = os.getenv("HOST")
    dbname: str = os.getenv("DB")
    user: str = os.getenv("USER")
    password: str = os.getenv("PASSWORD")
    port: int = os.getenv("PORT")

    url_api: str = os.getenv("URL_API")


settings = Settings()
