from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '023cb1594e4c4ad9ae26d719b65b472f'


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

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
     return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = RegistrationForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)