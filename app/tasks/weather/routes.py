from flask import render_template
from app.tasks.weather import bp


@bp.route('/')
def index():
    return render_template('weather/index.html')
