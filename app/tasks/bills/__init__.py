from flask import Blueprint

bp = Blueprint('bills', __name__)

from app.tasks.bills import routes