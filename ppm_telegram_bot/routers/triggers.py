"""
We have a special service for new talk requests (calls for paper), so we
should notify meetup organizers in chat about errors and new talk requests.
"""
from aiogram import Bot
from fastapi import (
    APIRouter,
    Depends,
)
from pydantic import (
    BaseModel,
    HttpUrl,
)
from starlette.responses import Response

from ppm_telegram_bot import templates
from ppm_telegram_bot.dependencies import telegram_bot
from ppm_telegram_bot.settings import settings

router = APIRouter()


class Message(BaseModel):
    message: str


class TalkInfo(BaseModel):
    speaker_name: str
    talk_name: str
    talk_dates: str
    notion_url: HttpUrl


class EmptyResponse(BaseModel):
    ...


@router.post("/talk_new", response_model=EmptyResponse)
async def talk_new(talk: TalkInfo, bot: Bot = Depends(telegram_bot)) -> None:
    message = templates.new_talk.format(**talk.dict())
    await bot.send_message(chat_id=settings.ORG_CHAT_ID, text=message)


@router.post("/typeform_invalid", response_model=EmptyResponse)
async def typeform_invalid(bot: Bot = Depends(telegram_bot)) -> None:
    await bot.send_message(
        chat_id=settings.ORG_CHAT_ID, text=templates.typeform_invalid
    )


@router.post("/notion_error", response_model=EmptyResponse)
async def notion_error(bot: Bot = Depends(telegram_bot)) -> None:
    await bot.send_message(chat_id=settings.ORG_CHAT_ID, text=templates.notion_error)
