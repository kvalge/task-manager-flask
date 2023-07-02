from flask import Blueprint

bp = Blueprint('entertainment', __name__)

from app.tasks.entertainment import routes
