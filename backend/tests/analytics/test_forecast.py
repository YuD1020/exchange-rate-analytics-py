from app.analytics.forecast import forecast_next


def test_forecast():
    assert forecast_next([3.5, 3.6, 3.7]) == 3.6
