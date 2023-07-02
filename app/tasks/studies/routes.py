from flask import render_template
from app.tasks.studies import bp


@bp.route('/')
def index():
    return render_template('studies/index.html')


@bp.route('/university/')
def categories():
    return render_template('studies/university.html')
