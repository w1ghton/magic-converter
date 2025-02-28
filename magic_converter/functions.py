import requests


def get_currencies_list(data):
    currencies = data["Valute"]
    exchange_rate = []

    for currency in currencies:
        exchange_rate.append(
            {
                "code": currency,
                "value": data["Valute"][currency]["Value"],
                "name": data["Valute"][currency]["Name"],
            }
        )
    return exchange_rate
