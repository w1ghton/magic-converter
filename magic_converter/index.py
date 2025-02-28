import requests
from flask import Blueprint, render_template, request
from .functions import get_currencies_list

bp = Blueprint("index", __name__, url_prefix="/")

@bp.get("/")
def index_get():
    currencies = get_currencies_list()
    return render_template("index/index.html", title="Magic Converter", currencies=currencies)

@bp.post("/")
def index_post():
    try:
        gbp = (
            int(request.form.get("galleons", 0)) * 4.93
            + int(request.form.get("sickles", 0)) * 0.29
            + int(request.form.get("knuts", 0)) * 0.01
        )
    except ValueError:
        gbp = 0
    exchange_rate = request.form.get("country")
    print(exchange_rate)
    # rub = f"{round(gbp * exchange_rate):,}".replace(",", " ")
    return render_template("index/index.html", title="Magic Converter")