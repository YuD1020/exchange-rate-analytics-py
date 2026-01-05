from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Exchange Rate Analytics")

app.include_router(api_router, prefix="/api/v1")
