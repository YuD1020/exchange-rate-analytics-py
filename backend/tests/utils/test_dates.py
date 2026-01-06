from datetime import date as Date

from app.utils.dates import month_key


def test_month_key_format():
    d = Date(2024, 3, 15)
    assert month_key(d) == "2024-03"


def test_month_key_zero_padding():
    d = Date(2023, 1, 1)
    assert month_key(d) == "2023-01"
