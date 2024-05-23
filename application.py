#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
#from flask_ngrok import run_with_ngrok



app = Flask(__name__)
#run_with_ngrok(app)

app.secret_key="SecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://sql9343746:3aUkY3fHFF@sql9.freemysqlhosting.net/sql9343746'
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://sql9343746:3aUkY3fHFF@sql9.freemysqlhosting.net/sql9343746'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dob = db.Column(db.DateTime)
    gender = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    country = db.Column(db.String(100))

    def __init__(self, name, dob, gender, email, phone, country):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone = phone
        self.country = country

@app.route('/')
def Index():
    all_data = Test.query.all()

    return render_template('index.html', employees = all_data)


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        country = request.form['country']


        my_data = Test(name, dob, gender, email, phone, country)
        db.session.add(my_data)
        db.session.commit()

        flash('Employee Updated Successfully')

        return redirect(url_for('Index'))

@app.route('/update', methods = ['GET','POST'])
def update():

    if request.method == 'POST':
        my_data = Test.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.dob = request.form['dob']
        my_data.gender = request.form['gender']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        my_data.country = request.form['country']

        db.session.commit()
        flash('Employee Updated Successfully')

        return redirect(url_for('Index'))


@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Test.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)