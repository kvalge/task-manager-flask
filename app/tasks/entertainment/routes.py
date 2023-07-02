from flask import render_template
from app.tasks.entertainment import bp


@bp.route('/')
def index():
    return render_template('entertainment/index.html')


@bp.route('/cinema/')
def categories():
    return render_template('entertainment/cinema.html')
