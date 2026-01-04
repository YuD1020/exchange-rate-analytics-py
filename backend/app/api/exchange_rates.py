from fastapi import APIRouter

router = APIRouter(prefix="/exchange-rates", tags=["exchange-rates"])

@router.get("/")
def list_exchange_rates():
    return {
        "base": "USD",
        "rates": {
            "ILS": 3.7,
            "EUR": 0.92
        }
    }
