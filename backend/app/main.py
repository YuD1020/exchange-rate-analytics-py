from fastapi import FastAPI
from app.core.settings import settings
from app.api.exchange_rates import router as exchange_rates_router

app = FastAPI(title=settings.app_name)

app.include_router(exchange_rates_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment
    }


