 


from flask import Flask, Blueprint, render_template, request, jsonify, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
 

# Replace these connection parameters with your database credentials
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_DB']='cap_project'
 


mysql = MySQL(app)
query = "insert into cap_project.time_table (examsession_id,subject_id,exam_year,coursename_id,date,starttime,endtime,year,sem,faculty_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
displayall = "select exam_year,month,degree from cap_project.examsession"


@app.route('/timetable')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute(
        'SELECT month,exam_year,examsession_id FROM cap_project.examsession')
    joblist = cursor.fetchall()
    print("list:", joblist)

    cursor.execute(
        'SELECT faculty, duration,faculty_id FROM cap_project.faculty')
    joblist1 = cursor.fetchall()
    print("list:", joblist1)

    cursor.execute('SELECT pattern,pattern_id FROM cap_project.pattern')
    joblist2 = cursor.fetchall()
    print("list:", joblist2)
    cursor.close()
    return render_template("timetabledemo.html", joblist=joblist, joblist1=joblist1, joblist2=joblist2)



 
@app.route("/getYear", methods=["POST"])
def getYear():
    degree = request.form['degree']
    print("selected fac: ", degree)
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT degree FROM cap_project.faculty')
    duration = cursor.fetchone()[0]
    print("duration:", duration)
    cursor.close()
    return str(duration)

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


@app.route('/faculty', methods=["POST"])
def faculty():
    degree = request.form["degree"]
    print("degree:", degree)
    cursor = mysql.connection.cursor()
    queryselect = 'select cap_project.faculty.faculty,cap_project.examsession.degree,cap_project.faculty.faculty_id from cap_project.faculty inner join cap_project.examsession on cap_project.faculty.faculty_id=cap_project.examsession.faculty_id where cap_project.examsession.degree=%s'
    cursor.execute(queryselect, (degree,))
    faculties = cursor.fetchall()

    print("faculties:", faculties)
    cursor.close()
    return jsonify(faculties)


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


@app.route('/course', methods=["POST"])
def course():
    subject = request.form["subject"]
    print("subject:", subject)
    cursor = mysql.connection.cursor()
    querycourse = 'select cap_project.coursename.course_id,cap_project.coursename.coursename,cap_project.coursefield.subject_id, cap_project.coursename.coursename_id from cap_project.coursename inner join cap_project.coursefield on cap_project.coursefield.coursefield_id=cap_project.coursename.coursefield_id where cap_project.coursefield.subject_id=%s'
    cursor.execute(querycourse, (subject,))
    courses = cursor.fetchall()

    print("courses:", courses)
    cursor.close()
    return jsonify(courses)


@app.route('/timetabledata', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        Examsession_id = request.form["Examsession_id"]
        print("Examsession_id:",Examsession_id)
        # degreedrop=request.form["degreedrop"]
        print("request: ", request.form)
        Year = request.form["Year"]
        print("Year:",Year)
        Sem = request.form["Sem"]
        print("Sem:",Sem)
        faculty = request.form["facultyradio"]
        print("faculty:",faculty)
        subject = request.form["subjectradio"]
        print("subject:",subject)
        courses=request.form.getlist('courses[]')
        print("courses:",courses)

        date=request.form.getlist('date[]')
        print("date:",date)
        starttime=request.form.getlist('starttime[]')
        print("starttime:",starttime)
        endtime=request.form.getlist('endtime[]')
        print("endtime:",endtime)
       
        cursor = mysql.connection.cursor()

        for cour,dates,stime,etime in zip(courses,date,starttime,endtime):
            print(cour,dates,stime,etime )
            cursor.execute("insert into cap_project.time_table (examsession_id,subject_id,coursename_id,date,starttime,endtime,year,sem,faculty_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Examsession_id,subject,cour,dates,stime,etime,Year,Sem,faculty,))
        
            print("gauri:", cursor)
        mysql.connection.commit()
        cursor.execute(displayall)
        data = cursor.fetchall()
        print("data:",data)
        cursor.close()
        return redirect('/timetable')

    else:
        query1="use cap_project"
        cursor=mysql.connection.cursor()
        cursor.execute(query1)
        query2="select cap_project.time_table.date,cap_project.time_table.starttime,time_table.endtime,coursename.course_id,coursename.coursename,faculty.faculty,time_table.year,time_table.sem,examsession.month,examsession.exam_year,pattern.pattern from time_table inner join cap_project.coursename on time_table.coursename_id=cap_project.coursename.coursename_id inner join cap_project.examsession  on cap_project.time_table.examsession_id=cap_project.examsession.examsession_id inner join cap_project.faculty on time_table.faculty_id=faculty.faculty_id inner join pattern on examsession.pattern_id=pattern.pattern_id"
        cursor.execute(query2)

        data=cursor.fetchall()
        cursor.close() 
        print("print:",data)
        return render_template('timetable.html',timetable=data,Examsession_id="",faculty="faculty",Year="Year")
    
if __name__== '__main__':
    app.run(debug=True)