from app.models.monthly_average import MonthlyAverage


def seed_monthly_averages(db):
    db.add_all(
        [
            MonthlyAverage(month="2023-01", average=3.45),
            MonthlyAverage(month="2023-02", average=3.52),
            MonthlyAverage(month="2023-03", average=3.60),
            MonthlyAverage(month="2023-04", average=3.58),
            MonthlyAverage(month="2023-05", average=3.62),
            MonthlyAverage(month="2023-06", average=3.67),
        ]
    )
    db.commit()
