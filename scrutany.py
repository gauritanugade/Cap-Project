from flask import Flask, Blueprint, render_template, request, jsonify, redirect,url_for,session
from flask_mysqldb import MySQL


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
            query = "SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id,paper_count.scrutany_remaining FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id where faculty.faculty=%s"
            cursor.execute(query, (faculty,))

        elif search_option == "subject":
            query = "SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id,paper_count.scrutany_remaining FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id where subject.subject=%s"
            cursor.execute(query, (subject_name,))
        
        elif search_option == "course_name":
            query = "SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id,paper_count.scrutany_remaining FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id where coursename.coursename=%s"
            cursor.execute(query, (coursename,))
        
        elif search_option == "course_id":
            query = " SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id,paper_count.scrutany_remaining FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id where coursename.course_id=%s"
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
    
    issue_date = request.form['issue_date']
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