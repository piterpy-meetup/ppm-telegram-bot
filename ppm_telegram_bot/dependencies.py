"""
FastAPI provides Dependency Injection system, so we implement a few.

More info about dependencies: https://fastapi.tiangolo.com/tutorial/dependencies/

It is better to create a new dependency if you want to use
something in your endpoint handler (telegram bot, security check, external library).
"""
from aiogram import (
    Dispatcher,
    Bot,
)

from ppm_telegram_bot.telegram.dispatcher import dispatcher


def bot_dispatcher() -> Dispatcher:
    """
    Set context manually for properly processing webhook updates.

    Source: https://t.me/aiogram_ru/167051
    """
    Bot.set_current(dispatcher.bot)
    Dispatcher.set_current(dispatcher)
    return dispatcher


def telegram_bot() -> Bot:
    return dispatcher.bot
