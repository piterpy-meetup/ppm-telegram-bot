"""
Endpoint for telegram webhook.

One way to receive events from telegram is webhook: for each event (e.g. somebody writes to the bot or tap the button)
telegram sends to us data about events. We should return "200 OK" and then do processing of new event.

More info about webhook mechanism: https://core.telegram.org/bots/webhooks
"""
from secrets import compare_digest

from aiogram import Dispatcher
from aiogram.types import Update
from fastapi import (
    APIRouter,
    Depends,
)
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_200_OK
from ppm_telegram_bot.dependencies import (
    bot_dispatcher,
    telegram_bot,
)
from ppm_telegram_bot.settings import settings

router = APIRouter()


@router.post("/webhook/{secret}")
async def telegram_webhook(
    secret: str, request: Request, dp: Dispatcher = Depends(bot_dispatcher)
) -> Response:
    """
    Pass the new update (event from telegram) to bot dispatcher for processing.

    Also checks `secret` in URL, so we build a little security around getting new updates.
    """
    real_secret = settings.TELEGRAM_BOT_WEBHOOK_SECRET.get_secret_value()
    if not compare_digest(secret, real_secret):
        raise HTTPException(status_code=403)

    telegram_update_dict = await request.json()
    telegram_update = Update(**telegram_update_dict)
    await dp.process_update(telegram_update)
    return Response(status_code=HTTP_200_OK)


@router.on_event("startup")
async def set_webhook() -> None:
    """
    Tell Telegram API about new webhook on app startup.

    We need to check current webhook url first, because Telegram API has
    strong rate limit for `set_webhook` method.
    """
    bot = telegram_bot()
    url = (
        settings.TELEGRAM_BOT_WEBHOOK_ENDPOINT
        + settings.TELEGRAM_BOT_WEBHOOK_SECRET.get_secret_value()
    )
    current_url = (await bot.get_webhook_info())["url"]
    if current_url != url:
        await bot.set_webhook(url=url)


@router.on_event("shutdown")
async def disconnect_storage() -> None:
    """
    Close connection to storage.

    We don't use storage at this moment, but in future...
    """
    dispatcher = bot_dispatcher()
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
