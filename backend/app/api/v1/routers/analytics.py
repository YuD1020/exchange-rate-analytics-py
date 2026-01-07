from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.monthly_average_repository import MonthlyAverageRepository
from app.analytics.service import AnalyticsService

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/monthly-averages")
def monthly_averages(
    sort_by: str | None = Query(None),
    order: str = Query("asc"),
    db: Session = Depends(get_db),
):
    repo = MonthlyAverageRepository(db)
    rows = repo.list(sort_by=sort_by, order=order)
    return [
        {"month": r.month, "average_rate": r.average_rate}
        for r in rows
    ]


@router.get("/forecast")
def forecast(db: Session = Depends(get_db)):
    rows = MonthlyAverageRepository(db).list(sort_by="month")
    service = AnalyticsService(rows)
    return {"forecast_next_month": service.forecast()}


@router.get("/matrices")
def matrices(db: Session = Depends(get_db)):
    rows = MonthlyAverageRepository(db).list(sort_by="month")
    service = AnalyticsService(rows)
    return service.matrices()
