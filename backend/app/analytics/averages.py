from collections import defaultdict
from app.models.exchange_rate import ExchangeRate

def monthly_averages(rates: list[ExchangeRate]) -> dict[str, float]:
    buckets = defaultdict(list)

    for r in rates:
        key = r.date.strftime("%Y-%m")
        buckets[key].append(r.rate)

    return {
        month: round(sum(values) / len(values), 4)
        for month, values in buckets.items()
    }
