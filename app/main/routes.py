from flask import render_template
from app.main import bp


# Imports the bp blueprint object from the main blueprint
@bp.route('/')
def index():
    return render_template("index.html")
