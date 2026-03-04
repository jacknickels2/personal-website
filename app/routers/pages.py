"""Page routes for the website."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="templates")
limiter = Limiter(key_func=get_remote_address)


@router.get("/", response_class=HTMLResponse)
@limiter.limit(f"{settings.rate_limit_per_minute}/minute")
async def home(request: Request):
    """Home page."""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Home"}
    )


@router.get("/about", response_class=HTMLResponse)
@limiter.limit(f"{settings.rate_limit_per_minute}/minute")
async def about(request: Request):
    """About page."""
    return templates.TemplateResponse(
        "about.html",
        {"request": request, "title": "About"}
    )


@router.get("/projects", response_class=HTMLResponse)
@limiter.limit(f"{settings.rate_limit_per_minute}/minute")
async def projects(request: Request):
    """Projects page."""
    return templates.TemplateResponse(
        "projects.html",
        {"request": request, "title": "Projects"}
    )


@router.get("/contact", response_class=HTMLResponse)
@limiter.limit(f"{settings.rate_limit_per_minute}/minute")
async def contact(request: Request):
    """Contact page."""
    return templates.TemplateResponse(
        "contact.html",
        {"request": request, "title": "Contact"}
    )
