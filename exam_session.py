from flask import Flask,Blueprint,render_template,request
from flask_mysqldb import MySQL

exam_session = Blueprint('exam_session', __name__, template_folder='templates')

app=exam_session


mysql=MySQL()
query="insert into cap.examsession (faculty,semester,sem_year,sem_month,pattern) values (%s,%s,%s,%s,%s)" 
displayall="select * from cap.examsession"

@app.route('/exam_session')
def home():
	cursor =mysql.connection.cursor()
	cursor.execute('SELECT faculty, duration FROM cap.faculty') 
	joblist=cursor.fetchall() 
	print("list:",joblist)
	cursor.close()
	return render_template("examsession_form.html",joblist=joblist)

@app.route('/examsessiondata', methods = ['POST','GET'])
def data():
	if request.method == 'POST':
		faculty= request.form['Faculty']
		semester = request.form['semester']
		sem_year=int( request.form ["sem_year"])
		sem_month=request.form ["sem_month"]
		pattern=request.form ["pattern"]
		cursor=mysql.connection.cursor()
		cursor.execute(query,(faculty,semester,sem_year,sem_month,pattern,))
		mysql.connection.commit()
		cursor.close()
		cursor=mysql.connection.cursor()
		cursor.execute(displayall)
		data =cursor.fetchall()
		cursor.close()
	return render_template('examsession.html',exam_session=data)

if __name__=='__main__':
	app.run(debug=True)

