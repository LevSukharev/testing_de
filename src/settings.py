from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("../.env.dev", "../.env.secret"),
        env_file_encoding="utf-8",
    )

    debug: bool
    host: str
    dbname: str
    user: str
    password: str
    port: int

    url_api: str


settings = Settings()
