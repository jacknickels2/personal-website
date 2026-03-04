"""Main FastAPI application."""
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.config import settings
from app.security import (
    limiter,
    rate_limit_handler,
    security_headers_middleware,
    validate_host,
)
from app.routers import pages


# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    docs_url=None if not settings.debug else "/docs",
    redoc_url=None if not settings.debug else "/redoc",
    openapi_url=None if not settings.debug else "/openapi.json",
)

# Add rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_handler)

# Add security headers middleware
app.middleware("http")(security_headers_middleware)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(pages.router)


@app.middleware("http")
async def validate_host_middleware(request: Request, call_next):
    """Validate the host header to prevent host header injection."""
    host = request.headers.get("host", "")
    
    if not validate_host(host):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Invalid host header"},
        )
    
    response = await call_next(request)
    return response


@app.get("/health", include_in_schema=False)
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "environment": settings.environment}
