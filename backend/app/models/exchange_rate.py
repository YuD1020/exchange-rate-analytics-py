from sqlalchemy import Column, Integer, String, Float, Date

from app.core.database import Base


class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String, index=True)
    rate = Column(Float)
    date = Column(Date)
