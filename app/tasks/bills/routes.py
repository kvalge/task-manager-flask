from flask import render_template
from app.tasks.bills import bp


@bp.route('/')
def index():
    return render_template('bills/index.html')


@bp.route('/mobile/')
def categories():
    return render_template('bills/mobile.html')
