from app.analytics.averages import monthly_averages
from app.analytics.forecast import forecast_next
from app.analytics.matrices import difference_matrix, multiply_matrices

class AnalyticsService:
    def __init__(self, rates):
        self.rates = rates

    def monthly_averages(self):
        return monthly_averages(self.rates)

    def forecast_next_month(self):
        averages = list(self.rates.values())
        if len(averages) < 3:
            return None
        return forecast_next(averages)

    def matrices(self):
        averages = list(self.monthly_averages().values())
        forecast = [
            forecast_next(averages[:i+3])
            for i in range(len(averages)-2)
        ]

        actual = averages[2:]
        diff = difference_matrix(actual, forecast)
        product = multiply_matrices(actual, diff)

        return {
            "forecast": forecast,
            "difference": diff,
            "product": product,
        }
        