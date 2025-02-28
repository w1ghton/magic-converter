import requests
from flask import Blueprint, render_template, request
from .functions import get_currencies_list

currencies = get_currencies_list()
# print(currencies[0]['name'])


bp = Blueprint("index", __name__, url_prefix="/")


@bp.get("/")
def index_get():
    return render_template("index/index.html", title="Magic Converter")


@bp.post("/")
def index_post(currencies_list=currencies):
    # data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    # exchange_rate = data["Valute"]["GBP"]["Value"]
    # try:
    #     gbp = (
    #         int(request.form.get("galleons", 0)) * 4.93
    #         + int(request.form.get("sickles", 0)) * 0.29
    #         + int(request.form.get("knuts", 0)) * 0.01
    #     )
    # except ValueError:
    #     gbp = 0
    # rub = f"{round(gbp * exchange_rate):,}".replace(",", " ")
    # currencies = get_currencies_list()
    
    return render_template("index/index.html", title="Magic Converter", currencies=currencies_list)
