#!/usr/bin/python3
"""Base settings for the application."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for environment variables."""

    FLIGHT_API_URL: str
    X_RapidAPI_Key: str
    X_RapidAPI_Host: str

    class Config:
        """Configuration for environment variables."""

        env_file = "./.env"


settings = Settings()
