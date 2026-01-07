from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.monthly_average import MonthlyAverage


class MonthlyAverageRepository:
    def __init__(self, db: Session):
        self.db = db

    def upsert(self, month: str, value: float) -> MonthlyAverage:
        obj = self.db.scalar(
            select(MonthlyAverage).where(MonthlyAverage.month == month)
        )

        if obj:
            obj.average_rate = value
        else:
            obj = MonthlyAverage(month=month, average_rate=value)
            self.db.add(obj)

        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(
        self,
        sort_by: str | None = None,
        order: str = "asc",
    ) -> list[MonthlyAverage]:
        stmt = select(MonthlyAverage)

        if sort_by in {"month", "average_rate"}:
            col = getattr(MonthlyAverage, sort_by)
            stmt = stmt.order_by(col.asc() if order == "asc" else col.desc())

        return list(self.db.scalars(stmt))

    def get_by_month(self, month: str) -> MonthlyAverage | None:
        return self.db.scalar(
            select(MonthlyAverage).where(MonthlyAverage.month == month)
        )
