from flask import render_template, request, redirect, url_for

from app import db
from app.models.study_program import Program
from app.tasks.studies import bp


@bp.route('/')
def index():
    programs = Program.query.all()
    return render_template('studies/index.html', programs=programs)


@bp.route('/new/', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        new_program = Program(title=request.form['title'],
                              organization=request.form['organization'],
                              description=request.form['description'])
        db.session.add(new_program)
        db.session.commit()
        return redirect(url_for('studies.index'))
    return render_template('studies/new_program.html')


@bp.route('/university/')
def categories():
    return render_template('studies/university.html')
