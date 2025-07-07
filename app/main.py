import logging
from fastapi import FastAPI
from .middleware import configure_middleware
from .routers.chat import router as chat_router

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI(title="Little Compass")

# CORS, etc.
configure_middleware(app)

# include your chat endpoint
app.include_router(chat_router)
