from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from routes import router


templates = Jinja2Templates(directory="templates")


def mount_static(app):
    app.mount("/assets", StaticFiles(directory="static"), name="static")
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_app():
    app = FastAPI(title="Chartio Clone", version="this is a clone version")
    mount_static(app)
    return app


app = start_app()
app.include_router(router)
