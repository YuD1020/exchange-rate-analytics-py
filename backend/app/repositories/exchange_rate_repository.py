from datetime import date

class ExchangeRateRepository:
    def get_latest_rates(self) -> dict:
        return {
            "base": "USD",
            "date": date.today().isoformat(),
            "rates": {
                "ILS": 3.72,
                "EUR": 0.91,
                "GBP": 0.78,
            },
        }
