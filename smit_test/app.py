from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from smit_test.settings import tortoise_config

app = FastAPI()
register_tortoise(app, config=tortoise_config, add_exception_handlers=True)

from smit_test.api.router import api_router

app.include_router(api_router)
