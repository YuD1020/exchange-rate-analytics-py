from datetime import date

from app.core.database import SessionLocal, engine, Base
from app.models.exchange_rate import ExchangeRate

Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()

    if db.query(ExchangeRate).count() == 0:
        db.add_all([
            ExchangeRate(currency="USD", rate=3.75, date=date.today()),
            ExchangeRate(currency="EUR", rate=4.05, date=date.today()),
        ])
        db.commit()

    db.close()

if __name__ == "__main__":
    seed()
