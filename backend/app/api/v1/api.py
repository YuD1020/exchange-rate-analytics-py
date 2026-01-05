from fastapi import APIRouter

from app.api.v1.routers import exchange_rates

api_router = APIRouter()
api_router.include_router(exchange_rates.router)
