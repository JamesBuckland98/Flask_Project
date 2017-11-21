import os
from flask import Flask, redirect, request, render_template
import sqlite3
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
DATABASE='InfoForm.db'
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
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO Event('Date', 'Attendance','Males','Females')\
            VALUES (?,?,?,?)",(date, Attendance, males, females ))
            conn.commit()
            msg = "Record successfully added"
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
