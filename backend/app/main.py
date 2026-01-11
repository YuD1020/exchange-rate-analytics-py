from app.api.v1.routers import analytics
from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Exchange Rate Analytics")

app.include_router(api_router, prefix="/api/v1")

app.include_router(analytics.router, prefix="/api/v1/analytics")