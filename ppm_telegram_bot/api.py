"""
App entry point which register FastAPI routers.

More info about used app structure: https://fastapi.tiangolo.com/tutorial/bigger-applications/

If you want to create a new API endpoint add endpoint handler to existed router or
create a new module in `routes` directory.
"""
from fastapi import FastAPI
from fastapi.routing import APIRoute

from ppm_telegram_bot.routers import (
    telegram,
    triggers,
)

app = FastAPI()
app.include_router(telegram.router, prefix="/telegram", tags=["telegram"])
app.include_router(triggers.router, prefix="/triggers", tags=["triggers"])

# Simplify route names in OpenAPI. Idea from https://fastapi-utils.davidmontague.xyz/user-guide/openapi/
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name

# TODO: how to generate http-client via https://github.com/dmontagu/fastapi_client
# ../fastapi_client/scripts/generate.sh -i ~/Downloads/openapi\ \(1\).json -p ppm_telegram_bot_client -o ../ppm-telegram-bot
# from ppm_telegram_bot_client.api_client import ApiClient, AsyncApis
# client = ApiClient(host="http://localhost:8000")
# async_apis = AsyncApis(client)
# await async_apis.triggers_api.notion_error()
