from typing import Any, Dict, List

import requests
from pydantic import Field


def get_api_data() -> Dict[str, Any]:
    try:
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(e)
        return None


def get_currencies_list(api_response: Dict[str, Any]) -> List[Dict[str, Any]]:
    currencies = api_response.get("Valute", {})
    exchange_rate = [
        {
            "code": currency,
            "value": currencies.get(currency, {}).get("Value", ""),
            "name": currencies.get(currency, {}).get("Name", ""),
            "nominal": currencies.get(currency, {}).get("Nominal", ""),
        }
        for currency in currencies
    ]
    return exchange_rate


def get_gbp(
    galleons: int = Field(ge=0), sickles: int = Field(ge=0), knuts: int = Field(ge=0)
) -> float:
    GALLEON_RATE = 4.93
    SICKLE_RATE = 0.29
    KNUT_RATE = 0.01
    gbp = galleons * GALLEON_RATE + sickles * SICKLE_RATE + knuts * KNUT_RATE

    return gbp
