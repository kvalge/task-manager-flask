from flask import render_template
from app.tasks.job import bp


@bp.route('/')
def index():
    return render_template('job/index.html')


@bp.route('/javaintern/')
def categories():
    return render_template('job/javaintern.html')
