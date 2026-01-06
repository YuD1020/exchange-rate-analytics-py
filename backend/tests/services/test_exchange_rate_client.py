from datetime import date

import pytest
import httpx

from app.services.exchange_rate_client import ExchangeRateHostClient


class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise httpx.HTTPStatusError("error", request=None, response=None)

    def json(self):
        return self._json


def test_fetch_success(monkeypatch):
    fake_api_response = {
        "rates": {
            "2024-01-01": {"ILS": 3.8},
            "2024-01-02": {"ILS": 3.82},
        }
    }

    def mock_get(*args, **kwargs):
        return DummyResponse(fake_api_response)

    monkeypatch.setattr(httpx, "get", mock_get)

    client = ExchangeRateHostClient()

    result = client.fetch(
        start=date(2024, 1, 1),
        end=date(2024, 1, 2),
    )

    assert result == {
        "2024-01-01": 3.8,
        "2024-01-02": 3.82,
    }


def test_fetch_http_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return DummyResponse({}, status_code=500)

    monkeypatch.setattr(httpx, "get", mock_get)

    client = ExchangeRateHostClient()

    with pytest.raises(httpx.HTTPStatusError):
        client.fetch(
            start=date(2024, 1, 1),
            end=date(2024, 1, 2),
        )
