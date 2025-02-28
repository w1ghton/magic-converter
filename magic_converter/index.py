import requests
from flask import Blueprint, render_template, request
from .functions import get_currencies_list

bp = Blueprint("index", __name__, url_prefix="/")


@bp.get("/")
def index_get():
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    currencies = get_currencies_list(data)
    return render_template(
        "index/index.html", title="Magic Converter", currencies=currencies
    )


@bp.post("/")
def index_post():
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    currencies = get_currencies_list(data)
    try:
        gbp = (
            int(request.form.get("galleons", 0)) * 4.93
            + int(request.form.get("sickles", 0)) * 0.29
            + int(request.form.get("knuts", 0)) * 0.01
        )
    except ValueError:
        gbp = 0

    rub = data["Valute"]["GBP"]["Value"] * gbp

    country = request.form.get("country")

    if country == "RUB":
        res = rub
        code = country
    else:
        rate, code = country.split("|")
        exchange_rate = float(rate)
        res = rub / exchange_rate

    return render_template(
        "index/index.html",
        title="Magic Converter",
        res=round(res, 2),
        currencies=currencies,
        code=code,
    )
