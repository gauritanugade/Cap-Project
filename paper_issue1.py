from flask import Flask, Blueprint, render_template, request, jsonify, redirect,url_for,session
from flask_mysqldb import MySQL
from datetime import datetime
from datetime import date


paper_issue1 = Blueprint('paper_issue1', __name__, template_folder='templates')


app = paper_issue1

mysql = MySQL()


@app.route("/issuehome", methods=["POST", "GET"])
def home():
     print("issue home called")
     if request.method == "GET": 

        cursor = mysql.connection.cursor()
        queryteacher = "SELECT teacher_name FROM teacher"
        cursor.execute(queryteacher)
        data = [row[0] for row in cursor.fetchall()]

        queryfaculty = "SELECT faculty FROM faculty"
        cursor.execute(queryfaculty) 
        datafaculty = [row[0] for row in cursor.fetchall()]

        querycourse = "SELECT coursename FROM coursename"
        cursor.execute(querycourse) 
        datacourse = [row[0] for row in cursor.fetchall()]

        querycourseid = "SELECT course_id FROM coursename"
        cursor.execute(querycourseid) 
        datacourseid = [row[0] for row in cursor.fetchall()]

        print("teacher: ", data)
        print("datacourse: ", datacourse)
        print("datacourseid: ", datacourseid)
        
        return render_template("searchitem1.html", datateacher=data,datafaculty=datafaculty,datacourse=datacourse,datacourseid=datacourseid)


 
@app.route("/search_subject", methods=['GET', 'POST'])
def search_subject():
    
    if request.method == 'POST':
        search_option = request.form.get('radio_option')
        teacher_name = request.form.get('teacher_name')
        faculty = request.form.get('faculty')
        coursename = request.form.get('course_name')
        course_id = request.form.get('course_id')

        timetable_id = request.form.get('timetable_id')
        papercount_id = request.form.get('papercount_id')
        teacher_id = request.form.get('teacher_id')

        session['selected_values'] = {
            'teacher_paper_count': request.form.getlist('teacher_paper_count[]'),
            'issue_date': request.form.getlist('issue_date[]'),
            'return_date': request.form.getlist('return_date[]')
        }
        selected_values = session.get('selected_values')

        print("teacher_name: ", teacher_name)
        print("faculty: ", faculty)
        print("coursename: ", coursename)
        print("course_id: ", course_id)
        
        cursor = mysql.connection.cursor()
        if search_option == "teacher_name":
            query = " SELECT faculty.faculty,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,paper_count.count,paper_count.quespaper_code,time_table.timetable_id,teacher.teacher_id,paper_count.papercount_id,paper_count.remaining_paper FROM paper_count join time_table on time_table.timetable_id=paper_count.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id join teacher_course on coursename.coursename_id=teacher_course.coursename_id join teacher on teacher_course.teacher_id=teacher.teacher_id where teacher.teacher_name=%s and paper_count.remaining_paper!=0;"
            cursor.execute(query, (teacher_name,))

        elif search_option == "faculty":
            query ="SELECT faculty.faculty,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,paper_count.count,paper_count.quespaper_code,time_table.timetable_id,paper_count.papercount_id,paper_count.remaining_paper from paper_count  JOIN time_table ON time_table.timetable_id = paper_count.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id  WHERE faculty.faculty =%s and paper_count.remaining_paper!=0"            
            cursor.execute(query, (faculty,))
        
        elif search_option == "course_name":
            query="SELECT faculty.faculty,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,paper_count.count,paper_count.quespaper_code,time_table.timetable_id,paper_count.papercount_id,paper_count.remaining_paper from paper_count  JOIN time_table ON time_table.timetable_id = paper_count.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id  WHERE coursename.coursename =%s and paper_count.remaining_paper!=0"            
            cursor.execute(query, (coursename,))
        
        elif search_option == "course_id":
            query = "SELECT faculty.faculty,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,paper_count.count,paper_count.quespaper_code,time_table.timetable_id,paper_count.papercount_id,paper_count.remaining_paper from paper_count  JOIN time_table ON time_table.timetable_id = paper_count.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id  WHERE coursename.course_id =%s and paper_count.remaining_paper!=0"            
            cursor.execute(query, (course_id,))

        print("query=",query)
        result = cursor.fetchall()
        print(result)

        cursor.execute('SELECT  teacher.teacher_name,teacher_id FROM cap_project.teacher') 
        joblist1=cursor.fetchall()

        cursor.close()

        return render_template("searchitem1.html", result=result, papercount_id=papercount_id, teacher_id=teacher_id, timetable_id=timetable_id,selected_values=selected_values,joblist1=joblist1)
    
    else:
        return redirect("/issuehome")
        
        
        
@app.route('/paper_issue', methods=["POST"])         
def paper_issue(): 
    # issue_date = request.form['issue_date[]']
    # print("issue_date=",issue_date)
    now = datetime.now()
    issue_date=  now.strftime("%Y-%m-%d")
    print("issue_date=",issue_date)

    papercount_id = request.form['papercount_id']
    print("papercount_id=",papercount_id)
    teacher_id = request.form['teacher_id'] 
    print("teacher_id=",teacher_id)
    from_count = request.form['from_count']
    print("from_count=",from_count)

    to_count = request.form['to_count']
    print("to_count=",to_count)
    teacher_paper_count = request.form.get('teacher_paper_count')
    print("teacher_paper_count=",teacher_paper_count)
    timetable_id = request.form['timetable_id']
    print("timetable_id=",timetable_id)

    cur = mysql.connection.cursor()
    
    teacher_paper_count = request.form.get('teacher_paper_count')
    print("teacher_paper_count",teacher_paper_count)

    papercount_id = request.form.get('papercount_id')
    print("papercount_id",papercount_id)
    
    cur.execute(' UPDATE paper_count SET remaining_paper = remaining_paper - %s WHERE papercount_id = %s',(teacher_paper_count,papercount_id,))
    issuepaper="INSERT INTO issue_check (issue_date,papercount_id, teacher_id,from_count,to_count,teacher_paper_count, timetable_id) VALUES (%s, %s, %s, %s, %s, %s,%s)"
    cur.execute(issuepaper,(issue_date,papercount_id, teacher_id,from_count,to_count,teacher_paper_count, timetable_id))            
  
    issuepaperdata= cur.fetchall()
    print("issuepaperdata",issuepaperdata)
    mysql.connection.commit()
        
    cur.close()

    return redirect('/search_subject')


@app.route('/backdata', methods=["POST"])
def backdata():
    papercount_id = request.form["papercount_id"]
    print("papercount_id:", papercount_id)
    cursor = mysql.connection.cursor()
    querysubject = 'select faculty.faculty,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,paper_count.count,paper_count.quespaper_code,paper_count.remaining_paper,paper_count.papercount_id,issue_check.from_count,issue_check.to_count,issue_check.issue_date,issue_check.issue_check_id,issue_check.teacher_paper_count from issue_check  JOIN time_table  ON issue_check.timetable_id = time_table.timetable_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join paper_count on paper_count.papercount_id=issue_check.papercount_id inner join teacher on teacher.teacher_id=issue_check.teacher_id where paper_count.papercount_id=%s'
    cursor.execute(querysubject, (papercount_id,))
    backdata = cursor.fetchall()

    print("backdata:", backdata)
    cursor.close()
    return jsonify(backdata)