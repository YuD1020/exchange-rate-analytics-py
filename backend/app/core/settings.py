from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Exchange Rate Analytics API"
    environment: str = "development"

    database_url: str = "sqlite:///./exchange_rates.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
