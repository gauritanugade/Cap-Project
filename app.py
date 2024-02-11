from flask import Flask,Blueprint, render_template
from flask_mysqldb import MySQL
from main import main_app

from add_course import add_course
from add_faculty import add_faculty
from add_pattern import add_pattern
from add_teacher_details import add_teacher_details
from add_subject import add_subject
from add_examsession import add_examsession
from timetable import timetable
from timetable_display import timetable_display
from capfaculty import capfaculty
from paper_register import paper_register
from paper_issue1 import paper_issue1
from login import login
from scrutany import scrutany
from moderation import moderation
from remuneration import remuneration
from receive_paper import receive_paper
from scrutany_receive_paper import scrutany_receive_paper
from moderation_receive_paper import moderation_receive_paper
from report import report


app = Flask(__name__)
app.secret_key='project'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_DB']='cap_project'
app.secret_key = 'VCK'
 

app.register_blueprint(main_app)

app.register_blueprint(add_course)
app.register_blueprint(add_faculty)
app.register_blueprint(add_pattern)
app.register_blueprint(add_teacher_details)
app.register_blueprint(add_subject)
app.register_blueprint(add_examsession)
app.register_blueprint(timetable)
app.register_blueprint(timetable_display)
app.register_blueprint(capfaculty)
app.register_blueprint(paper_register)
app.register_blueprint(paper_issue1)

app.register_blueprint(login)
app.register_blueprint(scrutany)
app.register_blueprint(moderation)
app.register_blueprint(remuneration)
app.register_blueprint(receive_paper)
app.register_blueprint(scrutany_receive_paper)
app.register_blueprint(moderation_receive_paper)
app.register_blueprint(report)



 


mysql = MySQL(app)

if __name__== '__main__':
    app.run(debug=True)
