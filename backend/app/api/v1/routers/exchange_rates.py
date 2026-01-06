from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.exchange_rate_repository import ExchangeRateRepository
from app.services.exchange_rate_service import ExchangeRateService

router = APIRouter(prefix="/exchange-rates", tags=["Exchange Rates"])


@router.get("/")
def get_exchange_rates(
    sort_by: str | None = None, order: str = "asc", db: Session = Depends(get_db)
):
    repo = ExchangeRateRepository(db)
    service = ExchangeRateService(repo)
    return service.list_rates()
