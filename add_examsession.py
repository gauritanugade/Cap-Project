from flask import Flask,Blueprint,render_template,request
from flask_mysqldb import MySQL
add_examsession = Blueprint('add_examsession', __name__, template_folder='templates')

app=add_examsession


mysql=MySQL()

displayall="select * from cap_project.examsession"


@app.route('/addsession')
def home(): 
	cursor =mysql.connection.cursor()
	cursor.execute('SELECT pattern,pattern_id FROM cap_project.pattern') 
	joblist=cursor.fetchall() 
	print("list:",joblist)
	cursor.execute('SELECT faculty, duration,faculty_id FROM cap_project.faculty') 
	joblist1=cursor.fetchall() 
	#print("list:",joblist1)
	cursor.close()
	return render_template("exam_session.html",joblist=joblist,joblist1=joblist1)


@app.route("/getYear", methods=["POST"])
def getYear():
	degree= request.form['degree']
	print("selected fac: ", degree)
	cursor =mysql.connection.cursor()
	cursor.execute('SELECT degree FROM cap_project.faculty' ) 
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


@app.route('/dataexamsession', methods = ['POST','GET'])
def data():
	print("Hii sayaliS")
	if request.method == 'POST':
		month=request.form["month"]
		exam_year=request.form["exam_year"]
		pattern_id=request.form["pattern"]
		degree=request.form["degree"]
		year=request.form["Year"]
		sem=request.form["Sem"]
		print(sem)
		subject= request.form.getlist('subject')
		print(subject)
		
		for sub in subject:
			cursor=mysql.connection.cursor()
			query="insert into cap_project.examsession(month,exam_year,pattern_id,degree,year,sem,faculty_id) values (%s,%s,%s,%s,%s,%s,%s)" 
			cursor.execute(query,(month,exam_year,pattern_id,degree,year,sem,sub,))
			mysql.connection.commit()
			cursor.close()
	return render_template("exam_session.html")

	
@app.route('/session_data', methods = ['POST'])
def faculty_data():
	msg=''
	if request.method == 'POST':
		cursor=mysql.connection.cursor()
		query="SELECT * FROM cap_project.examsession"
		cursor.execute(query)
		data=cursor.fetchall()
		cursor.close()
		return render_template("examsession.html",examsession=data)