from flask import Blueprint, render_template
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

main_app = Blueprint('main_app', __name__, template_folder='templates')

mysql = MySQL()

@main_app.route('/admin')
def adminPage():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COUNT(*) AS faculty_count FROM faculty")
    facultydata = cursor.fetchone()[0]
    print("facultydata", facultydata)

    cursor.execute("SELECT COUNT(DISTINCT pattern) AS pattern_count from pattern")
    patterndata = cursor.fetchone()[0]
    print("patterndata", patterndata)

    cursor.execute("SELECT COUNT(*) AS subject_count FROM subject")
    subjectdata = cursor.fetchone()[0]
    print("subjectdata", subjectdata)

    cursor.execute("SELECT COUNT(*) AS coursename_count FROM coursename")
    coursenamedata = cursor.fetchone()[0]
    print("coursenamedata", coursenamedata)

    cursor.execute("SELECT COUNT(DISTINCT teacher_name) AS teacher_count FROM teacher")
    teacherdata = cursor.fetchone()[0]
    print("teacherdata", teacherdata)

    cursor.execute("select count(DISTINCT name) as cap_faculty_count from cap_faculty")
    capmemeber = cursor.fetchone()[0]
    cursor.close()  # Close the cursor

    return render_template('cardes.html', facultydata=facultydata,patterndata=patterndata,subjectdata=subjectdata,coursenamedata=coursenamedata,teacherdata=teacherdata,capmemeber=capmemeber)


    # return render_template('homepage.html')

@main_app.route('/capfaculty')
def capfacultypage():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COUNT(*) AS count_ok_remark_and_remaining_paper_zero FROM paper_count WHERE remark = 'OK' AND remaining_paper != 0")
    okdata = cursor.fetchone()[0]
    print("subjectdata", okdata)

    cursor.execute("SELECT COUNT(*) AS remark_count_pending FROM  paper_count_pending where status = 0 and remark='Pending'")
    pendingdata = cursor.fetchone()[0]
    print("coursenamedata", pendingdata)

    cursor.execute("SELECT COUNT(*) AS null_return_date_count FROM issue_check WHERE return_date IS NULL")
    isuuerecive = cursor.fetchone()[0]
    print("coursenamedata", pendingdata)

    cursor=mysql.connection.cursor()
    cursor.execute("select teacher_name from teacher")
    teacherdata = cursor.fetchall()

    cursor=mysql.connection.cursor()
    cursor.execute("select name from cap_faculty;")
    capname = cursor.fetchall()
    
    return render_template('cardescap.html',okdata=okdata,pendingdata=pendingdata,isuuerecive=isuuerecive,teacherdata=teacherdata,capname=capname)

@main_app.route('/')
def homepage():
    
    return render_template('homepage1.html')
