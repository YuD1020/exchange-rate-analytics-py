from sqlalchemy.orm import Session

from app.models.monthly_average import MonthlyAverage


class MonthlyAverageService:
    def __init__(self, db: Session):
        self.db = db

    def save(self, month: str, average_rate: float) -> None:
        exists = (
            self.db.query(MonthlyAverage).filter(MonthlyAverage.month == month).first()
        )
        if exists:
            return

        self.db.add(
            MonthlyAverage(
                month=month,
                average_rate=average_rate,
            )
        )
        self.db.commit()

    def list_all(self) -> list[MonthlyAverage]:
        return self.db.query(MonthlyAverage).order_by(MonthlyAverage.month).all()
