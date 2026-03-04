#!/bin/bash
# Development server start script

# Activate virtual environment if not already activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    source .venv/bin/activate
fi

# Start the development server with hot reload
echo "Starting FastAPI development server..."
echo "Visit: http://localhost:8000"
echo "Press Ctrl+C to stop"
echo ""

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
