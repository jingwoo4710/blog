import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 초기 설정
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB 초기설정
db = SQLAlchemy(app)

# Table 정의
class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    address = db.Column(db.String, nullable=False)
    adresss2 = db.Column(db.String)
    country = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip = db.Column(db.String, nullable=False)


    def __repr__(self):
        return "< Name {} --- ID {} >".format(self.lastname, self.username)

# DB init
with app.test_request_context():
    db.create_all()

# `/`
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        address2 = request.form['address2']
        country = request.form['country']
        state = request.form['state']
        zip = request.form['zip']

        new = Users() # new 클래스
        new.firstname = firstname
        new.lastname = lastname
        new.username = username
        new.password = password
        new.email = email
        new.address = address
        new.address2 = address2
        new.country = country
        new.state = state
        new.zip = zip


        db.session.add(new)
        db.session.commit()
        

    return render_template('index.html')

         
if __name__ == '__main__':
    app.run(debug=True)
    