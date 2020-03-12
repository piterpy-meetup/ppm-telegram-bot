# Welcome to ppm-telegram-bot 👋
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> Telegram Bot Platform integration for bot commands processing. We use it for our internal @piterpy-meetup needs, basically, to manage things via Telegram.

## Install

We use `poetry` to manage dependencies, so it's the fastest way to install them:

```sh
poetry install
```

## Usage
In general, ppm-telegram-bot is just a FastAPI web app with aiogram to interact with Telegram.

To run it you can use any ASGI server like [uvicorn](https://www.uvicorn.org/),
[gunicorn with uvicorn workers](https://www.uvicorn.org/deployment/#gunicorn)
or [daphne](https://github.com/django/daphne/#running), e.g.:

```sh
uvicorn ppm_telegram_bit.api:app
```

## Deployment

We currently use awesome [kintohub](https://kintohub.com) to run the app in a Docker container as a serverless web app. 

## Development

Please, carefully read docstrings in all modules, they usually contain useful info and hints.

## Show your support

Give us a ⭐️ if you like this project!


***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
