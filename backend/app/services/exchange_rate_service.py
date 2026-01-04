from app.repositories.exchange_rate_repository import ExchangeRateRepository


class ExchangeRateService:
    def __init__(self, repo: ExchangeRateRepository):
        self.repo = repo

    def get_exchange_rates(self) -> dict:
        return self.repo.get_latest_rates()
