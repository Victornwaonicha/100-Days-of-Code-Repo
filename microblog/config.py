import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Flask-SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')


    # Email configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['malloyoung78@gmail.com']

    # Posts per page configuration.
    POSTS_PER_PAGE = 3

    # Supported languages list.
    LANGUAGES = ['en', 'es']

