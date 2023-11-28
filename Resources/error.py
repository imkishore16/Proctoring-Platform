
from flask import Blueprint, render_template

blp = Blueprint("error", __name__)

@blp.app_errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

@blp.app_errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500
