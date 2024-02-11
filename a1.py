from flask import Flask, render_template, request, jsonify, redirect,url_for,session
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_DB']='cap_project'
app.config['MYSQL_PASSWORD']='root'
app.secret_key = 'VCK'
 
 


mysql = MySQL(app)




@app.route("/scrutany")
def secu():
    return render_template("scrutany.html")


@app.route("/scrutanybuttion", methods=["POST", "GET"])
def scrutanybuttion():
    if request.method == "POST": 
        cursor = mysql.connection.cursor()
        query= "SELECT paper_count.quespaper_code, paper_count.count, time_table.year, time_table.sem, subject.subject, coursename.coursename, coursename.course_id, faculty.faculty,paper_count.papercount_id,time_table.timetable_id,paper_count.scrutany_remaining FROM paper_count JOIN time_table  ON paper_count.timetable_id = time_table.timetable_id JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id"
       
        cursor.execute(query) 
        result = cursor.fetchall()
        print("result:",result)
        cursor.execute('SELECT name,capfaculty_id FROM cap_project.cap_faculty where designation="Scrutiny Clerk"') 
        joblist1=cursor.fetchall()
        cursor.close()

        return render_template("a1.html",result=result,joblist1=joblist1)
    
    else:
        return render_template("a1.html")
    
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


if __name__== '__main__':
    app.run(debug=True)