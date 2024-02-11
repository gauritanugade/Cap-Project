from flask import Flask, Blueprint, render_template, request, jsonify, redirect
from flask_mysqldb import MySQL
from datetime import datetime

timetable_display = Blueprint('timetable_display', __name__, template_folder='templates')

app = timetable_display

mysql = MySQL()

@app.route('/selection')
def home():
	cursor =mysql.connection.cursor()
	cursor.execute('SELECT month,exam_year,pattern_id,examsession_id FROM cap_project.examsession') 
	joblist4=cursor.fetchall() 
	print("list:",joblist4)
	cursor.execute('SELECT faculty, duration,faculty_id FROM cap_project.faculty') 
	joblist5=cursor.fetchall() 
	print("list:",joblist5)
	cursor.close()
	return render_template("time_dis.html",joblist4=joblist4,joblist5=joblist5)

@app.route("/Year", methods=["POST"])
def Year():
	faculty= request.form['faculty']
	print("selected fac: ", faculty)
	cursor =mysql.connection.cursor()
	cursor.execute('SELECT duration FROM cap_project.faculty WHERE faculty_id = %s', (faculty,) ) 
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

@app.route('/displaytimetable' , methods = ['POST'])
def display():  
    Examsession_id = request.form["Examsession_id"]
    print("Examsession_id:",Examsession_id)
    faculty = request.form["Faculty"]
    print("faculty:",faculty)
    Year = request.form["Year"]
    Sem = request.form["Sem"]
    querycap="use cap_project"
    cursor=mysql.connection.cursor()
    cursor.execute(querycap)
    #query3=" select cap_project.time_table.date,cap_project.time_table.starttime,time_table.endtime,coursename.course_id,coursename.coursename,faculty.faculty,time_table.year,time_table.sem,examsession.month,examsession.exam_year,pattern.pattern from time_table inner join cap_project.coursename on time_table.coursename_id=cap_project.coursename.coursename_id inner join cap_project.examsession  on cap_project.time_table.examsession_id=cap_project.examsession.examsession_id inner join cap_project.faculty on time_table.faculty_id=faculty.faculty_id inner join pattern on examsession.pattern_id=pattern.pattern_id where cap_project.time_table.sem=%s and cap_project.time_table.year=%s and cap_project.faculty.faculty=%s and cap_project.examsession.examsession_id=%s"
    query3=" select time_table.date,time_table.starttime,time_table.endtime,time_table.year,time_table.sem,faculty.faculty,coursename.course_id,coursename.coursename,examsession.month,examsession.exam_year,pattern.pattern from time_table inner join faculty on time_table.faculty_id=faculty.faculty_id inner join examsession on time_table.examsession_id=examsession.examsession_id inner join coursename on time_table.coursename_id=coursename.coursename_id inner join pattern on examsession.pattern_id=pattern.pattern_id where time_table.year=%s and time_table.sem=%s and time_table.faculty_id=%s and time_table.examsession_id=%s"
    cursor=mysql.connection.cursor()
    cursor.execute(query3,(Year,Sem,faculty,Examsession_id,))
    data=cursor.fetchall()
    print("All=",data)
    examsession_query="select examsession.month,examsession.exam_year,pattern.pattern from examsession inner join pattern on pattern.pattern_id=examsession.pattern_id where examsession_id=%s"
    cursor.execute(examsession_query,(Examsession_id,))
    examsession=cursor.fetchone()
    print("Examsession:",examsession)
    exam_name=str(examsession[0]) + " "+str(examsession[1]) +" " + str(examsession[2])
    if Year=="1":
        yearRom = "I"
    elif Year == "2":
        yearRom = "II"
    elif Year == "3":
         yearRom = "III"
    elif Year == "4":
         yearRom = "IV"
    else:
         yearRom = ""

    return render_template('timetable.html',timetable=data,Examname=exam_name,faculty=faculty,year=yearRom,sem=Sem)

