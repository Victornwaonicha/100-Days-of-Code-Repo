from flask import request
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel



def get_locale():
    return request.accept_languages.best_match(bot_1.config['LANGUAGES'])


# Being an innstance variable of Flask makes bot_1 a member of the app package.
bot_1 = Flask(__name__)

# Initialize Flask-Babel.
babel = Babel(bot_1, locale_selector=get_locale)

# Flask-Mail instance.
mail = Mail(bot_1)

# Flask-Moment instance
moment = Moment(bot_1)

# Flask-Login initialization
login = LoginManager(bot_1)
login.login_view = 'login'

#  Flask configuration
bot_1.config.from_object(Config)
db = SQLAlchemy(bot_1)
migrate = Migrate(bot_1, db)

if not bot_1.debug:
    if bot_1.config['MAIL_SERVER']:
        auth = None
        if bot_1.config['MAIL_USERNAME'] or bot_1.config['MAIL_PASSWORD']:
            auth = (bot_1.config['MAIL_USERNAME'], bot_1.config['MAIL_PASSWORD'])
        secure = None
        if bot_1.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(bot_1.config['MAIL_SERVER'], bot_1.config['MAIL_PORT']),
            fromaddr='no-reply@' + bot_1.config['MAIL_SERVER'],
            toaddrs=bot_1.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        bot_1.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    bot_1.logger.addHandler(file_handler)

    bot_1.logger.setLevel(logging.INFO)
    bot_1.logger.info('Microblog startup')   

# Import error handlers
from app import routes, models, errors



# nitialize Flask-Babel.