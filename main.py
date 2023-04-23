from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite://root:@localhost/bhumart.db'
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno= db.Column(db.Integer, primary_key=True, nullable=False)
    company= db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50),nullable=False)
    crop = db.Column(db.String(50),nullable=False)
    quantity = db.Column(db.Integer(50),nullable=False)
    date_time = db.Column(db.String(20), nullable=False)
    
    
@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/login")
def login():
      return render_template('login.html')


@app.route("/signup")
def signup():
      return render_template('signup.html')



if __name__ == "__main__":
    app.run(debug=True,port=8001)


