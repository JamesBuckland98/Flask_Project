import os
from flask import Flask, redirect, request, render_template
from flask_mail import Mail, Message
from datetime import datetime
import sqlite3
import random
app = Flask(__name__)
#Configure Flask-Mail to use GMail
app.config.update(
    DEBUG=True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
    MAIL_USERNAME = 'notabot554@gmail.com',
    MAIL_PASSWORD = '3KAjFtJCLmsy5d3UHTKwFXRb8wNXPaV3p4WMcCsRmZJ46pfLtWXgseUzT6HhAyp7'
    )
mail=Mail(app)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
DATABASE1='EventForm.db'
DATABASE2='login.db'
filename='contacts.txt'
filename2="message.txt"
@app.route('/Upload', methods= ['POST','GET'])
def AddInfo():
    if request.method=='GET':
        return render_template("ChildForm.HTML")
    if request.method=='POST':
        date = request.form.get('date')
        if date == "":
            return render_template("ChildForm.html", msg="Please fill in the date.")
        Attendance = request.form.get('attendance')
        if Attendance == "":
            return render_template("ChildForm.html", msg="Please fill in the attendance.")
        if Attendance < 0:
            return render_template("ChildForm.html", msg="Attendance must be a positive number.")
        eventType = request.form.get('eventType')
        males = int(request.form.get('slider'))
        females= 100-males
        age= request.form.get('age')
        print("Uploading data:")
        print(date)
        print(Attendance)
        print(males)
        print(females)
        print(eventType)
        print(age)
        try:
            conn = sqlite3.connect(DATABASE1)
            cur = conn.cursor()
            cur.execute("INSERT INTO Events('Date', 'Attendance','male','female')\
            VALUES (?,?,?,?)",(date, Attendance, males, females ))
            cur.execute("INSERT INTO Games('gameType', 'ageRange', 'eventID')\
            VALUES (?,?,?)", (eventType, age, "1"))
            conn.commit()
            msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "Please fill in all fields"
        finally:
            conn.close()
            return render_template("ChildForm.html", msg=msg)

@app.route("/NewUser", methods=['GET','POST'])
def returnNewUser():
    if request.method=='GET':
        return render_template('NewUser.html')
    if request.method=='POST':
        try:
            username=request.form.get('username')
            password=request.form.get('password')
            repassword=request.form.get('repassword')
            contactnumber=request.form.get('contactnumber')
            email=request.form.get('email')
            print("uploading data")
            print(username)
            print(password)
            print(repassword)
            print(contactnumber)
            print(email)
            conn=sqlite3.connect(DATABASE2)
            cur = conn.cursor()
            cur.execute("INSERT INTO Login ('Username', 'Password', 'ContactNumber', 'Email')\
						VALUES (?,?,?,?)",(username, password, contactnumber, email))
            conn.commit()
            msg = "record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return render_template('NewUser.html', msg=msg)

@app.route("/AdminSearch",methods=['GET', 'POST'])
def returnAdminSearch():
    if request.method == 'GET':
        return render_template('Admin.html')
    if request.method == 'POST':
        try:
            date= request.form.get('date', default ="Error")
            game= request.form.get('eventType', default="Error")
            age= request.form.get('age', default="Error")
            print(date)
            print(game)
            print(age)
            conn = sqlite3.connect(DATABASE1)
            cur = conn.cursor()
            cur.execute("SELECT * FROM Events WHERE Date=? ",[date])
            data=cur.fetchall()
            cur.execute("SELECT * FROM Games WHERE gameType=?",[game])
            data2=cur.fetchall()
            cur.execute("SELECT * FROM Games WHERE ageRange=?",[age])
            data3=cur.fetchall()
            print(data)
            print(data2)
            print(data3)
        except:
            print('Error with', data)
            conn.close()
        finally:
            conn.close()
            return render_template("AdminTable.html", data= data, data2=data2, data3= data3)

@app.route("/Login" , methods=['GET', 'POST'])
def returnLogin():
    if request.method=='GET':
        return render_template("James_login.html")
    if request.method=='POST':
        try:
            username=request.form.get('username', default="Error")
            password=request.form.get('password', default="Error")
            print("fetching data")
            print(username)
            print(password)
            conn=sqlite3.connect(DATABASE2)
            cur = conn.cursor()
            cur.execute("SELECT Username FROM Login WHERE Username=?",[username])
            data=cur.fetchall()
            cur.execute("SELECT Password FROM Login WHERE Password=?",[password])
            data2=cur.fetchall()
            print(data)
            print(data2)
        except:
            print('error with',data)
            conn.close()
        finally:
            if data ==[] or data2 == []:
                conn.close()
                msg="Username or password is incorrect"
                return render_template("James_login.html",msg=msg)
            else:
                return render_template("ChildForm.html")
@app.route("/Parent", methods=['GET'])
def returnParent():
    if request.method == 'GET':
        return render_template('ParentTemplate.html')


@app.route("/Welcome", methods=['GET'])
def returnWelcome():
    if request.method == 'GET':
        return render_template('welcome.html')

@app.route("/Success", methods=['GET'])
def returnSuccess():
    if request.method == 'GET':
        return render_template('success.html')
@app.route("/email", methods=['GET','POST'])
def index():
    msg= Message("Hello",sender="notabot554@gmail.com",recipients=["jamesbuckland98@gmail.com"])
    msg.body='This is a test email'
    mail.send(msg)
    return 'email sent'
if __name__ == "__main__":
    app.run(debug=True)
