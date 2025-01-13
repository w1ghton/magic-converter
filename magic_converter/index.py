import requests

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

bp = Blueprint("index", __name__, url_prefix="/")


@bp.get("/")
def index_get():
    return render_template("index/index.html", title="Index")


@bp.post("/")
def index_post():
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    exchange_rate = data["Valute"]["GBP"]["Value"]
    gbp = (
        int(request.form.get("galleons", 0)) * 4.93
        + int(request.form.get("sickles", 0)) * 0.29
        + int(request.form.get("knuts", 0)) * 0.01
    )
    rub = round(gbp * exchange_rate, 1)
    return render_template("index/index.html", title="Index", rub=rub)
