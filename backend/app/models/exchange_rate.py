from sqlalchemy import Column, Integer, String, Float

from app.core.database import Base

class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True, index=True)
    base_currency = Column(String, index=True)
    target_currency = Column(String, index=True)
    rate = Column(Float)
