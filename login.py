from flask import Flask, render_template, request, redirect, url_for, session, Blueprint,flash
from flask_mysqldb import MySQL

login = Blueprint('login', __name__, template_folder='templates')
app = login

mysql = MySQL()

@app.route('/login')
def home():
	return render_template("loginboth.html")

@app.route('/adoption')
def adoption():
	return render_template('adminlogin.html')

@app.route('/adminlogin', methods =['GET', 'POST'])
def ladogin():
		msg = ''
		if request.method == 'POST' and 'userName' in request.form and 'password' in request.form:
			userName = request.form['userName']
			password = request.form['password']
			cur = mysql.connection.cursor()
			cur.execute('SELECT * FROM cap_project.accounts WHERE username = %s AND password = %s', (userName, password ))
			account = cur.fetchone()
			print(account)
			if account:
				#session['loggedin'] = True
				session['userName'] = account[0]
				session['password'] = account[1]
				msg = 'Logged in successfully !'
				return redirect(url_for("main_app.adminPage"))
			else:
				msg = 'Incorrect username / password !'
			return render_template('adminlogin.html', msg = msg)
		
# @app.route('/eg')
# def capmember():
# 	return render_template('capmemberlogin.html')

# @app.route('/caplogin', methods =['GET', 'POST'])
# def caplogin():
# 		print("hiiiiiiiiiiiiii")
# 		msg = ''
# 		if request.method == 'POST' and 'userName' in request.form and 'password' in request.form:
# 			userName = request.form['userName']
# 			password = request.form['password']
# 			cur = mysql.connection.cursor()
# 			cur.execute('SELECT * FROM cap_project.accounts WHERE username = %s AND password = %s', (userName, password ))
# 			account = cur.fetchone()
# 			print(account)
# 			if account:
# 				#session['loggedin'] = True
# 				session['userName'] = account[0]
# 				session['password'] = account[1]
# 				msg = 'Logged in successfully !'
# 				return redirect(url_for("main_app.capfacultypage"))
# 			else:
# 				msg = 'Incorrect username / password !'
# 			return render_template('capmemberlogin.html', msg = msg)
		
#################################################################################################
@app.route('/eg')
def eg():
	return render_template('capmemberlogin.html')

#########################################################################################
@app.route('/caplogin', methods =['GET', 'POST'])
def loginn():
	msg = ''
	if request.method == 'POST' and 'userid' in request.form and 'pass1' in request.form:
		userid = request.form['userid']
		pass1 = request.form['pass1']
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM cap_project.accounts WHERE username = %s AND password = %s', (userid, pass1 ))
		student = cur.fetchone()
		print(student)
		if student:
			#session['loggedin'] = True
			session['userid'] = student[0]
			session['pass1'] = student[1]
			msg = 'Logged in successfully !'
			return redirect(url_for("main_app.capfacultypage"))
		else:
			msg = 'Incorrect username / password !'
		return render_template('capmemberlogin.html', msg = msg)
	return redirect(url_for("main_app.capfacultypage"))
# @app.route('/login_page', methods=['GET', 'POST'])
# def home():
#     msg = ''

#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         cursor = mysql.connection.cursor()
#         cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
#         account = cursor.fetchone()

#         if account:
#             if account[1] == 'vck@123':
#                 flash('Login successful for admin!')
#                 return redirect(url_for("main_app.adminPage"))
#             elif account[1] == 'cap@123':
#                 flash('Login successful for cap!')
#                 return redirect(url_for("main_app.capfacultypage"))
#             else:
#                 msg = 'Incorrect password!'
        

#     return render_template('homepage1.html', msg=msg)


@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('main_app.homepage'))

