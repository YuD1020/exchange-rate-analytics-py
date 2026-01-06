def forecast_next(values: list[float]) -> float:
    if len(values) < 3:
        raise ValueError("Need at least 3 months for forecast")

    last_three = values[-3:]
    return round(sum(last_three) / 3, 4)
