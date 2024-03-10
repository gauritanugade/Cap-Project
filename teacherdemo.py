from flask import Flask,Blueprint,render_template,request,session,make_response,redirect,flash,jsonify
from flask_mysqldb import MySQL
import itertools

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'cap_project'
app.secret_key='tybsc'

mysql = MySQL(app)

getquery="select * from cap_project.teacher"
@app.route('/')
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
	return render_template("teacherdemo.html",joblist=joblist,joblist1=joblist1,joblist3=joblist3 ) 

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



@app.route('/subject', methods=["POST"])
def subject():
    faculty = request.form["faculty"]
    print("faculty:", faculty)
    cursor = mysql.connection.cursor()
    querysubject = 'select subject.subject, faculty.faculty, subject.subject_id from subject inner join faculty on faculty.faculty_id=subject.faculty_id where cap_project.faculty.faculty_id=%s'
    cursor.execute(querysubject, (faculty,))
    subjects = cursor.fetchall()
    print("subject:", subjects)
    cursor.close()
    return jsonify(subjects)

@app.route('/submitteacher', methods=['POST', 'GET'])
def submitteacher():
	if request.method == 'POST':
		teacher_name = request.form["teacher_name"]
		print(teacher_name)
		teacher_email = request.form["teacher_email"]
		teacher_phoneno = request.form["teacher_phoneno"]
		faculty_id = request.form.getlist('Faculty')
		print(faculty_id)
		year = request.form.getlist('Year')
		sem = request.form.getlist('Sem')
		subject_id = request.form.getlist('subject')
		coursename_id = request.form.getlist('coursename')
		
		print("coursename_id:", coursename_id)
		cursor = mysql.connection.cursor()
		query = "INSERT INTO cap_project.teacher (teacher_name, teacher_email, teacher_phoneno) VALUES (%s, %s, %s)"
		cursor.execute(query, (teacher_name, teacher_email, teacher_phoneno))
		teac_id = cursor.lastrowid
		
		for (fac, y, s, sub, cour) in zip(faculty_id, year, sem, subject_id, coursename_id):
			query1 = "INSERT INTO cap_project.teacher_course (year, sem, faculty_id, coursename_id, subject_id, teacher_id) VALUES (%s, %s, %s, %s, %s, %s)"
			cursor.execute(query1, (y, s, fac, cour, sub, teac_id))
		mysql.connection.commit()
		cursor.close()
		return render_template("teacherdemo.html")



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
	
if __name__ == '__main__':
	app.run(debug=True)