from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


templates = Jinja2Templates(directory="templates")


def mount_static(app):
    app.mount("/assets", StaticFiles(directory="static"), name="static")


def start_app():
    app = FastAPI(title="Chartio Clone", version="this is a clone version")
    mount_static(app)
    return app


app = start_app()


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "chartio/index.html", context={"request": request}
    )


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(
        "chartio/login.html", context={"request": request}
    )
