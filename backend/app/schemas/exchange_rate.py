from datetime import date
from pydantic import BaseModel, ConfigDict


class ExchangeRateBase(BaseModel):
    currency: str
    rate: float
    date: date


class ExchangeRateResponse(ExchangeRateBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
