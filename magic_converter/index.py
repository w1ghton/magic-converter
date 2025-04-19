from flask import Blueprint, render_template, request

from .functions import get_api_data, get_currencies_list, get_gbp

bp = Blueprint("index", __name__, url_prefix="/")


@bp.get("/")
def index_get():
    data = get_api_data()
    if data is None:
        return render_template("error.html")
    currencies = get_currencies_list(data)
    return render_template(
        "index/index.html", title="Magic Converter", currencies=currencies
    )


@bp.post("/")
def index_post():
    data = get_api_data()
    if data is None:
        return render_template("error.html")
    currencies = get_currencies_list(data)
    try:
        gbp = get_gbp(
            int(request.form.get("galleons", 0)),
            int(request.form.get("sickles", 0)),
            int(request.form.get("knuts", 0)),
        )
    except ValueError:
        gbp = 0
    rub = data["Valute"]["GBP"]["Value"] * gbp
    country = request.form.get("country")
    if country == "RUB":
        res = rub
        code = country
    else:
        rate, code, nominal = country.split("|")
        exchange_rate = float(rate)
        nominal = float(nominal)
        res = rub * nominal / exchange_rate

    res = f"{round(res, 2):,}".replace(",", " ")
    return render_template(
        "index/index.html",
        title="Magic Converter",
        res=res,
        currencies=currencies,
        code=code,
    )
