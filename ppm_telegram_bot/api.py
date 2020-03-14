"""
App entry point which register FastAPI routers.

More info about used app structure: https://fastapi.tiangolo.com/tutorial/bigger-applications/

If you want to create a new API endpoint add endpoint handler to existed router or
create a new module in `routes` directory.
"""
from fastapi import FastAPI
from fastapi.routing import APIRoute

import ppm_telegram_bot
from ppm_telegram_bot.routers import (
    telegram,
    triggers,
)

app = FastAPI(title="PPM Telegram Bot", version=ppm_telegram_bot.__version__,)
app.include_router(telegram.router, prefix="/telegram", tags=["telegram"])
app.include_router(triggers.router, prefix="/triggers", tags=["triggers"])

# Simplify route names in OpenAPI. Idea from https://fastapi-utils.davidmontague.xyz/user-guide/openapi/
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name
