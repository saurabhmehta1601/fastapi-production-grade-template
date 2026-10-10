# This module is the main entry point that runs fastapi in development or production environment
# You can use commands like:
#   1. fastapi dev app/main.py or fastapi run app/main.py --workers 4
#   2. uvicorn app.main:app

import uvicorn
from app.factory import create_app
from app.core.config import get_settings

app = (
    create_app()
)  # dont put inside any block, put it at top level only so that fastapi cli / uvicorn cli can pick app to run.

if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(app)
