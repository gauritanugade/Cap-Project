from flask import Flask,Blueprint,render_template,request,session,make_response,redirect,flash,jsonify
from flask_mysqldb import MySQL
import itertools


add_course = Blueprint('add_course', __name__, template_folder='templates')

app=add_course


mysql=MySQL()


getquery="select * from cap_project.coursefield"

@app.route('/addcourse')
def home(): 
	cursor =mysql.connection.cursor()
	cursor.execute('SELECT faculty, duration,faculty_id FROM cap_project.faculty') 
	joblist=cursor.fetchall() 
	#print("list:",joblist)
	cursor.execute('SELECT subject,subject_id FROM cap_project.subject') 
	joblist1=cursor.fetchall() 
	#print("list:",joblist1)
	cursor.close()
	return render_template("add_course_form.html",joblist=joblist,joblist1=joblist1 ) 


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


@app.route('/add_course',methods=['POST'])
def course_data():
	print("hgdshghdsga")
	if request.method=='POST':
		faculty_name=request.form["Faculty"]
		subject_id=request.form['subject']
		year= request.form['Year']
		sem= request.form['Sem']

		course_id=request.form.getlist('course_id')
		course_name=request.form.getlist('course_name')
		print("course id :",course_id)
		print("course_name :",course_name)
		# subject =request.form['subject']
		print("subject_id:",subject_id)
		cursor=mysql.connection.cursor()
		q5="insert into cap_project.coursefield(faculty_id, subject_id,year,sem) values(%s,%s,%s,%s)"
		
		cursor.execute(q5,(faculty_name,subject_id,year,sem))
		print("query :",q5)
		# cursor.execute("insert into cap_project.coursename(course_id,coursename,coursefield_id) values(%s,%s,%s)",(course_id,course_name,cursor.lastrowid))
		mysql.connection.commit()
		curr_id=cursor.lastrowid

		for (cid,cname) in zip(course_id, course_name):
			print(cid,cname)
			query="insert into cap_project.coursename(course_id,coursename,coursefield_id) values(%s,%s,%s)"
			val=(cid,cname,curr_id)
			try:
				cursor.execute(query, val)
				mysql.connection.commit()
			except mysql.connection.IntegrityError as e:
                # Duplicate entry, handle accordingly
				cursor.close()
				return "duplicate"
		return "success"

	
@app.route('/course_data', methods = ['POST'])
def data_course():
	msg=''
	if request.method == 'POST':
		cursor=mysql.connection.cursor()
		query="select cap_project.coursefield.faculty_id,cap_project.coursefield.subject_id,cap_project.coursefield.year,cap_project.coursefield.sem,cap_project.coursename.course_id,cap_project.coursename.coursename from cap_project.coursefield inner join cap_project.coursename on cap_project.coursefield.coursefield_id = cap_project.coursename.coursefield_id;"
		cursor.execute(query)
		data=cursor.fetchall()
		print("data :",data)
		cursor.close()
	return "done"