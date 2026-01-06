from datetime import date

from app.schemas.exchange_rate import MonthlyAverageRate
from app.services.exchange_rate_calculator import MonthlyAverageCalculator


class FakeClient:
    def fetch(self, start: date, end: date) -> dict[str, float]:
        return {
            "2023-01-01": 3.5,
            "2023-01-02": 3.7,
            "2023-02-01": 3.6,
        }


def test_monthly_average_calculation():
    calculator = MonthlyAverageCalculator(FakeClient())

    result = calculator.calculate(
        start=date(2023, 1, 1),
        end=date(2023, 2, 1),
    )

    assert result == [
        MonthlyAverageRate(month="2023-01", average_rate=3.6),
        MonthlyAverageRate(month="2023-02", average_rate=3.6),
    ]
