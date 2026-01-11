from typing import List


def forecast_matrix(values: List[float]) -> List[List[float]]:
    matrix = []
    for i in range(len(values) - 2):
        avg = sum(values[i:i + 3]) / 3
        matrix.append([avg])
    return matrix


def difference_matrix(actual: List[float], forecast: List[List[float]]) -> List[List[float]]:
    diff = []
    for i, row in enumerate(forecast):
        diff.append([actual[i + 2] - row[0]])
    return diff


def average_difference_row(diff):
    if not diff:
        return []

    total = sum(row[0] for row in diff) / len(diff)
    return diff + [[total]]



def multiply_matrices(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    result = []
    for i in range(len(a)):
        result.append([a[i][0] * b[i][0]])
    return result
