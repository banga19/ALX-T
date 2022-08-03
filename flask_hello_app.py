from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# setting up config variable that
# enables flask-sqlalchemy to connect to postgresql database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://banga:banga123@localhost:5432/example"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # when condition is false, deprication error will not pop up

# setting up db connection
db = SQLAlchemy(app)


####---models
# creating the table using classes syntax method in python
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False) 

    ## adding code below is helpfull in debugging python script when 
    # running it in the python interactive shell

    # Has ability to customize printable strings
    def __repr__(self):
        return f'<Person ID: {self.id},  name: {self.name}>'



# code below will create DB tables if theyt dont exist
db.create_all()

# setting up view to homepage
@app.route('/')
def index():
    person1 = Person.query.first()
    return f'Hello ' + person1.name

#This code goes at the bottom of your flask Python file(this is actually your server)
#if __name__ == '__main__':
#    app.debug = True
#    app.run(host='0.0.0.0', port=4000)