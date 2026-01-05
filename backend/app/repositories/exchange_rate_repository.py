from sqlalchemy.orm import Session

from app.models.exchange_rate import ExchangeRate

class ExchangeRateRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(ExchangeRate).all()
