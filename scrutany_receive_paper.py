from flask import Flask, Blueprint, render_template, request, jsonify, redirect,url_for,session
from flask_mysqldb import MySQL
from datetime import datetime
from datetime import date



scrutany_receive_paper = Blueprint('scrutany_receive_paper',__name__, template_folder='templates')


app = scrutany_receive_paper

mysql = MySQL()


@app.route("/scrutreceivehome", methods=["POST", "GET"])
def home():
     if request.method == "GET": 

        cursor = mysql.connection.cursor()

        queryfaculty = "SELECT faculty FROM faculty"
        cursor.execute(queryfaculty) 
        datafaculty = [row[0] for row in cursor.fetchall()]

        querycourse = "SELECT coursename FROM coursename"
        cursor.execute(querycourse) 
        datacourse = [row[0] for row in cursor.fetchall()]

        querycourseid = "SELECT course_id FROM coursename"
        cursor.execute(querycourseid) 
        datacourseid = [row[0] for row in cursor.fetchall()]
        
        return render_template("scrutany_receive_paper.html",datafaculty=datafaculty,datacourse=datacourse,datacourseid=datacourseid)

@app.route("/searchscrutany", methods=['GET', 'POST'])
def searchscrutany():
    
    
    if request.method == 'POST':
        search_option = request.form.get('radio_option')
        faculty = request.form.get('faculty')
        coursename = request.form.get('course_name')
        course_id = request.form.get('course_id')

        timetable_id = request.form.get('timetable_id')
        papercount_id = request.form.get('papercount_id')
 
        session['selected_values'] = {
            'issue_date': request.form.getlist('issue_date[]'),
            'return_date': request.form.getlist('return_date[]')
        }
        selected_values = session.get('selected_values')

        print("faculty: ", faculty)
        print("coursename: ", coursename)
        print("course_id: ", course_id)
        
        cursor = mysql.connection.cursor()
        

        if search_option == "faculty":
            query = "select paper_count.quespaper_code,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,scrutany.papercount_id,scrutany.timetable_id,scrutany.issue_date,scrutany.from_count,scrutany.to_count,scrutany.scrutany_paper_count,scrutany.scrutany_id, DATEDIFF(NOW(), scrutany.issue_date) AS difference from scrutany JOIN time_table ON scrutany.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id INNER JOIN paper_count ON paper_count.papercount_id=scrutany.papercount_id WHERE faculty.faculty=%s and scrutany.return_date is null"
            cursor.execute(query, (faculty,))
        
        elif search_option == "course_name":
            query = " select paper_count.quespaper_code,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,scrutany.papercount_id,scrutany.timetable_id,scrutany.issue_date,scrutany.from_count,scrutany.to_count,scrutany.scrutany_paper_count,scrutany.scrutany_id, DATEDIFF(NOW(), scrutany.issue_date) AS difference from scrutany JOIN time_table ON scrutany.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id INNER JOIN paper_count ON paper_count.papercount_id=scrutany.papercount_id WHERE coursename.coursename=%s and scrutany.return_date is null"
            cursor.execute(query, (coursename,))
        
        elif search_option == "course_id":
            query = "select paper_count.quespaper_code,time_table.year,time_table.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,scrutany.papercount_id,scrutany.timetable_id,scrutany.issue_date,scrutany.from_count,scrutany.to_count,scrutany.scrutany_paper_count,scrutany.scrutany_id, DATEDIFF(NOW(), scrutany.issue_date) AS difference from scrutany JOIN time_table ON scrutany.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id INNER JOIN paper_count ON paper_count.papercount_id=scrutany.papercount_id WHERE coursename.course_id=%s and scrutany.return_date is null"
            cursor.execute(query, (course_id,))

        print("query=",query)
        result = cursor.fetchall()
        print(result)
        
        cursor.close()
        return render_template("scrutany_receive_paper.html",  result=result, papercount_id=papercount_id, timetable_id=timetable_id,selected_values=selected_values)
    
    else:
        return render_template("scrutany_receive_paper.html")
    
@app.route('/scrutany_paper_receive', methods=["POST"])         
def scrutany_paper_receive(): 
    cur = mysql.connection.cursor()  
    scrutany_id = request.form.get('scrutany_id')
    print("scrutany_id",scrutany_id)
    
    now = datetime.now()
    return_date =  now.strftime("%Y-%m-%d")
    print("return_date",return_date)


    cur = mysql.connection.cursor()
    cur.execute('UPDATE scrutany SET return_date = %s  WHERE scrutany_id = %s',(return_date,scrutany_id))
    mysql.connection.commit()
    cur.close()
    return redirect('/searchscrutany')