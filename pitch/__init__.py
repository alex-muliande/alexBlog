from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config['SECRET_KEY'] = '023cb1594e4c4ad9ae26d719b65b472f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from pitch import routes