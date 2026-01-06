def difference_matrix(actual: list[float], forecast: list[float]) -> list[float]:
    return [round(a - f, 4) for a, f in zip(actual, forecast)]


def multiply_matrices(a: list[float], b: list[float]) -> list[float]:
    return [round(x * y, 4) for x, y in zip(a, b)]
