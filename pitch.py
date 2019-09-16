from flask import Flask, render_template, url_for, flash,redirect
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