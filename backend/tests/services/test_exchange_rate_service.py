from app.models.exchange_rate import ExchangeRate
from app.repositories.exchange_rate_repository import ExchangeRateRepository
from app.services.exchange_rate_service import ExchangeRateService


def test_service_returns_rates(db):
    db.add(ExchangeRate(currency="EUR", rate=4.1))
    db.commit()

    repo = ExchangeRateRepository(db)
    service = ExchangeRateService(repo)

    rates = service.list_rates()
    assert rates[0].currency == "EUR"
