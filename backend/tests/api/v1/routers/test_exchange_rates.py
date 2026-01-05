def test_get_exchange_rates(client):
    response = client.get("/api/v1/exchange-rates/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
