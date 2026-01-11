from fastapi import APIRouter
from app.analytics.service import (
    forecast_next_month,
    get_forecast_matrix,
    get_difference_matrix,
    get_product_matrix,
)
from app.schemas.monthly_average import MonthlyAverageResponse
from app.services.monthly_average_service import MonthlyAverageService
from app.core.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/monthly-averages", response_model=list[MonthlyAverageResponse])
def monthly_averages(db: Session = Depends(get_db)):
    service = MonthlyAverageService(db)
    return service.list_all()


@router.get("/forecast-next")
def forecast_next():
    return {"forecast": forecast_next_month()}


@router.get("/forecast-matrix")
def forecast_matrix():
    return {"matrix": get_forecast_matrix()}


@router.get("/difference-matrix")
def difference_matrix():
    return {"matrix": get_difference_matrix()}


@router.get("/product-matrix")
def product_matrix():
    return {"matrix": get_product_matrix()}
