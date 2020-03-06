from aiogram import types

from ppm_telegram_bot.telegram import (
    dispatcher,
    bot,
)


@dispatcher.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)
