from flask import Flask, request, render_template 
from flask_mysqldb import MySQL

app = Flask(__name__)

# Your database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'cap_project'
 

 

mysql = MySQL(app)

@app.route("/", methods=["POST", "GET"]) 
def database(): 
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
        
        return render_template("searchitem1.html", datateacher=data,datafaculty=datafaculty,datacourse=datacourse,datacourseid=datacourseid)

if __name__ == '__main__': 
    app.run(debug=True)