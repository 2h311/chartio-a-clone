from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "chartio/index.html", context={"request": request}
    )


@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(
        "chartio/login.html", context={"request": request}
    )


@router.get("/users/password/reset")
async def password_reset(request: Request):
    return templates.TemplateResponse(
        "chartio/password_reset.html", context={"request": request}
    )


@router.get("/users/password/reset/email-sent")
async def password_reset(request: Request):
    return templates.TemplateResponse(
        "chartio/email_sent.html", context={"request": request}
    )


@router.get("/product/support")
async def support(request: Request):
    return templates.TemplateResponse(
        "chartio/support.html", context={"request": request}
    )
