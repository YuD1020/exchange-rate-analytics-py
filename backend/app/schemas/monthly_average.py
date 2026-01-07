from pydantic import BaseModel


class MonthlyAverageResponse(BaseModel):
    month: str
    average_rate: float

    class Config:
        from_attributes = True
