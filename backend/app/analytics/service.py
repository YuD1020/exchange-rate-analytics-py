from app.analytics.matrix import (
    forecast_matrix,
    difference_matrix,
    average_difference_row,
    multiply_matrices,
)
from app.services.monthly_average_service import MonthlyAverageService
from app.core.database import SessionLocal


def _get_monthly_values():
    db = SessionLocal()
    try:
        service = MonthlyAverageService(db)
        return [item.average for item in service.list_all()]
    finally:
        db.close()


def forecast_next_month():
    values = _get_monthly_values()
    return sum(values[-3:]) / 3


def get_forecast_matrix():
    return forecast_matrix(_get_monthly_values())


def get_difference_matrix():
    values = _get_monthly_values()
    forecast = forecast_matrix(values)
    diff = difference_matrix(values, forecast)
    return average_difference_row(diff)


def get_product_matrix():
    forecast = get_forecast_matrix()
    diff = get_difference_matrix()

    if not forecast or not diff:
        return []

    return multiply_matrices(forecast, diff[:-1])

