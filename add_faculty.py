from flask import Flask,Blueprint,render_template,request,url_for
from flask_mysqldb import MySQL	
import itertools

add_faculty = Blueprint('add_faculty', __name__, template_folder='templates')


app=add_faculty
mysql=MySQL()

@app.route('/form')
def home():
	return render_template("add_faculty_form.html")


@app.route('/submit', methods = ['POST'])
def insertData():
	if request.method == 'POST':
		faculty = request.form.getlist('Faculty') 
		duration = request.form.getlist('duration')
		sem = request.form.getlist('sem_pattern')

		print("Faculty  = ",faculty)
		print("duration = ",duration)
		print("sem = ",sem)

		for (f,d,s) in zip(faculty, duration, sem):
			print(f,d,s)
			cursor=mysql.connection.cursor()
			print("curs:",cursor)
			query="insert into cap_project.faculty (faculty,duration,sem_pattern) values (%s,%s,%s)"
			val=(f,d,s)
			try:
				cursor.execute(query, val)
				
			except mysql.connection.IntegrityError as e:
                # Duplicate entry, handle accordingly
				cursor.close()
				return "duplicate"
		mysql.connection.commit()
		return "success"
	

