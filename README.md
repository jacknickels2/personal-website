# Personal Website

A secure, modern personal portfolio website built with FastAPI, featuring a clean design and ready for deployment via Docker and Cloudflare Tunnel.

## Features

- 🚀 **FastAPI** - Modern, fast Python web framework
- 🔒 **Security Hardened** - Rate limiting, security headers, CSP, host validation
- 🐳 **Docker Ready** - Multi-stage builds with non-root user
- 🎨 **Responsive Design** - Mobile-first, modern UI
- ⚡ **High Performance** - Optimized for speed and efficiency
- 🔧 **Developer Friendly** - Uses mise and uv for environment management

## Security Features

- Rate limiting on all endpoints
- Security headers (CSP, HSTS, X-Frame-Options, etc.)
- Host header validation
- Non-root user in Docker
- No debug endpoints in production
- Input validation with Pydantic
- Regular dependency updates

## Setup

### Prerequisites

- [mise](https://mise.jdx.dev/) - Development environment manager
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer
- Docker and Docker Compose
- Git / GitHub CLI (gh)

### Local Development

1. **Install dependencies:**
   ```bash
   mise install
   uv pip install -e ".[dev]"
   ```

2. **Create environment file:**
   ```bash
   cp .env.example .env
   # Edit .env and set your SECRET_KEY and other variables
   ```

3. **Generate a secret key:**
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```

4. **Run the development server:**
   ```bash
   uvicorn app.main:app --reload
   ```

   Visit http://localhost:8000

### Docker Deployment

1. **Create .env file:**
   ```bash
   cp .env.example .env
   # Edit .env with production values
   ```

2. **Build and run:**
   ```bash
   docker-compose up -d
   ```

3. **View logs:**
   ```bash
   docker-compose logs -f
   ```

4. **Stop:**
   ```bash
   docker-compose down
   ```

## Cloudflare Tunnel Configuration

To expose your site via Cloudflare Tunnel, add this to your cloudflared config:

```yaml
ingress:
  - hostname: nicholascox.dev
    service: http://localhost:8000
  - hostname: www.nicholascox.dev
    service: http://localhost:8000
  # ... other services
  - service: http_status:404
```

Then reload your tunnel configuration.

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── config.py        # Configuration management
│   ├── security.py      # Security middleware
│   └── routers/
│       └── pages.py     # Page routes
├── templates/           # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   └── contact.html
├── static/
│   └── css/
│       └── style.css    # Styles
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml       # Python dependencies
└── .mise.toml          # Development environment

```

## Customization

1. **Update content** in `templates/*.html` files
2. **Modify styles** in `static/css/style.css`
3. **Add new pages** by creating routes in `app/routers/pages.py`
4. **Add ML demos** by creating new routers in `app/routers/`

## Security Checklist

- [ ] Set a strong SECRET_KEY in .env
- [ ] Update ALLOWED_HOSTS in .env
- [ ] Keep dependencies updated
- [ ] Use HTTPS (handled by Cloudflare Tunnel)
- [ ] Monitor logs for suspicious activity
- [ ] Regular security audits

## License

© 2026 Nicholas Cox. All rights reserved.
