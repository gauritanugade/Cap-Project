from flask import Flask, Blueprint, render_template, request, jsonify, redirect
from flask_mysqldb import MySQL


scrutanyremuneration = Blueprint('scrutanyremuneration', __name__, template_folder='templates')

app = scrutanyremuneration

mysql = MySQL()


displayall = "select exam_year,month,degree from cap_project.examsession"


@app.route('/scrutanyremuneration')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute(
        'SELECT month,exam_year,examsession_id FROM cap_project.examsession')
    joblist = cursor.fetchall()
    print("list:", joblist)
    
    cursor.execute(
        'select designation,capfaculty_id from cap_project.cap_faculty')
    joblist1 = cursor.fetchall()
    print("list:", joblist1)

    return render_template("scrutanyremuneration.html", joblist=joblist,joblist1=joblist1)




@app.route('/scrutanyremunerationdata', methods=['POST', 'GET'])
def scrutanyremunerationdata():
    if request.method == 'POST':
        rupees = request.form.getlist("rupees")
        print("rupees:",rupees)
        
        capfaculty_id = request.form["capfaculty_id"]
        print("capfaculty_id:",capfaculty_id)
        
        examsession_id = request.form["examsession_id"]
        print("examsession_id:",examsession_id)
        
        

        for(rs) in zip(rupees):

            cursor = mysql.connection.cursor()

            cursor.execute("insert into cap_project.scrutanyremuneration (rupees,capfaculty_id,examsession_id) values (%s,%s,%s)",(rs,capfaculty_id,examsession_id))
            mysql.connection.commit()
            cursor.execute(displayall)
            data = cursor.fetchall()
            print("data:",data)
            cursor.close()
        return render_template("scrutanyremuneration.html")