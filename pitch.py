from datetime import datetime
from flask import Flask, render_template, url_for, flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = '023cb1594e4c4ad9ae26d719b65b472f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(20),unique=True,nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False) 
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__ (self):
        return f"User('{self.username}', '{self.email},{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False) 
    date_posted = db.Column (db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post ('{self.title}', '{self.date_posted},{self.image_file}')"
      



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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'paulwamaria@gmail.com' and form.password.data=='pass':
            flash('You have been logged in!', 'Success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.Please check Username and password', 'danger')
    return render_template('login.html', title='Login', form=form )


if __name__ == '__main__':
    app.run(debug=True)