from flask import Flask, Blueprint, render_template, request, jsonify, redirect,url_for
from flask_mysqldb import MySQL
from datetime import datetime

paper_register= Blueprint('paper_register', __name__, template_folder='templates')

app = paper_register

mysql = MySQL()

@app.route('/selectdate',methods=["POST","GET"])
def home():
    cursor =mysql.connection.cursor()
    cursor.execute('SELECT month,exam_year,pattern_id,examsession_id FROM cap_project.examsession') 
    # cursor.execute(' SELECT DISTINCT month, exam_year, MAX(examsession_id) AS examsession_id FROM cap_project.examsession GROUP BY month, exam_year') 

   
    joblist4=cursor.fetchall()
    print("list:",joblist4)
    cursor.execute('SELECT name,capfaculty_id FROM cap_project.cap_faculty') 
    joblist=cursor.fetchall()
    print("cap_faculty:",joblist)
    
    if request.method=="GET":
        return render_template('paper_count.html',joblist4=joblist4,joblist=joblist,data=[],data1=[])
    
    else:
        examsession_id=request.form['examsession_id']
        date = request.form["date"]
        querycap="use cap_project"
        cursor=mysql.connection.cursor()
        cursor.execute(querycap)
        query3='select time_table.date,time_table.starttime,time_table.endtime,faculty.faculty,coursename.course_id,coursename.coursename,examsession.month,examsession.exam_year,time_table.timetable_id,examsession.examsession_id from time_table inner join faculty on time_table.faculty_id=faculty.faculty_id inner join examsession on time_table.examsession_id=examsession.examsession_id inner join coursename on time_table.coursename_id=coursename.coursename_id  where time_table.examsession_id=%s and time_table.date=%s'

        cursor.execute(query3,(examsession_id,date,))
        data=cursor.fetchall()
        print("All=",data)
        cursor.close()
        return render_template('paper_count.html',joblist4=joblist4,data=data,examsession_id=examsession_id,date=date,joblist=joblist)


@app.route('/paper_register',methods=["POST"])
def paper_register8(): 
    print("Gauriiiiiii")
    quespaper_code=request.form.getlist('quespaper_code[]')
    print("queapaper:",quespaper_code)
    count=request.form.getlist('count[]')
    print("count:",count)
    remark=request.form.getlist('remark[]')
    print("remark:",remark)
    reason=request.form.getlist('reason[]')
    print("reason:",reason)
    capfaculty_id=request.form['capfaculty_id'] 
    print("capfaculty_id:",capfaculty_id)
    received_date=request.form['received_date']
    print("received_date:",received_date)
    examsession_id=request.form.getlist('examsession_id[]')
    print("examsession_id:",examsession_id)
    timetable_id =request.form['timetable_id']
    print("timetable_id:",timetable_id)
    submited_name=request.form['submited_name']
    print("submited_name:",submited_name)
 

    cursor=mysql.connection.cursor()
    print("loop")
    for paper_code, papercount, re_mark, rs, examsessionid in zip(quespaper_code, count, remark, reason, examsession_id):
        print("papercode",paper_code, papercount, re_mark, rs, examsessionid)
        remaining_paper = int(papercount)
        scrutany_remaining = int(papercount)
        moderation_remaining = int(papercount)
        print("remaining_paper:", remaining_paper)

        if re_mark == "OK":
            cursor.execute(f"INSERT INTO cap_project.paper_count(quespaper_code, count, remark, reason, capfaculty_id, received_date, examsession_id, timetable_id, submited_name, remaining_paper,scrutany_remaining,moderation_remaining) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",
               (paper_code, papercount, re_mark, rs, capfaculty_id, received_date, examsessionid, timetable_id, submited_name, remaining_paper,scrutany_remaining,moderation_remaining))
        elif re_mark == "Pending":
            cursor.execute(f"INSERT INTO cap_project.paper_count_pending(quespaper_code, count, remark, reason,received_date,examsession_id,timetable_id,submited_name,capfaculty_id) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               (paper_code, papercount, re_mark, rs, received_date, examsessionid, timetable_id, submited_name,capfaculty_id, ))


        else:
            # Handle other cases or raise an error
            continue

        # cur.execute(f"INSERT INTO cap_project.{table_name} (quespaper_code, count, remark, reason, capfaculty_id, received_date, examsession_id, timetable_id, submited_name, remaining_paper) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #             (paper_code, papercount, re_mark, rs, capfaculty_id, received_date, examsessionid, time_id, submited_name, remaining_paper,))

    mysql.connection.commit()
    cursor.close()

    return redirect('/selectdate')

@app.route('/pending')
def pending():
    print("Heloooo")
    querycap="use cap_project"
    cursor=mysql.connection.cursor()
    cursor.execute(querycap)
    querystatus='select paperpending_id,quespaper_code,count,remark,reason,received_date,examsession_id,timetable_id,submited_name,capfaculty_id,case when status=1 then "ok" else "pending" end as status from paper_count_pending where status=0'

    cursor.execute(querystatus)
    statusdata=cursor.fetchall()
    print("pendingAll=",statusdata)
    cursor.close()
    cursor =mysql.connection.cursor()
    cursor.execute('SELECT name,capfaculty_id FROM cap_project.cap_faculty') 
    joblist5=cursor.fetchall()
    print("cap_faculty:",joblist5)
    return render_template('paper_count.html',statusdata=statusdata,joblist5=joblist5)


@app.route('/paper_pending', methods=["POST"])         
def paper_pending():
    print("Hiiiiiii")
    
    quespaper_code=request.form.getlist('quespaper_code[]')
    print("queapaper:",quespaper_code)
    count=request.form.getlist('count[]')
    print("count:",count)
    remark=request.form.getlist('remark[]')
    print("remark:",remark)
    reason=request.form.getlist('reason[]')
    print("reason:",reason)
    capfaculty_id=request.form['capfaculty_id'] 
    print("capfaculty_id:",capfaculty_id)
    received_date=request.form['received_date']
    print("received_date:",received_date)
    examsession_id=request.form['examsession_id']
    print("examsession_id:",examsession_id)
    timetable_id =request.form['timetable_id']
    print("timetable_id:",timetable_id)
    submited_name=request.form['submited_name']
    print("submited_name:",submited_name)

    cursor=mysql.connection.cursor()
    print("loop")
    for paper_code, papercount, re_mark, rs in zip(quespaper_code, count, remark, reason):
        print("papercode",paper_code, papercount, re_mark, rs)
        remaining_paper = int(papercount)
        scrutany_remaining = int(papercount)
        moderation_remaining = int(papercount)
        print("remaining_paper:", remaining_paper)


        cursor.execute(f"INSERT INTO cap_project.paper_count(quespaper_code, count, remark, reason, capfaculty_id, received_date, examsession_id, timetable_id, submited_name, remaining_paper,scrutany_remaining,moderation_remaining) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (paper_code, papercount, re_mark, rs, capfaculty_id, received_date, examsession_id, timetable_id, submited_name, remaining_paper,scrutany_remaining,moderation_remaining))
        
        quespaper_code=request.form.getlist('quespaper_code[]')
        print("paperpending_id",quespaper_code)
        cursor.execute(' UPDATE cap_project.paper_count_pending SET status = 1 WHERE quespaper_code = %s',(paper_code,))
          
    mysql.connection.commit()
    cursor.close()


    return redirect('/pending')