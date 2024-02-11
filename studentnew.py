from flask import Flask, render_template
from flask_mysqldb import MySQL
#from flask_mysql_connector import MySQL

app=Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DATABASE'] = 'tysbc'
app.config['MYSQL_HOST'] = 'localhost'

mysql=MySQL(app)

query="select * from tybsc.studentnew"

@app.route('/')
def inserttable():
	cursor=mysql.connection.cursor()
	cursor.execute(query)
	data =cursor.fetchall()
	cursor.close()
	print(data)
	return render_template('studentnew.html',student=data)


if __name__ =='__main__':
	app.run(debug=True)
