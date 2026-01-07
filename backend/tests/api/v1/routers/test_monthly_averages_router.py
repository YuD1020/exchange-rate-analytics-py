def test_get_monthly_averages(client, db):
    from app.models.monthly_average import MonthlyAverage

    db.add(MonthlyAverage(month="2024-01", average_rate=3.7))
    db.commit()

    res = client.get("/api/v1/monthly-averages/")
    assert res.status_code == 200
    assert res.json()[0]["month"] == "2024-01"
