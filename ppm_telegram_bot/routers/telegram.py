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
from ppm_telegram_bot.telegram import (
    bot,
    dispatcher,
)
from ppm_telegram_bot.dependencies import bot_dispatcher
from ppm_telegram_bot.settings import settings

router = APIRouter()


@router.post("/telegram/webhook/{secret}")
async def telegram_webhook(
    secret: str, request: Request, bot_dispatcher: Dispatcher = Depends(bot_dispatcher)
) -> Response:
    real_secret = settings.TELEGRAM_BOT_WEBHOOK_SECRET.get_secret_value()
    if not compare_digest(secret, real_secret):
        raise HTTPException(status_code=403)

    telegram_update_dict = await request.json()
    telegram_update = Update(**telegram_update_dict)
    await bot_dispatcher.process_update(telegram_update)
    return Response(status_code=HTTP_200_OK)


@router.on_event("startup")
async def on_startup() -> None:
    url = (
        settings.TELEGRAM_BOT_WEBHOOK_ENDPOINT
        + settings.TELEGRAM_BOT_WEBHOOK_SECRET.get_secret_value()
    )
    current_url = (await bot.get_webhook_info())["url"]
    if current_url != url:
        await bot.set_webhook(url=url)


@router.on_event("shutdown")
async def on_shutdown() -> None:
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
