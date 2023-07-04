from flask import render_template, request, redirect, url_for

from app import db
from app.models.bill import Bill
from app.tasks.bills import bp


@bp.route('/')
def index():
    bills = Bill.query.all()
    return render_template('bills/index.html', bills=bills)


@bp.route('/new/', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        new_bill = Bill(service=request.form['service'],
                        period=request.form['period'],
                        price=request.form['price'])
        db.session.add(new_bill)
        db.session.commit()
        return redirect(url_for('bills.index'))
    return render_template('bills/new-bill.html')


@bp.route('/edit/<id>', methods=['GET', 'POST'])
def get_bill_by_id_for_edit(id):
    bill = Bill.query.filter_by(id=id).first()
    return render_template('bills/edit-bill.html', bill=bill)


@bp.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    bill = Bill.query.filter_by(id=id).first()
    bill.service = request.form["service"]
    bill.period = request.form["period"]
    bill.price = request.form["price"]
    db.session.commit()
    return index()


@bp.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    bill = Bill.query.filter_by(id=id).first()
    db.session.delete(bill)
    db.session.commit()
    return index()
