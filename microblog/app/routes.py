from flask import render_template, flash, redirect, url_for
from datetime import datetime, timezone
from app.forms import LoginForm
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import bot_1, db
from app.forms import RegistrationForm
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from urllib.parse import urlsplit
from app.forms import EditProfileForm, EmptyForm



# Edit profile view function
@bot_1.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

# Record time of last visit
@bot_1.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()

# Home view function
@bot_1.route('/')
@bot_1.route('/index')
@login_required
def index():
    # user = {'username': 'Mallo'}
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
    return render_template('index.html', title='Home', posts=posts)

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
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    
    # If it's a GET request or the form is not valid, render the login template
    return render_template('login.html', title='Sign In', form=form)

# Logout view function
@bot_1.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# User registration view function
@bot_1.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# User profile view function
@bot_1.route('/user/<username>')
@login_required
def user(username):
    # Query to find the user or return 404 if not found
    user = db.session.scalar(sa.select(User).where(User.username == username))
    
    if user is None:
        # Return a 404 error if the user is not found
        return render_template('404.html'), 404  # You can create a custom 404 template

    # Example posts
    posts = [
        {'author': user, 'body': 'Always Python #1'},
        {'author': user, 'body': 'Alright, now go! #2'}
    ]

    # Render the user profile template
    # return render_template('user.html', user=user, posts=posts)

    # Follow and unfollow routes.
    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts, form=form)


@bot_1.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == username))
        if user is None:
            flash(f'User {username} not found.')
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash(f'You are following {username}!')
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))


@bot_1.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == username))
        if user is None:
            flash(f'User {username} not found.')
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash(f'You are not following {username}.')
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))
