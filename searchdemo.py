from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
 

# Replace these connection parameters with your database credentials
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_DB']='cap_project'
 


mysql = MySQL(app)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET": 

        cursor = mysql.connection.cursor()
        queryteacher = "SELECT teacher_name FROM teacher"
        cursor.execute(queryteacher)
        data = [row[0] for row in cursor.fetchall()]
        print(data)

        queryfaculty = "SELECT faculty FROM faculty"
        cursor.execute(queryfaculty) 
        datafaculty = [row[0] for row in cursor.fetchall()]
        print("datafaculty=",datafaculty)

        querycourse = "SELECT coursename FROM coursename"
        cursor.execute(querycourse) 
        datacourse = [row[0] for row in cursor.fetchall()]
        print("datacourse=",datacourse)

        querycourseid = "SELECT course_id FROM coursename"
        cursor.execute(querycourseid) 
        datacourseid = [row[0] for row in cursor.fetchall()]
        print("datacourseid=",datacourseid)

        return render_template("search1.html", datateacher=data,datafaculty=datafaculty,datacourse=datacourse,datacourseid=datacourseid)


@app.route("/search_subject", methods=['GET', 'POST'])
def search_subject():
    print("dffggg")
    if request.method == 'POST':
        teacher_name = request.form.get('teacher_name')
        timetable_id = request.form.get('timetable_id')
        papercount_id = request.form.get('papercount_id')
        teacher_id = request.form.get('teacher_id')
        
        cursor = mysql.connection.cursor()

         
        query=" SELECT faculty.faculty,teacher.year,teacher.sem,subject.subject,coursename.coursename,coursename.course_id,paper_count.count,paper_count.quespaper_code,time_table.timetable_id,teacher.teacher_id,paper_count.papercount_id,paper_count.remaining_paper FROM teacher INNER JOIN faculty ON teacher.faculty_id = faculty.faculty_id INNER JOIN subject ON teacher.subject_id = subject.subject_id INNER JOIN coursename ON teacher.coursename_id = coursename.coursename_id INNER JOIN time_table ON time_table.coursename_id = teacher.coursename_id INNER JOIN paper_count ON time_table.timetable_id = paper_count.timetable_id WHERE teacher.teacher_name = %s"
        cursor.execute(query, (teacher_name,))
        result = cursor.fetchall()
        print(result)

        cursor.close()
        return render_template("search1.html",  result=result, papercount_id=papercount_id, teacher_id=teacher_id, timetable_id=timetable_id)
    
    else:
        return render_template("search1.html")
        
@app.route('/paper_issue', methods=["POST"])         
def paper_issue(): 
    issue_date = request.form.getlist('issue_date[]')
    print("issue_date=",issue_date)
    return_date = request.form.getlist('return_date[]')
    print("return_date=",return_date)
    papercount_id = request.form['papercount_id']
    print("papercount_id=",papercount_id)
    teacher_id = request.form['teacher_id'] 
    print("teacher_id=",teacher_id)
    teacher_paper_count = request.form.getlist('teacher_paper_count[]')
    print("teacher_paper_count=",teacher_paper_count)
    timetable_id = request.form['timetable_id']
    print("timetable_id=",timetable_id)

    cur = mysql.connection.cursor()
    
    
    for issuedate, returndate, papercountid, teacherid, papercount, timetableid in zip(issue_date, return_date, papercount_id, teacher_id, teacher_paper_count, timetable_id):
        papercountid = int(papercountid) if papercountid.strip() else None
        timetableid = int(timetableid) if timetableid.strip() else None
        if not papercountid:
            # Provide a default value or skip inserting it based on your application's requirements
            continue  # Skip inserting this record
        else:
            teacher_paper_count = request.form.get('teacher_paper_count')
            papercount_id = request.form.get('papercount_id')
            cur.execute(' UPDATE paper_count SET remaining_paper = remaining_paper - %s WHERE papercount_id = %s',(papercount,papercount_id,))
            cur.execute("INSERT INTO issue_check (issue_date, return_date, papercount_id, teacher_id, teacher_paper_count, timetable_id) VALUES (%s, %s, %s, %s, %s, %s)", (issuedate, returndate, papercountid, teacherid, papercount, timetableid))
            mysql.connection.commit()
        
    cur.close()

    return redirect('/search_subject')

if __name__ == "__main__":
    app.run(debug=True)