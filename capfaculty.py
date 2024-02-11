from flask import Flask,Blueprint,render_template,request,redirect
from flask_mysqldb import MySQL
from datetime import datetime
from werkzeug.utils import secure_filename
import os

capfaculty = Blueprint('capfaculty', __name__, template_folder='templates')

app=capfaculty


mysql=MySQL()


query="insert into cap_project.cap_faculty (name,designation,appoiment_date,appoiment_letter,examsession_id,contact_no,email,biometric) values (%s,%s,%s,%s,%s,%s,%s,%s)"
displayall=" select name,designation,appoiment_date,examsession.month,examsession.exam_year,contact_no,email from cap_project.cap_faculty inner join cap_project.examsession on cap_project.examsession.examsession_id=cap_project.cap_faculty.examsession_id"
@app.route('/capfacultyform')
def home():
	cursor=mysql.connection.cursor()
	cursor.execute('SELECT month,exam_year,examsession_id FROM cap_project.examsession') 
	joblist1=cursor.fetchall() 
	print("list:",joblist1)
	cursor.close()
	return render_template("capfaculty_form.html",joblist1=joblist1) 
	
@app.route('/capfacultydata', methods = ['POST','GET'])
def data():
	if request.method=='POST':
		input=request.form
		f=request.files['appoiment_letter']
		filename=secure_filename(f.filename)
		print(filename)
		examsession_id = request.form["examsession_id"]
		print("Examsession_id:",examsession_id)
		name=request.form["name"]
		designation=request.form["designation"]
		appoiment_date= request.form ["appoiment_date"]
		# appoiment_letter=request.form["appoiment_letter"]
		contact_no=request.form["contact_no"]
		email= request.form ["email"]
		biometric=request.form["biometric"]

		static_folder_path = os.path.join(os.path.dirname(os.path.abspath(f.filename)), 'static\\appoiment_letters')
		file_path = os.path.join(static_folder_path, f.filename)
		print("file_path=",file_path)
		f.save(file_path)

		cursor=mysql.connection.cursor()
		cursor.execute(query,(name,designation,appoiment_date,file_path,examsession_id,contact_no,email,biometric,))	
		mysql.connection.commit()
		cursor.close()
		cursor=mysql.connection.cursor()
		cursor.execute(displayall)

		data =cursor.fetchall()
		print("data:",data)
		cursor.close()
	# return render_template('capfaculty.html',faculty=data)
		return redirect('/capfacultyform')