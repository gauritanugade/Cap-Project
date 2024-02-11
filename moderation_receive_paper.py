from flask import Flask, Blueprint, render_template, request, jsonify, redirect,url_for,session
from flask_mysqldb import MySQL


moderation_receive_paper = Blueprint('moderation_receive_paper', __name__, template_folder='templates')


app = moderation_receive_paper

mysql = MySQL()


@app.route("/moderationreceivehome", methods=["POST", "GET"])
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
        
        return render_template("moderation_receive_paper.html", datateacher=data,datafaculty=datafaculty,datacourse=datacourse,datacourseid=datacourseid)



@app.route("/searchsubjects", methods=['GET', 'POST'])
def searchsubjects():
    
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
            'moderation_paper_count': request.form.getlist('moderation_paper_count[]'),
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
            query = "select paper_count.quespaper_code,teacher.year,teacher.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,moderation.papercount_id,moderation.teacher_id,moderation.timetable_id,moderation.issue_date,moderation.from_count,moderation.to_count,moderation.moderation_paper_count, moderation.moderation_id from moderation JOIN time_table ON moderation.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join teacher on teacher.teacher_id=moderation.teacher_id INNER JOIN paper_count ON paper_count.papercount_id=moderation.papercount_id WHERE teacher.teacher_name=%s"
            cursor.execute(query, (teacher_name,))

        elif search_option == "faculty":
            query = "select paper_count.quespaper_code,teacher.year,teacher.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,moderation.papercount_id,moderation.teacher_id,moderation.timetable_id,moderation.issue_date,moderation.from_count,moderation.to_count,moderation.moderation_paper_count, moderation.moderation_id from moderation JOIN time_table ON moderation.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join teacher on teacher.teacher_id=moderation.teacher_id INNER JOIN paper_count ON paper_count.papercount_id=moderation.papercount_id WHERE faculty.faculty=%s"
            cursor.execute(query, (faculty,))
        
        elif search_option == "course_name":
            query = " select paper_count.quespaper_code,teacher.year,teacher.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,moderation.papercount_id,moderation.teacher_id,moderation.timetable_id,moderation.issue_date,moderation.from_count,moderation.to_count,moderation.moderation_paper_count, moderation.moderation_id from moderation JOIN time_table ON moderation.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join teacher on teacher.teacher_id=moderation.teacher_id INNER JOIN paper_count ON paper_count.papercount_id=moderation.papercount_id WHERE coursename.coursename=%s"
            cursor.execute(query, (coursename,))
        
        elif search_option == "course_id":
            query = "select paper_count.quespaper_code,teacher.year,teacher.sem,subject.subject,coursename.coursename,coursename.course_id,faculty.faculty,moderation.papercount_id,moderation.teacher_id,moderation.timetable_id,moderation.issue_date,moderation.from_count,moderation.to_count,moderation.moderation_paper_count, moderation.moderation_id from moderation JOIN time_table ON moderation.timetable_id=time_table.timetable_id JOIN subject ON  time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id inner join teacher on teacher.teacher_id=moderation.teacher_id INNER JOIN paper_count ON paper_count.papercount_id=moderation.papercount_id WHERE coursename.course_id=%s"
            cursor.execute(query, (course_id,))

        print("query=",query)
        result = cursor.fetchall()
        print(result)

        cursor.close()
        return render_template("moderation_receive_paper.html",  result=result, papercount_id=papercount_id, teacher_id=teacher_id, timetable_id=timetable_id,selected_values=selected_values)
    
    else:
        return render_template("moderation_receive_paper.html")



@app.route('/paper_receives', methods=["POST"])         
def paper_receives(): 

    cur = mysql.connection.cursor()  
    moderation_id = request.form.get('moderation_id')
    print("moderation_id",moderation_id)
    
    return_date = request.form.get('return_date')
    print("return_date",return_date)
   
    cur.execute('UPDATE moderation SET return_date = %s  WHERE moderation_id = %s',(return_date,moderation_id))

    mysql.connection.commit()
        
    cur.close()

    return redirect('/searchsubjects')