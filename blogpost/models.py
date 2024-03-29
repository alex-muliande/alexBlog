from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from blogpost import db, login_manager,app 
from flask_login import UserMixin
from . import db

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(55),unique=True,nullable=False)
    email = db.Column(db.String(5555),unique=True,nullable=False)
    image_file = db.Column(db.String(5555), nullable=False, default='https://images.pexels.com/photos/257840/pexels-photo-257840.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
    password = db.Column(db.String(60), nullable=False) 
    posts = db.relationship('Post', backref='author', lazy=True)
    comment = db.relationship('Comment',backref = 'author',lazy=True)


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def __repr__ (self):
        return f"User('{self.username}', '{self.email},{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False) 
    date_posted = db.Column (db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    

    def __repr__(self):
        return f"Post ('{self.title}', '{self.date_posted}')"
      
# Comments section Class

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Comment ('{self.content}')"
      
class Quote():
   def __init__(self, author,quoteMsg):
       self.author = author
       self.quoteMsg = quoteMsg