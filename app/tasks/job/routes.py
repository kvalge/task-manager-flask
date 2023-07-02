from flask import render_template, request, redirect, url_for

from app import db
from app.models.job import Job
from app.tasks.job import bp


@bp.route('/')
def index():
    return render_template('job/index.html')


@bp.route('/new/', methods=('GET', 'POST'))
def categories():
    if request.method == 'POST':
        new_question = Job(title=request.form['title'],
                           content=request.form['content'])
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('job.index'))
    return render_template('job/new-job.html')
