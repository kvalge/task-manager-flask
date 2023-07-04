from flask import render_template, request, redirect, url_for

from app import db
from app.models.job import Job
from app.tasks.job import bp


@bp.route('/')
def index():
    jobs = Job.query.all()
    return render_template('job/index.html', jobs=jobs)


@bp.route('/new/', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        new_question = Job(title=request.form['title'],
                           content=request.form['content'])
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('job.index'))
    return render_template('job/new-job.html')


@bp.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    job = Job.query.filter_by(id=id).first()
    db.session.delete(job)
    db.session.commit()
    return index()
