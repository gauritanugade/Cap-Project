from flask import Flask,Blueprint,render_template,request,session,make_response,redirect,flash
from flask_mysqldb import MySQL
import itertools


add_teacher_details = Blueprint('add_teacher_details', __name__, template_folder='templates')

app=add_teacher_details


mysql=MySQL()

getquery="select * from cap_project.teacher"
@app.route('/addteacher')
def home(): 
	cursor =mysql.connection.cursor()
	cursor.execute('SELECT faculty, duration,faculty_id FROM cap_project.faculty') 
	joblist=cursor.fetchall() 
	print("list:",joblist)
	cursor.execute('SELECT subject,subject_id FROM cap_project.subject') 
	joblist1=cursor.fetchall() 
	print("list:",joblist1)

	cursor.execute('SELECT course_id,coursename ,coursename_id FROM cap_project.coursename') 
	joblist3=cursor.fetchall() 
	print("list:",joblist3)
	cursor.close()
	return render_template("techer.html",joblist=joblist,joblist1=joblist1,joblist3=joblist3 ) 






@app.route("/getYear", methods=["POST"])
def getYear():
	faculty= request.form['faculty']
	print("selected fac: ", faculty)
	cursor =mysql.connection.cursor()
	cursor.execute('SELECT duration FROM cap_project.faculty WHERE faculty_id= %s', (faculty,) ) 
	duration=cursor.fetchone()[0] 
	print("duration:",duration)
	cursor.close()
	return str(duration)


@app.route("/getSem", methods=["POST"])
def getSem():
	year = int(request.form['year'])
	print("new year", year)
	sem1 = year * 2 - 1
	sem2 = year * 2
	return [sem1, sem2]

@app.route('/submitteacher', methods = ['POST','GET'])
def submitteacher():
	if request.method == 'POST':
		teacher_name=request.form["teacher_name"]
		print(teacher_name)
		teacher_email=request.form["teacher_email"]
		teacher_phoneno= request.form ["teacher_phoneno"]
		year=request.form["Year"]
		sem=request.form["Sem"]
		faculty_id=request.form["Faculty"]
		print(faculty_id)
		# coursename_id=request.form["coursename"]
		coursename_id=request.form["coursename"]

		print("coursename_id:",coursename_id)
		subject_id=request.form["subject"]
		cursor =mysql.connection.cursor()
		query="insert into cap_project.teacher(teacher_name,teacher_email,teacher_phoneno,year,sem,faculty_id,coursename_id,subject_id) values(%s,%s,%s,%s,%s,%s,%s,%s)"
		cursor.execute(query,(teacher_name,teacher_email,teacher_phoneno,year,sem,faculty_id,coursename_id,subject_id,))	
		mysql.connection.commit()
		cursor.close()
	return render_template("techer.html")


	
@app.route('/teacher_data', methods = ['POST'])
def teacher_data():
	msg=''
	if request.method == 'POST':
		cursor=mysql.connection.cursor()
		query="SELECT * FROM cap_project.teacher"
		cursor.execute(query)
		data=cursor.fetchall()
		cursor.close()
		return render_template("teacher_data.html",teacher=data)