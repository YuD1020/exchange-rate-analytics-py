from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.exchange_rate_repository import ExchangeRateRepository
from app.analytics.averages import monthly_averages
from app.analytics.matrices import difference_matrix, multiply_matrices
from app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/monthly-averages")
def get_monthly_averages(db: Session = Depends(get_db)):
    rates = ExchangeRateRepository(db).get_all_by_list()
    return monthly_averages(rates)


@router.get("/forecast")
def forecast(db: Session = Depends(get_db)):
    rates = monthly_averages(
        ExchangeRateRepository(db).get_all_by_list()
    )

    forecast_value = AnalyticsService(rates).forecast_next_month()

    return {
        "forecast_next_month": forecast_value
    }


@router.get("/matrices")
def matrices(db: Session = Depends(get_db)):
    rates = ExchangeRateRepository(db).get_all_by_list()
    averages = list(monthly_averages(rates).values())

    if len(averages) < 3:
        return {
            "difference": [],
            "product": []
        }

    forecast = [
        sum(averages[i-3:i]) / 3
        for i in range(3, len(averages) + 1)
    ]

    actual = averages[3:]

    diff = difference_matrix(actual, forecast)
    product = multiply_matrices(actual, diff)

    return {
        "difference": diff,
        "product": product
    }
