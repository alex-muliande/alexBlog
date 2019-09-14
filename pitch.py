from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)