# Welcome to ppm-telegram-bot 👋
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> Integration with telegram via bot platform. Uses for internal meetup needs

## Install

We use `poetry` as dependency manager, so it's the fastest way to install all stuff:

```sh
poetry install
```

## Usage
In general, app is just FastAPI-based web-app with aiogram for interaction with telegram. So, for running it, you can
 use any ASGI server, e.g. uvicorn:

```sh
uvicorn ppm_telegram_bit.api:app
```

## Deployment

We currently use awesome [kintohub](https://kintohub.com) to run a docker container as serverless web-app. 

## Development

Please, carefully read docstring in all modules: they usually contains info and hints.

## Show your support

Give a ⭐️ if you like this project


***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_