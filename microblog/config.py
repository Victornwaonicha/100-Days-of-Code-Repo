import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Flask-SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
