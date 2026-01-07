from app.analytics.averages import monthly_averages
from app.analytics.forecast import forecast_next
from app.analytics.matrices import difference_matrix, multiply_matrices
from app.models.monthly_average import MonthlyAverage


class AnalyticsService:
    def __init__(self, rows: list[MonthlyAverage]):
        self.values = [r.average_rate for r in rows]

    def forecast(self) -> float | None:
        if len(self.values) < 3:
            return None
        return forecast_next(self.values)

    def matrices(self) -> dict:
        if len(self.values) < 4:
            return {"difference": [], "product": []}

        forecast_series = [
            sum(self.values[i - 3 : i]) / 3
            for i in range(3, len(self.values) + 1)
        ]

        actual = self.values[3:]
        diff = difference_matrix(actual, forecast_series)
        product = multiply_matrices(actual, diff)

        return {
            "difference": diff,
            "product": product,
        }
