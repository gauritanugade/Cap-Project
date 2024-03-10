from flask import Flask, Blueprint, render_template, request, jsonify, redirect
from flask_mysqldb import MySQL


remuneration = Blueprint('remuneration', __name__, template_folder='templates')

app = remuneration

mysql = MySQL()


displayall = "select exam_year,month,degree from cap_project.examsession"


@app.route('/remuneration')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute(
        'SELECT month,exam_year,examsession_id FROM cap_project.examsession')
    joblist = cursor.fetchall()
    print("list:", joblist)

    cursor.execute(
        'SELECT faculty,faculty_id FROM cap_project.faculty')
    joblist1 = cursor.fetchall()
    print("list1:", joblist1)

    return render_template("remuneration.html", joblist=joblist,joblist1=joblist1)


@app.route('/remunerationdata', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        Examsession_id = request.form["Examsession_id"]
        print("Examsession_id:",Examsession_id)

        degree = request.form["degree"]
        print("degree:",degree)

        faculty_id = request.form["faculty_id"]
        print("faculty_id:",faculty_id)


        slab = request.form.getlist("slab")
        print("slab:",slab)

        lowerlimit = request.form.getlist("lowerlimit")
        print("lowerlimit:",lowerlimit)

        upperlimit = request.form.getlist("upperlimit")
        print("upperlimit:",upperlimit)

        rupees = request.form.getlist("rupees")
        print("rupees:",rupees)

        perpaper_rs = request.form["perpaper_rs"]
        print("perpaper_rs:",perpaper_rs)

        for(sl,lower_limit,upper_limit,rs) in zip(slab,lowerlimit,upperlimit,rupees):

            cursor = mysql.connection.cursor()

            cursor.execute("insert into cap_project.remuneration (examsession_id,degree,slab,lowerlimit,upperlimit,rupees,faculty_id) values (%s,%s,%s,%s,%s,%s,%s)",(Examsession_id,degree,sl,lower_limit,upper_limit,rs,faculty_id))
            remuneration_id = cursor.lastrowid
            cursor.execute("insert into cap_project.remu_perpaper (examsession_id,degree,perpaper_rs,remuneration_id,faculty_id) values (%s,%s,%s,%s,%s)",(Examsession_id,degree,perpaper_rs,remuneration_id,faculty_id))
            mysql.connection.commit()
            cursor.execute(displayall)
            data = cursor.fetchall()
            print("data:",data)
            cursor.close()
        return render_template("remuneration.html")