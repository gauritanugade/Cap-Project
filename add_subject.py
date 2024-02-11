



from flask import Flask,Blueprint,render_template,request,redirect
from flask_mysqldb import MySQL
import itertools


add_subject = Blueprint('add_subject', __name__, template_folder='templates')


app=add_subject


mysql=MySQL()



query="insert into cap_project.subject (subject,faculty_id,pattern_id) values (%s,%s,%s)"
displayall="select * from cap_project.subject"

@app.route('/selectdata')
def home(): 
	cursor =mysql.connection.cursor()
	cursor.execute('SELECT faculty, duration,faculty_id FROM cap_project.faculty') 
	joblist=cursor.fetchall() 
	# print("list:",joblist)
	# cursor.execute('SELECT pattern,pattern_id FROM cap_project.pattern')
	cursor.execute(" SELECT DISTINCT pattern, MAX(pattern_id) AS pattern_id FROM cap_project.pattern GROUP BY pattern;")

	joblist1=cursor.fetchall()
	cursor.close()
	return render_template("subject_form.html",joblist=joblist,joblist1=joblist1) 

@app.route('/subject_add', methods = ['POST'])
def subject():
	print("Hii...!")
	if request.method == 'POST':
		faculty_id= int(request.form['Faculty'])
		pattern_id= int(request.form['pattern'])
		print("pattern_id:",pattern_id)

		print("faculty:",faculty_id)
		subjects= request.form.getlist('subject')

		print("subject:",subjects)

		for sub in subjects:
			cursor = mysql.connection.cursor()
			
			query="insert into cap_project.subject(faculty_id,subject, pattern_id) values (%s,%s,%s)"
			val=(faculty_id,sub, pattern_id)
			try:
				cursor.execute(query, val)
				mysql.connection.commit()
			except mysql.connection.IntegrityError as e:
                # Duplicate entry, handle accordingly
				cursor.close()
				return "duplicate"
		return "success"

	
@app.route('/subject_data', methods = ['POST'])
def faculty_data():
	msg=''
	if request.method == 'POST':
		cursor=mysql.connection.cursor()
		query="SELECT * FROM cap_project.subject"
		cursor.execute(query)
		data=cursor.fetchall()
		cursor.close()
		return render_template("subject_data.html",subject=data)



