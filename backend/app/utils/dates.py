from datetime import date
import calendar


def month_range(year: int, month: int) -> tuple[date, date]:
    start = date(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    end = date(year, month, last_day)

    return start, end


def month_key(d: date) -> str:
    return f"{d.year:04d}-{d.month:02d}"
