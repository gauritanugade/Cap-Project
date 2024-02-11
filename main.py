from flask import Blueprint, render_template
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

main_app = Blueprint('main_app', __name__, template_folder='templates')

mysql = MySQL()

@main_app.route('/admin')
def adminPage():
   

    return render_template('homepage.html')

@main_app.route('/capfaculty')
def capfacultypage():
    return render_template('capfacultypage.html')

@main_app.route('/')
def homepage():
    
    return render_template('homepage1.html')
