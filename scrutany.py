from flask import Flask, Blueprint, render_template, request, jsonify, redirect,url_for,session
from flask_mysqldb import MySQL
from datetime import datetime
from datetime import date



scrutany = Blueprint('scrutany', __name__, template_folder='templates')


app = scrutany

mysql = MySQL()


@app.route("/scruthome", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        # Get the current date in the format 'Y-m-d'
        # current_date = datetime.date.today().strftime('%Y-%m-%d')
        # print(current_date)
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

        return render_template("scrutany_form.html",  datafaculty=datafaculty,datasubject=datasubject,datacourse=datacourse, datacourseid=datacourseid)



@app.route("/scrutanybuttion", methods=["POST", "GET"])
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
            query = "SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id,paper_count.scrutany_remaining FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id where faculty.faculty=%s and paper_count.scrutany_remaining!=0 and (paper_count.remaining_paper=0 or paper_count.moderation_remaining=0)"
            cursor.execute(query, (faculty,))

        elif search_option == "subject":
            query = "SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id,paper_count.scrutany_remaining FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id where subject.subject=%s  and paper_count.scrutany_remaining!=0 and (paper_count.remaining_paper=0 or paper_count.moderation_remaining=0)"
            cursor.execute(query, (subject_name,))
        
        elif search_option == "course_name":
            query = "SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id,paper_count.scrutany_remaining FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id where coursename.coursename=%s  and paper_count.scrutany_remaining!=0 and (paper_count.remaining_paper=0 or paper_count.moderation_remaining=0)"
            cursor.execute(query, (coursename,))
        
        elif search_option == "course_id":
            query = "SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id,paper_count.scrutany_remaining FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id where coursename.course_id=%s  and paper_count.scrutany_remaining!=0 and (paper_count.remaining_paper=0 or paper_count.moderation_remaining=0)"
            cursor.execute(query, (course_id,))

        print("query=",query)
        result = cursor.fetchall()
        print(result)
        cursor.execute('SELECT name,capfaculty_id FROM cap_project.cap_faculty where designation="Scrutiny Clerk"') 
        joblist1=cursor.fetchall()

        cursor.close()
        return render_template("scrutany_form.html",  result=result, selected_values=selected_values,joblist1=joblist1)
    
    else:
        return render_template("scrutany_form.html")
  
@app.route('/paper_scrutany', methods=["POST"])         
def paper_scrutany():
    
    now = datetime.now()
    issue_date=  now.strftime("%Y-%m-%d")
    print("issue_date=",issue_date)
    # return_date = request.form.getlist('return_date[]')
    # print("return_date=",return_date)
    papercount_id = request.form['papercount_id']
    print("papercount_id=",papercount_id)
    capfaculty_id = request.form['capfaculty_id']
    print("capfaculty_id=",capfaculty_id)
    from_count = request.form['from_count']
    print("from_count=",from_count)
    to_count = request.form['to_count']
    print("to_count=",to_count)
    scrutany_paper_count = request.form.get('scrutany_paper_count')
    print("scrutany_paper_count=",scrutany_paper_count)
    timetable_id = request.form['timetable_id']
    print("timetable_id=",timetable_id)
    
    
    cur = mysql.connection.cursor()
        
    # papercount_id = request.form.get('papercount_id')
    cur.execute('UPDATE paper_count SET scrutany_remaining=scrutany_remaining - %s WHERE papercount_id=%s',(scrutany_paper_count,papercount_id,))
    cur.execute("INSERT INTO scrutany (issue_date, papercount_id, capfaculty_id,from_count,to_count,scrutany_paper_count,timetable_id) VALUES (%s, %s, %s, %s, %s,%s,%s)", (issue_date, papercount_id,capfaculty_id,from_count,to_count,scrutany_paper_count,timetable_id))
    
    mysql.connection.commit()
        
    cur.close()

    return redirect('/scrutanybuttion')


@app.route('/backdatascrutany', methods=["POST"])
def backdatascrutany():
    papercount_id = request.form["papercount_id"]
    print("papercount_id:", papercount_id)
    cursor = mysql.connection.cursor()
    querysubject = 'select faculty.faculty,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,paper_count.count,paper_count.quespaper_code,paper_count.scrutany_remaining,paper_count.papercount_id,scrutany.from_count,scrutany.to_count,scrutany.issue_date,scrutany.scrutany_id,scrutany.scrutany_paper_count,cap_faculty.name from scrutany join time_table ON scrutany.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join paper_count on paper_count.papercount_id=scrutany.papercount_id inner join cap_faculty on cap_faculty.capfaculty_id=scrutany.capfaculty_id where paper_count.papercount_id=%s'
    cursor.execute(querysubject, (papercount_id,))
    backdata = cursor.fetchall()

    print("backdata:", backdata)
    cursor.close()
    return jsonify(backdata)


    