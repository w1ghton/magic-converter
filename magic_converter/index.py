import requests
from flask import Blueprint, render_template, request

bp = Blueprint("index", __name__, url_prefix="/")


@bp.get("/")
def index_get():
    return render_template("index/index.html", title="Magic Converter")


@bp.post("/")
def index_post():
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    exchange_rate = data["Valute"]["GBP"]["Value"]
    gbp = (
        int(request.form.get("galleons", 0)) * 4.93
        + int(request.form.get("sickles", 0)) * 0.29
        + int(request.form.get("knuts", 0)) * 0.01
    )
    rub = f"{round(gbp * exchange_rate):,}".replace(",", " ")
    return render_template("index/index.html", title="Magic Converter", rub=rub)
