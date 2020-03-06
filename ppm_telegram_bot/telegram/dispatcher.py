from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from ppm_telegram_bot.telegram.bot import bot

dispatcher = Dispatcher(bot)
dispatcher.middleware.setup(LoggingMiddleware())
