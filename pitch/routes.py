from flask import render_template, url_for, flash, redirect,request
from pitch import app, db, bcrypt
from pitch.forms import RegistrationForm, LoginForm
from pitch.models import User, Post
from flask_login import login_user, current_user, logout_user,login_required


posts = [
    {
        'author': 'Alex Muliande',
        'title': 'Lamination',
        'content': 'First content post',
        'date_posted': 'September 15, 2018',
    },
    {
        'author': 'Mercy Pinky',
        'title': 'Lamination 2',
        'content': 'Second content post',
        'date_posted': 'September 18, 2019',

    }
]

# @app.route('/')
@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.Please check email and password', 'danger')            
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
    