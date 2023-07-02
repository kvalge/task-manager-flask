import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = "postgresql://postgres:postgres@host:port/tasks"


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
