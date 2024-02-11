from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
from flask_mysqldb import MySQL

login = Blueprint('login', __name__, template_folder='templates')
app = login

mysql = MySQL()

@app.route('/login_page', methods =['GET', 'POST'])
def home():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor()
		cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password, ))
		account = cursor.fetchone()
		print(account[1])
		if account[1]=='vck@123':
			
			return redirect(url_for("main_app.adminPage"))
		
		elif account[1]=='cap@123':
			
			return redirect(url_for("main_app.capfacultypage"))
		
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('main_app.homepage'))

