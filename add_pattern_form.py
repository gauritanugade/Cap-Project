from flask import Flask, Blueprint, render_template, request, jsonify, redirect
from flask_mysqldb import MySQL
from datetime import datetime

add_pattern_form = Blueprint('add_pattern_form', __name__, template_folder='templates')

app = add_pattern_form

mysql = MySQL()

query="insert into cap_project.pattern(pattern,theory_mark,internal_mark,year,faculty_id) values (%s,%s,%s,%s,%s)"
displayall="select * from cap_project.pattern"

@app.route('/select')
def home():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT faculty, duration FROM cap_project.faculty') 
    joblist=cursor.fetchall() 
    return render_template("add_pattern_form.html",joblist=joblist)


@app.route('/pattern', methods = ['POST'])
def pattern():
    if request.method == 'POST':
        faculty= request.form['Faculty']
        year=int( request.form ["year"])
        pattern=request.form ["pattern"]
        theory_mark=request.form["theory_mark"]
        internal_mark=request.form["internal_mark"]
        cursor=mysql.connection.cursor()
        cursor.execute(query,(pattern,theory_mark,internal_mark,year,faculty))
        mysql.connection.commit()
        cursor.close()
        cursor=mysql.connection.cursor()
        cursor.execute(displayall)
        data =cursor.fetchall()
        cursor.close()
    return render_template('add_pattern_form.html',data=data)

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
