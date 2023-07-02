from flask import render_template
from app.tasks.weather import bp


@bp.route('/')
def index():
    return render_template('weather/index.html')


@bp.route('/beach/')
def categories():
    return render_template('weather/beach.html')
