from app.analytics.matrix import forecast_matrix, difference_matrix


def test_forecast_matrix_size():
    values = [1.0, 2.0, 3.0, 4.0]
    matrix = forecast_matrix(values)
    assert len(matrix) == 2


def test_difference_matrix_values():
    actual = [1.0, 2.0, 3.0, 4.0]
    forecast = [[2.0], [3.0]]
    diff = difference_matrix(actual, forecast)
    assert diff[0][0] == 1.0
