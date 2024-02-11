from flask import Flask,Blueprint,render_template,request,redirect
from flask_mysqldb import MySQL
import itertools



add_pattern = Blueprint('add_pattern', __name__, template_folder='templates')

app=add_pattern

mysql=MySQL()

@app.route('/add_pattern')
def home():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT faculty, duration,faculty_id FROM cap_project.faculty') 
    joblist=cursor.fetchall() 
    return render_template("add_pattern_form.html",joblist=joblist)

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


@app.route('/pattern', methods = ['POST'])
def pattern():
    print("hii")
    if request.method == 'POST':
        faculty= request.form['Faculty']
        year=request.form ['Year']
        pattern=request.form ['pattern']
        theory_mark=request.form['theory_mark']
        internal_mark=request.form['internal_mark']
        print(internal_mark)
        cursor=mysql.connection.cursor()
        query="insert into cap_project.pattern(faculty_id,year,pattern,theory_mark,internal_mark) values (%s,%s,%s,%s,%s)"
        cursor.execute(query,(faculty,year,pattern,theory_mark,internal_mark))
        mysql.connection.commit()
        cursor.close()
        return render_template('add_pattern_form.html')
 
@app.route('/pattern_data')
def pattern_data():
    cursor=mysql.connection.cursor()
    print(cursor)
    query="select * from cap_project.pattern1"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    cursor.close()
    return render_template("data_pattern.html",pattern1=data)
