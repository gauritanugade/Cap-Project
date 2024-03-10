from flask import Flask, Blueprint, render_template, request, jsonify, redirect,url_for,session
from flask_mysqldb import MySQL
from datetime import datetime
from datetime import date


receive_paper = Blueprint('receive_paper', __name__, template_folder='templates')


app = receive_paper

mysql = MySQL()

 
@app.route("/receivehome", methods=["POST", "GET"])
def home():
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
        
        return render_template("receive_paper.html", datateacher=data,datafaculty=datafaculty,datacourse=datacourse,datacourseid=datacourseid)


 
@app.route("/searchsubject", methods=['GET', 'POST'])
def searchsubject():
    
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
            query = " select paper_count.quespaper_code,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,issue_check.papercount_id,issue_check.teacher_id,issue_check.timetable_id,issue_check.issue_date,issue_check.from_count,issue_check.to_count,issue_check.teacher_paper_count,issue_check.issue_check_id,DATEDIFF(NOW(), issue_check.issue_date) AS difference from issue_check JOIN time_table ON issue_check.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join teacher on teacher.teacher_id=issue_check.teacher_id INNER JOIN paper_count ON paper_count.papercount_id=issue_check.papercount_id WHERE teacher.teacher_name=%s  and issue_check.return_date is null"            
            cursor.execute(query, (teacher_name,))

        elif search_option == "faculty":
            query = "select paper_count.quespaper_code,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,issue_check.papercount_id,issue_check.teacher_id,issue_check.timetable_id,issue_check.issue_date,issue_check.from_count,issue_check.to_count,issue_check.teacher_paper_count, issue_check.issue_check_id,DATEDIFF(NOW(), issue_check.issue_date) AS difference from issue_check JOIN time_table ON issue_check.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join teacher on teacher.teacher_id=issue_check.teacher_id INNER JOIN paper_count ON paper_count.papercount_id=issue_check.papercount_id WHERE faculty.faculty =%s  and issue_check.return_date is null"
            cursor.execute(query, (faculty,))
        
        elif search_option == "course_name":
            query = " select paper_count.quespaper_code,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,issue_check.papercount_id,issue_check.teacher_id,issue_check.timetable_id,issue_check.issue_date,issue_check.from_count,issue_check.to_count,issue_check.teacher_paper_count, issue_check.issue_check_id,DATEDIFF(NOW(), issue_check.issue_date) AS difference from issue_check JOIN time_table ON issue_check.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join teacher on teacher.teacher_id=issue_check.teacher_id INNER JOIN paper_count ON paper_count.papercount_id=issue_check.papercount_id WHERE coursename.coursename =%s  and issue_check.return_date is null"
            cursor.execute(query, (coursename,))
        
        elif search_option == "course_id":
            query = "select paper_count.quespaper_code,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,issue_check.papercount_id,issue_check.teacher_id,issue_check.timetable_id,issue_check.issue_date,issue_check.from_count,issue_check.to_count,issue_check.teacher_paper_count, issue_check.issue_check_id,DATEDIFF(NOW(), issue_check.issue_date) AS difference from issue_check JOIN time_table ON issue_check.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join teacher on teacher.teacher_id=issue_check.teacher_id INNER JOIN paper_count ON paper_count.papercount_id=issue_check.papercount_id WHERE coursename.course_id=%s  and issue_check.return_date is null"
            cursor.execute(query, (course_id,))

        print("query=",query)
        result = cursor.fetchall()
        print(result)

        cursor.close()
        return render_template("receive_paper.html",  result=result, papercount_id=papercount_id, teacher_id=teacher_id, timetable_id=timetable_id,selected_values=selected_values)
    
    else:
        return render_template("receive_paper.html")
    
@app.route('/paper_receive', methods=["POST"])         
def paper_receive(): 

    cur = mysql.connection.cursor()  
    issue_check_id = request.form.get('issue_check_id')
    print("issue_check_id",issue_check_id)
    now = datetime.now()
    return_date =  now.strftime("%Y-%m-%d")
    print("return_date",return_date)
    # cur.execute(' UPDATE paper_count SET remaining_paper = remaining_paper - %s WHERE papercount_id = %s',(return_date))

    cur.execute('UPDATE issue_check SET return_date = %s  WHERE issue_check_id = %s',(return_date,issue_check_id))

    mysql.connection.commit()
        
    cur.close()

    return redirect('/searchsubject')