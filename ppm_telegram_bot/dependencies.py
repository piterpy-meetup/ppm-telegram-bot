from aiogram import (
    Dispatcher,
    Bot,
)

from ppm_telegram_bot.telegram import dispatcher

# TODO: добавить sub-dependency для бота


def bot_dispatcher() -> Dispatcher:
    """
    Set context manually for properly processing webhook updates.

    Source: https://t.me/aiogram_ru/167051
    """
    Bot.set_current(dispatcher.bot)
    Dispatcher.set_current(dispatcher)
    return dispatcher
