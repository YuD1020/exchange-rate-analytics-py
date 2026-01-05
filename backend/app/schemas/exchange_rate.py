from datetime import date
from pydantic import BaseModel

class ExchangeRateBase(BaseModel):
    currency: str
    rate: float
    date: date

class ExchangeRateResponse(ExchangeRateBase):
    id: int

    class Config:
        from_attributes = True
