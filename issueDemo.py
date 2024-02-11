from flask import Flask,render_template,request,redirect,url_for,jsonify
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_DB']='cap_project'
app.config['MYSQL_PASSWORD']='root'

mysql = MySQL(app)

@app.route('/')
def index():
    # Retrieve roll numbers from the StudentMaster table
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM cap_project.faculty")
    faculty = [row[1] for row in cursor.fetchall()]
    #print(type(roll_numbers))
    return render_template('isuueDemo.html', faculty=faculty)

if __name__ == '__main__':
    app.run(debug=True)