def test_monthly_averages(client):
    res = client.get("/api/v1/analytics/monthly-averages")
    data = res.json()

    assert res.status_code == 200
    assert isinstance(data, list)
    assert len(data) >= 3


def test_forecast_matrix(client):
    res = client.get("/api/v1/analytics/forecast-matrix")
    matrix = res.json()["matrix"]

    assert isinstance(matrix, list)
    assert len(matrix) > 0
    assert all(len(row) == 3 for row in matrix)


def test_difference_matrix(client):
    res = client.get("/api/v1/analytics/difference-matrix")
    matrix = res.json()["matrix"]

    assert isinstance(matrix, list)
    assert len(matrix) > 1


def test_product_matrix(client):
    res = client.get("/api/v1/analytics/product-matrix")
    matrix = res.json()["matrix"]

    assert isinstance(matrix, list)
    assert len(matrix) > 0
