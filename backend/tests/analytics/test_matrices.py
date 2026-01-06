from app.analytics.matrices import difference_matrix, multiply_matrices


def test_difference_matrix():
    assert difference_matrix([4, 5], [3, 4]) == [1, 1]


def test_multiply_matrix():
    assert multiply_matrices([2, 3], [4, 5]) == [8, 15]
