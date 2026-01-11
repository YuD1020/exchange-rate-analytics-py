from pydantic import BaseModel
from typing import List


class MonthlyAverage(BaseModel):
    month: str
    average: float


class ForecastResult(BaseModel):
    month: str
    forecast: float


class MatrixResponse(BaseModel):
    matrix: List[List[float]]
