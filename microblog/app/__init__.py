from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Being an innstance variable of Flask makes bot_1 a member of the app package.
bot_1 = Flask(__name__)

# Flask-Login initialization
login = LoginManager(bot_1)
login.login_view = 'login'

#  Flask configuration
bot_1.config.from_object(Config)
db = SQLAlchemy(bot_1)
migrate = Migrate(bot_1, db)

from app import routes, models