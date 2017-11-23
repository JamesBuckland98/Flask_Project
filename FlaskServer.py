import os
from flask import Flask, redirect, request, render_template
import sqlite3
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
DATABASE1='EventForm.db'
DATABASE2='login.db'
@app.route('/Upload', methods= ['POST','GET'])
def AddInfo():
    if request.method=='GET':
        return render_template("surveyForm.HTML")
    if request.method=='POST':
        date=request.form.get('date', default="Error")
        Attendance = request.form.get('attendance', default="Error")
        eventType = request.form.get('eventType', default="Error")
        males = int(request.form.get('slider', default="Error"))
        females= 100-males
        age= request.form.get('age', default="Error")
        print("uploading data")
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
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg
# Hugo Login Page DataBase
@app.route("/Login/loginweb", methods = ['GET','POST'])
def Loginintowebpage():
	if request.method =='GET':
		return render_template('login.html')
	if request.method =='POST':
		Username = request.form.get('Username', default="Error")#rem: args for get form for post
		Password = request.form.get('Password', default="Error")
		print("Welcome logger")
		print(Username)
		print(Password)
		try:
			conn = sqlite3.connect(DATABASE2)
			cur = conn.cursor()
			cur.execute("INSERT INTO Login ('Username', 'Password')\
						VALUES (?,?)",(Username, Password) )
			conn.commit()
			msg = "Login successfully implemented"
		except:
			conn.rollback()
			msg = "error in insert operation"
		finally:
			conn.close()
			return msg
@app.route("/Parent", methods=['GET'])
def returnParent():
    if request.method == 'GET':
        return render_template('ParentTemplate.html')

@app.route("/Form", methods=['GET'])
def returnForm():
    if request.method == 'GET':
        return render_template('ChildForm.html')

@app.route("/Login", methods=['GET'])
def returnLogin():
    if request.method == 'GET':
        return render_template('login.html')

@app.route("/Welcome", methods=['GET'])
def returnWelcome():
    if request.method == 'GET':
        return render_template('welcome.html')

@app.route("/Success", methods=['GET'])
def returnSuccess():
    if request.method == 'GET':
        return render_template('success.html')
@app.route("/AdminSearch",methods=['GET', 'POST'])
def returnAdminSearch():
    if request.method == 'GET':
        return render_template('Admin.html')
    if request.method == 'POST':
        try:
            date= request.form.get('date', default ="Error")
            conn = sqlite3.connect(DATABASE1)
            cur = conn.cursor()
            cur.execute("SELECT * FROM Event WHERE Date=? ",[date])
            data=cur.fetchall()
            print(data)
        except:
            print('Error with', data)
            conn.close()
        finally:
            conn.close()
            return str(data)


if __name__ == "__main__":
    app.run(debug=True)
