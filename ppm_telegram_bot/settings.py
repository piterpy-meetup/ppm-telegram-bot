"""
Validates environment variables during import-time and provides `settings` singletone.

More info about pydantic settings: https://pydantic-docs.helpmanual.io/usage/settings/
"""

from pydantic import (
    BaseSettings,
    SecretStr,
)


class Settings(BaseSettings):
    TELEGRAM_BOT_API_KEY: SecretStr
    TELEGRAM_BOT_WEBHOOK_ENDPOINT: str
    TELEGRAM_BOT_WEBHOOK_SECRET: SecretStr
    ORG_CHAT_ID: str


settings = Settings()
