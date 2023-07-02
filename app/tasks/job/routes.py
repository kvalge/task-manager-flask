from flask import render_template
from app.tasks.job import bp


@bp.route('/')
def index():
    return render_template('job/index.html')


@bp.route('/new/')
def categories():
    return render_template('job/new-job.html')
