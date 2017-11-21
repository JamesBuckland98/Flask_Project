import os
from flask import Flask, redirect, request, render_template
import sqlite3
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
DATABASE1='InfoForm.db'
DATABASE2='login.db'
@app.route('/Upload', methods= ['POST','GET'])
def AddInfo():
    if request.method=='GET':
        return render_template("surveyForm.HTML")
    if request.method=='POST':
        date=request.form.get('date', default="Error")
        Attendance = request.form.get('attendance', default="Error")
        eventType = request.form.get('eventType', default="Error")
        slider = request.form.get('slider', default="Error")
        age= request.form.get('age', default="Error")
        print("uploading data")
        try:
            conn = sqlite3.connect(DATABASE1)
            cur = conn.cursor()
            cur.execute("INSERT INTO Event('Date', 'Attendance','Males','Females')\
            VALUES (?,?,?,?)",(date, Attendance, slider, 100-slider))
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
def returnInheritanceBase():
    if request.method == 'GET':
        return render_template('ChildForm.html')

if __name__ == "__main__":
    app.run(debug=True)
