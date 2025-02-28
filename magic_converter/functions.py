import requests
from typing import Dict, Any, List


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
        }
        for currency in currencies
    ]
    return exchange_rate
