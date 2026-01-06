def test_monthly_averages(client):
    res = client.get("/api/v1/analytics/monthly-averages")
    assert res.status_code == 200
    assert isinstance(res.json(), dict)


def test_forecast(client):
    res = client.get("/api/v1/analytics/forecast")
    assert res.status_code == 200
    assert "forecast_next_month" in res.json()


def test_matrices(client):
    res = client.get("/api/v1/analytics/matrices")
    assert res.status_code == 200
    assert "product" in res.json()
