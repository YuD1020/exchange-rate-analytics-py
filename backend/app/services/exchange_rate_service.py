from app.repositories.exchange_rate_repository import ExchangeRateRepository


class ExchangeRateService:
    def __init__(self, repo: ExchangeRateRepository):
        self.repo = repo

    def list_rates(self):
        return self.repo.get_all_by_list()
