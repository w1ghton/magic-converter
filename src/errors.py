from flask import Blueprint, render_template

bp = Blueprint("errors", __name__, url_prefix="/")


@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template("errors/page_not_found.html", title="Not found"), 404


@bp.app_errorhandler(500)
def internal_server_error(error):
    return (
        render_template(
            "errors/internal_server_error.html", title="Internal server error"
        ),
        500,
    )
