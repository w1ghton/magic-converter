from flask import Blueprint, render_template, request
from .functions import get_currencies_list, get_api_data

GALLEON_RATE = 4.93
SICKLE_RATE = 0.29
KNUT_RATE = 0.01

bp = Blueprint("index", __name__, url_prefix="/")


def get_currencies(data):
    return get_currencies_list(data)


@bp.get("/")
def index_get():
    data = get_api_data()
    if data is None:
        return render_template("error.html")
    currencies = get_currencies(data)
    return render_template(
        "index/index.html", title="Magic Converter", currencies=currencies
    )


@bp.post("/")
def index_post():
    data = get_api_data()
    if data is None:
        return render_template("error.html")
    currencies = get_currencies(data)
    try:
        gbp = (
            int(request.form.get("galleons", 0)) * GALLEON_RATE
            + int(request.form.get("sickles", 0)) * SICKLE_RATE
            + int(request.form.get("knuts", 0)) * KNUT_RATE
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
