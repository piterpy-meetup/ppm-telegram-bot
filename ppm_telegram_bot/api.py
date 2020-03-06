from fastapi import FastAPI

from ppm_telegram_bot.routers import telegram

app = FastAPI()
app.include_router(telegram.router)
