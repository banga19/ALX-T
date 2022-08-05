## this is the test file for learning tasks on flask migrations

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

## setting up the DATABASE SERVER connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://banga:banga123@localhost:5432/todoapp'
db = SQLAlchemy(app)

## below is the migrations section that is an instance of the Migrate Class 
# It connects both our app and db 

migrate = Migrate(app, db) 

class Todo(db.Model):
    id = db.column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'< Todo {self.id}, {self.description}>'

db.create_all()


# FLASK-SETUP This code should be at the bottom of all your files.
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
