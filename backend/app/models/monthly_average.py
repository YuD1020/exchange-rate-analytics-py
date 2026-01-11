from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base


class MonthlyAverage(Base):
    __tablename__ = "monthly_averages"

    id = Column(Integer, primary_key=True)
    month = Column(String, nullable=False)
    average_rate = Column(Float, nullable=False)
