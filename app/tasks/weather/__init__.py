from flask import Blueprint

bp = Blueprint('weather', __name__)

from app.tasks.weather import routes
