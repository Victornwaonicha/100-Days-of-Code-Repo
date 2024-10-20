from flask import render_template, flash, redirect, url_for
from app import bot_1
from app.forms import LoginForm
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from urllib.parse import urlsplit

# Home view function
@bot_1.route('/')
@bot_1.route('/index')
@login_required
def index():
    user = {'username': 'Mallo'}
    posts = [
        {
            'author': {'username': 'Vivian'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Nneka'},
            'body': 'I love writting codes!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

# Login view function
@bot_1.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# Logout view function
@bot_1.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
