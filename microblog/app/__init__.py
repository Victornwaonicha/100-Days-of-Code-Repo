from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bot_1 = Flask(__name__)

#  Flask configuration
bot_1.config.from_object(Config)
db = SQLAlchemy(bot_1)
migrate = Migrate(bot_1, db)

from app import routes, models