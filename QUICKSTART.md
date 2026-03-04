# Quick Start Guide

## 🚀 Local Development

1. **Start the development server:**
   ```bash
   ./dev.sh
   ```
   Or manually:
   ```bash
   source .venv/bin/activate
   uvicorn app.main:app --reload
   ```

2. **Visit:** http://localhost:8000

## 🐳 Docker Deployment

1. **Build and run:**
   ```bash
   docker-compose up -d
   ```

2. **Check logs:**
   ```bash
   docker-compose logs -f web
   ```

3. **Stop:**
   ```bash
   docker-compose down
   ```

## 🌐 Cloudflared Setup

1. **Update your cloudflared config** with the content from `cloudflared-config-example.yml`

2. **Reload cloudflared:**
   ```bash
   sudo systemctl restart cloudflared
   # or if running manually:
   cloudflared tunnel run YOUR_TUNNEL_NAME
   ```

3. **Your site will be available at:**
   - https://nicholascox.dev
   - https://www.nicholascox.dev

## 🔒 Security Notes

- ✅ Secret key is generated and stored in `.env`
- ✅ Rate limiting is enabled (60 requests/minute by default)
- ✅ Security headers are configured
- ✅ Host validation is active
- ✅ Docker runs as non-root user

## 📝 Customization

### Update Content
Edit files in `templates/` directory:
- `index.html` - Home page
- `about.html` - About page
- `projects.html` - Projects showcase
- `contact.html` - Contact page

### Update Styles
Edit `static/css/style.css`

### Add New Pages
1. Create HTML template in `templates/`
2. Add route in `app/routers/pages.py`

### Add ML/AI Features
Create new router in `app/routers/` directory. Example:

```python
# app/routers/ml_demo.py
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api", tags=["ml"])

@router.post("/predict")
async def predict(data: dict):
    # Your ML model logic here
    return {"prediction": "result"}
```

Then include it in `app/main.py`:
```python
from app.routers import ml_demo
app.include_router(ml_demo.router)
```

## 🔧 Maintenance

### Update Dependencies
```bash
uv pip install --upgrade -r pyproject.toml
```

### Rebuild Docker Image
```bash
docker-compose build --no-cache
docker-compose up -d
```

### Check Application Health
```bash
curl http://localhost:8000/health
```

## 📊 Monitoring

Watch logs in real-time:
```bash
# Docker
docker-compose logs -f web

# Local
# Logs are output to stdout when running with uvicorn
```
