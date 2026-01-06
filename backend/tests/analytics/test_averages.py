from datetime import date

from app.models.exchange_rate import ExchangeRate
from app.analytics.averages import monthly_averages

def test_monthly_average():
    rates = [
        ExchangeRate(rate=3.5, date=date(2023, 1, 1)),
        ExchangeRate(rate=3.7, date=date(2023, 1, 15)),
    ]

    result = monthly_averages(rates)
    assert result["2023-01"] == 3.6
