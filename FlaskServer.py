import os
from flask import Flask, redirect, request, render_template, session, escape
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
DATABASE1='RugbyEvents.db'
DATABASE2='login.db'
DATABASE3='pin.db'
customer = []
app.secret_key ='gLFdXn6X'
@app.route('/Upload', methods= ['POST','GET'])
def AddInfo():
    if request.method=='GET':
        conn = sqlite3.connect(DATABASE1)
        cur = conn.cursor()
        cur.execute("SELECT eventName FROM Events")
        data=cur.fetchall()
        return render_template("ChildForm.HTML", data=data)
    if request.method=='POST':
        date = request.form.get('date')
        if date == "":
            return render_template("ChildForm.html", msg="Please select a Date.")
        eventName = request.form.get('eventName')
        if eventName == "":
            return render_template("ChildForm.html", msg="Please select an Event.")
        # Attendance = int(request.form.get('attendance'))
        # if Attendance == "":
        #     return render_template("ChildForm.html", msg="Please fill in Attendance.")
        # elif Attendance < 0:
        #     return render_template("ChildForm.html", msg="Please set Attendance greater than 0.")
        # try:
        #     except ValueError:
        #         return render_template("ChildForm.html", msg= "Please set a valid Attendance number.")
        eventType = request.form.get('eventType')
        if eventType == "":
            return render_template("ChildForm.html", msg= "Please select an Event type.")
        males = int(request.form.get('slider'))
        females = 100-males
        age = request.form.get('age')
        if age == "":
            return render_template("ChildForm.html", msg="Please select an Age.")
        gameType = request.form.get('gameType')
        if gameType == "":
            return render_template("ChildForm.html", msg="Please select a Game.")
        print("uploading data - ")
        print("{} {} {} {} {} {} {} {}".format(date,eventName,Attendance,eventType,males,females,age,gameType))

        try:
            conn = sqlite3.connect(DATABASE1)
            cur = conn.cursor()
            cur.execute("INSERT INTO Activities('date','eventName','attendance','eventType','Male','Female', 'GameID')\
            VALUES (?,?,?,?,?,?,?)",(date, eventName, Attendance, eventType, males, females, '1' ))
            cur.execute("INSERT INTO Games('gameType', 'ageRange')\
            VALUES (?,?)", (gameType, age))
            conn.commit()
            msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "Please fill in all fields correctly"
        finally:
            if msg == "Record successfully added":
                conn.close()
                return render_template("success.html", msg=msg)
            else:
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
        username=request.cookies.get('username')
        userType=request.cookies.get('userType')
        if 'userType' in session:
            userType= escape(session['userType'])
        if userType=="admin":
            return render_template('Admin.html')
        else:
            return render_template('ChildForm.html')

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
            cur.execute("SELECT * FROM Activities WHERE date=? ",[date])
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
        session.clear()
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
            elif data==[('admin',)] and data2==[('password',)]:
                session['userType']='admin'
                print(session['userType'])
                return render_template("Admin.html")
            else:
                session['userType']= 'staff'
                session['username']= username
                print(session['userType'])
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
    if request.method=='GET':
        return render_template("NewUser.html ")
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        repassword=request.form.get('repassword')
        email=request.form.get('email')
        FirstName=request.form.get('FirstName')
        surname=request.form.get('Surname')
        pin=str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        print("uploading data")
        print(username)
        print(password)
        print(repassword)
        print(email)
        print(pin)
        customer.append(FirstName)
        customer.append(surname)
        customer.append(email)
        customer.append(username)
        customer.append(password)
        print(customer)
        # FIX THIS:
        conn = sqlite3.connect(DATABASE3)
        cur = conn.cursor()
        cur.execute("INSERT INTO pin('pin')\
                    VALUES (?)",(pin,))
        conn.commit()
        msg= Message("Your pin",sender="notabot554@gmail.com",recipients=[email])
        msg.body='your pin is: '+ pin
        mail.send(msg)
        conn.close()
        return redirect("/Pin")

@app.route("/Pin", methods=['GET','POST'])
def getPin():
    if request.method=='GET':
        return render_template("pin.html")
    if request.method=='POST':
        pin=request.form.get('pin')
        FirstName=customer[0]
        surname=customer[1]
        email=customer[2]
        username=customer[3]
        password=customer[4]
        print(customer)
        print(FirstName)
        print(surname)
        print(username)
        print(password)
        conn=sqlite3.connect(DATABASE3)
        cur = conn.cursor()
        cur.execute("SELECT pin FROM pin WHERE pin=?",[pin])
        data=cur.fetchall()
    if data==[]:
        conn.close()
        msg='pin is incorrect'
        return render_template("pin.html",msg=msg)
    else:
        try:
            conn=sqlite3.connect(DATABASE2)
            cur = conn.cursor()
            cur.execute("INSERT INTO Login ('FirstName','Surname','Email','Username', 'Password')\
                        VALUES (?,?,?,?,?)",(FirstName,surname, email, username, password))
            conn.commit()
            while len(customer)>0:
                customer.pop()
            print(customer)
            msg="data uploaded successfully"
        except:
            conn.rollback()
            msg='Username already exists please try again'
            while len(customer)>0:
                customer.pop()
            print(customer)
        finally:
            conn.close()
            return render_template("NewUser.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
