from fastapi import FastAPI

from smit_test.api import api_router

app = FastAPI()

app.include_router(api_router)
