from app import bot_1
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import bot_1, db
from app.models import User, Post

@bot_1.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    bot_1.run(debug=True)