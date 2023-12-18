from fastapi import FastAPI, Body, Request
from fastapi.responses import RedirectResponse
from secrets import token_hex

from app.resources.app import router


app = FastAPI()
app.include_router(router)
