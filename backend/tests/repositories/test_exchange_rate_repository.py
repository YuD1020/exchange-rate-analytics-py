from app.models.exchange_rate import ExchangeRate
from app.repositories.exchange_rate_repository import ExchangeRateRepository

def test_list_exchange_rates(db):
    repo = ExchangeRateRepository(db)

    db.add(ExchangeRate(currency="USD", rate=3.7))
    db.commit()

    rates = repo.get_all_by_list()
    assert len(rates) == 1
    assert rates[0].currency == "USD"
