from fastapi import APIRouter

from app.api.v1.routers import exchange_rates, analytics, health

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(exchange_rates.router)
api_router.include_router(analytics.router)
