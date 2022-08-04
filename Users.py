from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up th db connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://banga:banga123@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## models section 
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    ## enables debuging on python3 interactive shell
    def __repr__(self):
        return f'<User id: {self.id}, Name: {self.name}>'

db.create_all()
