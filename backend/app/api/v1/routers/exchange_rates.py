from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.exchange_rate import ExchangeRateResponse
from app.repositories.exchange_rate_repository import ExchangeRateRepository
from app.services.exchange_rate_service import ExchangeRateService

router = APIRouter(prefix="/exchange-rates", tags=["Exchange Rates"])

@router.get("/", response_model=list[ExchangeRateResponse])
def get_exchange_rates(db: Session = Depends(get_db)):
    repo = ExchangeRateRepository(db)
    service = ExchangeRateService(repo)
    return service.list_rates()
