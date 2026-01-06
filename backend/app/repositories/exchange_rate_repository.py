from sqlalchemy.orm import Session

from app.models.exchange_rate import ExchangeRate


class ExchangeRateRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, *, currency: str | None = None, order_by_rate: bool = False):
        q = self.db.query(ExchangeRate)

        if currency:
            q = q.filter(ExchangeRate.currency == currency)

        if order_by_rate:
            q = q.order_by(ExchangeRate.rate.asc())
        else:
            q = q.order_by(ExchangeRate.date.asc())

        return q.all()

    def get_all_by_list(self) -> list[ExchangeRate]:
        return self.db.query(ExchangeRate).order_by(ExchangeRate.id.asc()).all()
