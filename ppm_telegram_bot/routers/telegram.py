"""
Endpoint for telegram webhook.

One way to receive events from telegram is webhook: for each event (e.g. somebody writes to the bot or tap the button)
telegram sends to us data about events. We should return "200 OK" and then do processing of new event.

More info about webhook mechanism: https://core.telegram.org/bots/webhooks
"""
from typing import (
    Dict,
    Any,
)

from aiogram import Dispatcher
from aiogram.types import Update
from fastapi import (
    APIRouter,
    Depends,
    Body,
)
from fastapi_security_telegram_webhook import OnlyTelegramNetworkWithSecret
from starlette.responses import Response
from starlette.status import HTTP_200_OK


from ppm_telegram_bot.dependencies import (
    bot_dispatcher,
    telegram_bot,
)
from ppm_telegram_bot.settings import settings

router = APIRouter()
telegram_webhook_security = OnlyTelegramNetworkWithSecret(
    real_secret=settings.TELEGRAM_BOT_WEBHOOK_SECRET.get_secret_value()
)


@router.post("/webhook/{secret}", dependencies=[Depends(telegram_webhook_security)])
async def telegram_webhook(
    update_raw: Dict[str, Any] = Body(...), dp: Dispatcher = Depends(bot_dispatcher),
) -> Response:
    """
    Pass the new update (event from telegram) to bot dispatcher for processing.
    """
    telegram_update = Update(**update_raw)
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
    url = "{endpoint}/{secret}".format(
        endpoint=settings.TELEGRAM_BOT_WEBHOOK_ENDPOINT.rstrip("/"),
        secret=settings.TELEGRAM_BOT_WEBHOOK_SECRET.get_secret_value(),
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
