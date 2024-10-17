from flask import render_template, flash, redirect, url_for
from app import bot_1
from app.forms import LoginForm

# Home view function
@bot_1.route('/')
@bot_1.route('/index')
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)