"""
Module with message handlers and FSM-schemas.

Example: https://github.com/aiogram/aiogram/blob/dev-2.x/examples/finite_state_machine_example.py
Documentation: https://aiogram.readthedocs.io/en/latest/dispatcher/fsm.html

NOTE: This module should be manually imported somewhere for being reachable.
In aiogram v3 it can be changed: https://t.me/aiogram_ru/167702
"""
from aiogram import types

from ppm_telegram_bot.telegram.dispatcher import dispatcher


@dispatcher.message_handler(commands=['healthcheck'])
async def echo_health_check(message: types.Message) -> None:
    await dispatcher.bot.send_message(message.chat.id, message.text)
