from flask import Flask,Blueprint,render_template,request,session,make_response,redirect,flash,Response
from flask_mysqldb import MySQL
from fpdf import FPDF
from datetime import datetime
import inflect

date = datetime.now()


Billing = Blueprint('Billing', __name__, template_folder='templates')

app=Billing

mysql=MySQL()

@app.route('/billing')
def home():
    return render_template('billing.html')

@app.route('/download/report/bill', methods=["POST"])
def generate_bill():
    if request.method == "POST":
        session['teacher_name'] = request.form['teacher_name']
        teacher_name = session['teacher_name']

        cursor = mysql.connection.cursor()
        cursor.execute("select teacher_name from teacher where teacher.teacher_name=%s",(teacher_name,))
        teachername = cursor.fetchone()
        print("teachername",teachername)


        cursor.execute("select issue_check.issue_check_id,issue_check.issue_date,issue_check.return_date,issue_check.papercount_id,issue_check.teacher_id,issue_check.timetable_id,issue_check.teacher_paper_count,issue_check.from_count,issue_check.to_count,time_table.year,time_table.sem,faculty.faculty,subject.subject,coursename.coursename,coursename.course_id,teacher.teacher_name,paper_count.quespaper_code,examsession.month,examsession.exam_year,faculty.duration from issue_check  JOIN time_table ON time_table.timetable_id = issue_check.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN examsession ON time_table.examsession_id = examsession.examsession_id inner join teacher on issue_check.teacher_id=teacher.teacher_id inner join paper_count on paper_count.papercount_id=issue_check.papercount_id where teacher.teacher_name=%s and issue_check.return_date is not null",(teacher_name,))
        result = cursor.fetchall()
        print("result",result)
        

        cursor.execute("select moderation.moderation_id,moderation.issue_date,moderation.return_date,moderation.cases,moderation.papercount_id,moderation.teacher_id,moderation.timetable_id,moderation.moderation_paper_count,moderation.from_count,moderation.to_count,time_table.year,time_table.sem,paper_count.quespaper_code,faculty.duration from moderation JOIN time_table ON moderation.timetable_id=time_table.timetable_id inner join teacher on moderation.teacher_id=teacher.teacher_id inner join paper_count on paper_count.papercount_id=moderation.papercount_id  JOIN faculty ON time_table.faculty_id = faculty.faculty_id  where teacher.teacher_name=%s and moderation.return_date is not null",(teacher_name,))
        data = cursor.fetchall()
        print("data",data)

        # if len(result)<=0  and len(data)<=0:
        #     return redirect("/billing")
        
        
        cursor.execute("select sum(issue_check.teacher_paper_count) from issue_check  JOIN time_table ON time_table.timetable_id = issue_check.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN examsession ON time_table.examsession_id = examsession.examsession_id inner join teacher on issue_check.teacher_id=teacher.teacher_id inner join paper_count on paper_count.papercount_id=issue_check.papercount_id where teacher.teacher_name=%s and issue_check.return_date is not null",(teacher_name,))
        total = cursor.fetchone()
        try:
            if total != None and len(total)>0:
                total_integer = int(total[0])
                print("Total:", total_integer)

                cursor.execute('select rupees from remuneration where %s>=lowerlimit and %s<=upperlimit limit 1',(total_integer,total_integer))
                assesrupees = cursor.fetchone()
                print("assesrupees",assesrupees)
                if assesrupees==None:
                    assesrupees=total_integer*7
                    
                else:
                    assesrupees = assesrupees[0]
                print("assesrupees",assesrupees)

                
                totalaccesrupees=assesrupees
                print("totalaccesrupees",totalaccesrupees)
            else:
                print("No data found.")

            print("total",total)
        except:
            total_integer = 0
            totalaccesrupees = 0
            print("error")


        cursor.execute("select sum(moderation.moderation_paper_count) from moderation JOIN time_table ON moderation.timetable_id=time_table.timetable_id inner join teacher on moderation.teacher_id=teacher.teacher_id inner join paper_count on paper_count.papercount_id=moderation.papercount_id  where teacher.teacher_name=%s and moderation.return_date is not null",(teacher_name,))
        total1= cursor.fetchone()
        print("total1:", total1)
        try:
            if total1 != None and len(total1) > 0:
                total_integer1 = int(total1[0])
                print("Total1:", total_integer1)

                cursor.execute('select rupees from remuneration where %s>=lowerlimit and %s<=upperlimit limit 1',(total_integer1,total_integer1))
                modrupees = cursor.fetchone()
                print("modrupees",modrupees)
                if modrupees==None:
                    modrupees=total_integer1*7
                    
                else:
                    modrupees = modrupees[0]
                print("modrupees",modrupees)

                
                totalrupees=modrupees
                print("totalrupees",totalrupees)    
            else:
                print("No data found.")

            print("total1",total1)
        except:
            total_integer1 = 0
            totalrupees = 0
            print("error")


        totalAssessedModerated=totalrupees+totalaccesrupees
    
        totalInWords=number_to_words(totalAssessedModerated)
        print("totalInWords",totalInWords)

        pdf = FPDF()
        pdf.add_page()

 



        return render_template("billing_form.html",teachername=teachername[0],result=result,data=data,total= total_integer,total1= total_integer1,totalrupees=totalrupees,totalaccesrupees=totalaccesrupees,totalAssessedModerated=totalAssessedModerated,totalInWords=totalInWords)

def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)


