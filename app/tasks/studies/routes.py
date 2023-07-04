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


@bp.route('/edit/<id>', methods=['GET', 'POST'])
def get_program_by_id_for_edit(id):
    program = Program.query.filter_by(id=id).first()
    return render_template('studies/edit-program.html', program=program)


@bp.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    program = Program.query.filter_by(id=id).first()
    program.title = request.form["title"]
    program.organization = request.form["organization"]
    program.description = request.form["description"]
    db.session.commit()
    return index()


@bp.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    program = Program.query.filter_by(id=id).first()
    db.session.delete(program)
    db.session.commit()
    return index()
