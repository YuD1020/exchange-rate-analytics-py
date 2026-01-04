from fastapi import APIRouter, Depends

from app.services.exchange_rate_service import ExchangeRateService
from app.repositories.exchange_rate_repository import ExchangeRateRepository

router = APIRouter(prefix="/exchange-rates", tags=["Exchange Rates"])


def get_exchange_rate_service() -> ExchangeRateService:
    repo = ExchangeRateRepository()
    return ExchangeRateService(repo)


@router.get("/")
def get_exchange_rates(
    service: ExchangeRateService = Depends(get_exchange_rate_service),
):
    return service.get_exchange_rates()
