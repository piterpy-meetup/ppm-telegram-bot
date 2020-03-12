from aiogram import Bot

from ppm_telegram_bot.settings import settings

bot = Bot(token=settings.TELEGRAM_BOT_API_KEY.get_secret_value())
