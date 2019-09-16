from flask import render_template, url_for, flash,redirect
from pitch import app, db, bcrypt 
from pitch.forms import RegistrationForm, LoginForm
from pitch.models import User, Post


posts = [
    {
        'author':'Alex Muliande',
        'title':'Lamination',
        'content':'First content post',
        'date_posted':'September 15, 2018',
    },
    {
        'author':'Mercy Pinky',
        'title':'Lamination 2',
        'content':'Second content post',
        'date_posted':'September 18, 2019',

    }
]

# @app.route('/') 
@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
     return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username =form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'alex@gmail.com' and form.password.data=='pass':
            flash('You have been logged in!', 'Success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.Please check Username and password', 'danger')
    return render_template('login.html', title='Login', form=form )
