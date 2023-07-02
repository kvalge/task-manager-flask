from flask import Blueprint

bp = Blueprint('studies', __name__)

from app.tasks.studies import routes
