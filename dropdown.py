from flask import Flask, session, render_template, request,make_response,redirect,flash
from flask_mysqldb import MySQL

app=Flask(__name__)

mysql=MySQL(app)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_DB']='cap'


@app.route('/') 

def index(): 
    
    cursor =mysql.connection.cursor()
  
    cursor.execute('SELECT distinct facultyid,facultyname FROM cap.faculty') 
    
    joblist=cursor.fetchall() 
    cursor.close()
    return render_template("input.html",joblist=joblist ) 
   

   
if __name__=='__main__':
	app.run(debug=True)