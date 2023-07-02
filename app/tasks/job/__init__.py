from flask import Blueprint

bp = Blueprint('job', __name__)

from app.tasks.job import routes
