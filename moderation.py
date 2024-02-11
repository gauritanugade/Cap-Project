
from flask import Flask, Blueprint, render_template, request, jsonify, redirect,url_for,session
from flask_mysqldb import MySQL
from datetime import datetime
from datetime import date


moderation = Blueprint('moderation', __name__, template_folder='templates')


app = moderation

mysql = MySQL()


# @app.route("/moderation")
# def home():
#     return render_template("moderation_form.html")


@app.route("/moderation", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        
        cursor = mysql.connection.cursor()
       

        queryfaculty = "SELECT faculty FROM faculty"
        cursor.execute(queryfaculty)
        datafaculty = [row[0] for row in cursor.fetchall()]

        queryteacher = "SELECT subject FROM subject"
        cursor.execute(queryteacher)
        datasubject = [row[0] for row in cursor.fetchall()]

        querycourse = "SELECT coursename FROM coursename"
        cursor.execute(querycourse)
        datacourse = [row[0] for row in cursor.fetchall()]

        querycourseid = "SELECT course_id FROM coursename"
        cursor.execute(querycourseid)
        datacourseid = [row[0] for row in cursor.fetchall()]

        return render_template("moderation.html",  datafaculty=datafaculty,datasubject=datasubject,datacourse=datacourse, datacourseid=datacourseid)

@app.route("/moderationbuttion", methods=["POST", "GET"])
def scrutanybuttion():
    if request.method == "POST": 
        search_option = request.form.get('radio_option')
        print("search_option:",search_option)
        

        faculty = request.form.get('faculty')
        print("faculty:",faculty)

        subject_name = request.form.get('subject_name')
        print("subject_name:",subject_name)
        coursename = request.form.get('course_name')
        course_id = request.form.get('course_id')
        selected_values = session.get('selected_values')

        cursor = mysql.connection.cursor()
        # query= "SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id"
        cursor = mysql.connection.cursor()
        if search_option == "faculty":
            query = " SELECT faculty.faculty, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, paper_count.count, paper_count.quespaper_code, paper_count.papercount_id, time_table.timetable_id,paper_count.moderation_remaining FROM paper_count JOIN time_table ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id WHERE paper_count.count > 100 and time_table.year = 3 and faculty.faculty=%s and paper_count.remaining_paper=0  and paper_count.moderation_remaining!=0"
            cursor.execute(query, (faculty,))

        elif search_option == "subject":
            query = "SELECT faculty.faculty, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, paper_count.count, paper_count.quespaper_code, paper_count.papercount_id, time_table.timetable_id,paper_count.moderation_remaining FROM paper_count JOIN time_table ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id WHERE paper_count.count > 100 and time_table.year = 3 and subject.subject=%s and paper_count.remaining_paper=0  and paper_count.moderation_remaining!=0"
            cursor.execute(query, (subject_name,))
        
        elif search_option == "course_name":
            query = "SELECT faculty.faculty, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, paper_count.count, paper_count.quespaper_code, paper_count.papercount_id, time_table.timetable_id,paper_count.moderation_remaining FROM paper_count JOIN time_table ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id WHERE paper_count.count > 100 and time_table.year = 3 and coursename.coursename=%s and paper_count.remaining_paper=0  and paper_count.moderation_remaining!=0"
            cursor.execute(query, (coursename,))
        
        elif search_option == "course_id":
            query = "SELECT faculty.faculty, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, paper_count.count, paper_count.quespaper_code, paper_count.papercount_id, time_table.timetable_id,paper_count.moderation_remaining FROM paper_count JOIN time_table ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id WHERE paper_count.count > 100 and time_table.year = 3 and coursename.course_id=%s and paper_count.remaining_paper=0  and paper_count.moderation_remaining!=0"
            cursor.execute(query, (course_id,))

            print("query=",query)
        result = cursor.fetchall()
        print(result)
       
    
        queryteacher='select teacher_name,teacher_id from teacher'
        cursor.execute(queryteacher) 
        joblist = cursor.fetchall()
        print(joblist)

        cursor.close()
        return render_template("moderation.html",  result=result, selected_values=selected_values,joblist=joblist)
    
    else:
        return render_template("moderation.html")
    
@app.route('/paper_moderation', methods=["POST"])         
def paper_moderation(): 
    now = datetime.now()
    issue_date=  now.strftime("%Y-%m-%d")
    print("issue_date=",issue_date)
     
    papercount_id = request.form['papercount_id']
    print("papercount_id=",papercount_id)
    teacher_id = request.form['teacher_id'] 
    print("teacher_id=",teacher_id)
    cases = request.form['cases']
    print("cases=",cases)
    timetable_id = request.form['timetable_id']
    print("timetable_id=",timetable_id)
    moderation_paper_count = request.form.get('moderation_paper_count')
    print("moderation_paper_count=",moderation_paper_count)
    from_count = request.form['from_count']
    print("from_count=",from_count)
    to_count = request.form['to_count']
    print("to_count=",to_count)

    cur = mysql.connection.cursor()
    
    
    cur = mysql.connection.cursor()
    papercount_id = request.form.get('papercount_id')
    cur.execute('UPDATE paper_count SET moderation_remaining=moderation_remaining - %s WHERE papercount_id=%s',(moderation_paper_count,papercount_id,))
    cur.execute("INSERT INTO moderation (issue_date,cases, papercount_id, teacher_id, from_count,to_count,moderation_paper_count,timetable_id) VALUES (%s, %s, %s,%s,%s, %s, %s,%s)", (issue_date,cases, papercount_id, teacher_id,from_count,to_count,moderation_paper_count, timetable_id))
    mysql.connection.commit()
        
    cur.close()

    return redirect('/moderationbuttion')


@app.route('/backdatamoderation', methods=["POST"])
def backdatamoderation():
    papercount_id = request.form["papercount_id"]
    print("papercount_id:", papercount_id)
    cursor = mysql.connection.cursor()
    querysubject = 'select faculty.faculty,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,paper_count.count,paper_count.quespaper_code,paper_count.moderation_remaining,paper_count.papercount_id,moderation.from_count,moderation.to_count,moderation.issue_date,moderation.moderation_id,moderation.moderation_paper_count,teacher.teacher_name,moderation.cases from moderation join time_table ON moderation.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join paper_count on paper_count.papercount_id=moderation.papercount_id inner join teacher on teacher.teacher_id=moderation.teacher_id where paper_count.papercount_id=%s'
    cursor.execute(querysubject, (papercount_id,))
    backdata = cursor.fetchall()

    print("backdata:", backdata)
    cursor.close()
    return jsonify(backdata)