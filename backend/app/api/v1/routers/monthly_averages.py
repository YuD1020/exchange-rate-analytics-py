from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.monthly_average import MonthlyAverageResponse
from app.services.monthly_average_service import MonthlyAverageService

router = APIRouter(
    prefix="/monthly-averages",
    tags=["Monthly Averages"],
)


@router.get("/", response_model=list[MonthlyAverageResponse])
def get_monthly_averages(db: Session = Depends(get_db)):
    service = MonthlyAverageService(db)
    return service.list_all()
