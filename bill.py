from flask import Flask,request,redirect,url_for,flash,render_template,Response,session
from flask_mysqldb import MySQL
from fpdf import FPDF
from datetime import datetime
import inflect

date=datetime.now()
app=Flask(__name__)


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='cap_project'
 
app.secret_key="stud"
mysql=MySQL(app)

@app.route('/billing')
def home():
    return render_template('bill.html')

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
        for results in result:
            print("result[11]",results[11])
        

        cursor.execute("select moderation.moderation_id,moderation.issue_date,moderation.return_date,moderation.cases,moderation.papercount_id,moderation.teacher_id,moderation.timetable_id,moderation.moderation_paper_count,moderation.from_count,moderation.to_count,time_table.year,time_table.sem,paper_count.quespaper_code,faculty.duration from moderation JOIN time_table ON moderation.timetable_id=time_table.timetable_id inner join teacher on moderation.teacher_id=teacher.teacher_id inner join paper_count on paper_count.papercount_id=moderation.papercount_id  JOIN faculty ON time_table.faculty_id = faculty.faculty_id  where teacher.teacher_name=%s and moderation.return_date is not null",(teacher_name,))
        data = cursor.fetchall()
        print("data",data)

        if len(result)<=0  and len(data)<=0:
            return redirect("/billing")
        
        
        cursor.execute("select sum(issue_check.teacher_paper_count) from issue_check  JOIN time_table ON time_table.timetable_id = issue_check.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN examsession ON time_table.examsession_id = examsession.examsession_id inner join teacher on issue_check.teacher_id=teacher.teacher_id inner join paper_count on paper_count.papercount_id=issue_check.papercount_id where teacher.teacher_name=%s and issue_check.return_date is not null",(teacher_name,))
        total = cursor.fetchone()
        if total != None:
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

 



        
        # if result[0][19]==3:
        #     rupees=total_integer * 7 
            
        # else:
        #     rupees=total_integer * 10
      
        # print("rupees",rupees)

        cursor.execute("select sum(moderation.moderation_paper_count) from moderation JOIN time_table ON moderation.timetable_id=time_table.timetable_id inner join teacher on moderation.teacher_id=teacher.teacher_id inner join paper_count on paper_count.papercount_id=moderation.papercount_id  where teacher.teacher_name=%s and moderation.return_date is not null",(teacher_name,))
        total1= cursor.fetchone()
        if total1 and len(total1) > 0:
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


        totalAssessedModerated=totalrupees+totalaccesrupees
    
        totalInWords=number_to_words(totalAssessedModerated)
        print("totalInWords",totalInWords)

        pdf = FPDF()
        pdf.add_page()
        

        pdf.image("D:\Cap-Project-master\Cap-Project-master\static\VCK LOGO PNG (1).png", x=pdf.get_x(), y=pdf.get_y(), w=40)
        page_width = pdf.w - 2 * pdf.l_margin

        pdf.ln(5)
        pdf.ln()
        pdf.set_font('Times')
        pdf.cell(page_width, 0.0, "        Shri Swami Vivekanand Shikshan Santha's",align='C')
        pdf.ln(10)
        pdf.set_font('Times', 'B', 20.0)
        pdf.cell(page_width, 0.0, "        Vivekanad College Kolhapur",align='C')
        pdf.ln(10)
        pdf.cell(page_width, 0.0, "        (Empowered Autonomous)",align='C')

        pdf.ln(10)
        pdf.set_font('Times', 'B', 15.0)
        pdf.cell(page_width, 0.0, "         Remuneration Bill Form",align='C')
        pdf.ln(8)
        pdf.set_font('Times','',11)
        col_width=page_width/4
                
        pdf.ln(1)

        th=pdf.font_size
        th=10
        i=1
        pdf.cell(col_width,th,"Bank Name",border=1)
        pdf.cell(col_width,th,"Bank A/C No",border=1)
        pdf.cell(col_width,th,"IFSC Code",border=1)
        pdf.cell(col_width,th,"Mobile No.",border=1)
               
        pdf.ln()  

        pdf.cell(col_width, th, "", border=1)
        pdf.cell(col_width, th, "", border=1)
        pdf.cell(col_width, th, "", border=1)
        pdf.cell(col_width, th, "", border=1)
        pdf.ln()  

        pdf.ln(6)
        pdf.set_font('Times', 'B', 12.0)
        # pdf.cell(page_width, 0.0, "Faculty:",align='C')
        # for results in result:
        #     pdf.cell(page_width, 0.0, str(results[11])+"/",align='C')  # Use 'results' instead of 'result[0]'
        
       
        faculty_values = "/".join(str(results[11]) for results in result)
        pdf.cell(page_width, 0.0, "Faculty:- " + faculty_values, align='C')

        
        pdf.ln(6)
        
        pdf.cell(page_width, 0.0, "Examination:",align='C')
        pdf.ln(6)
        pdf.set_font('Times')
        pdf.cell(page_width, 0.0, "To",align='L')
        pdf.ln(6)
        pdf.cell(page_width, 0.0, "Full Name:"+" "+str(teachername[0]),align='L')
        pdf.ln(6)
        # pdf.cell(page_width, 0.0, "Examiner/Moderator in the Subject:",align='L')
        # for resultt in result:
        #     pdf.cell(page_width, 0.0, (resultt[13])+(resultt[14])+"/",align='L')  # Use 'results' instead of 'result[0]'
            
       
        subject_values = "/".join(str(resultt[13]) for resultt in result)
        pdf.cell(page_width, 0.0, "Examiner/Moderator in the Subject:- " + subject_values, align='L')
        pdf.ln(6)

        # pdf.cell(page_width, 0.0, "at the class:",align='L')
        # for resultss in result:
        #     pdf.cell(page_width, 0.0, str(resultss[9])+"/",align='L')  # Use 'results' instead of 'result[0]'
            
        #     pdf.ln(10)

        class_values = "/".join(str(resultss[9]) for resultss in result)
        pdf.cell(page_width, 0.0, "at the class:-" + class_values, align='L')
        pdf.ln(6)
        # pdf.cell(page_width, 0.0, "Semester:",align='L')
        # for sem in result:
        #     pdf.cell(page_width, 0.0, str(sem[10])+"/",align='L')  # Use 'results' instead of 'result[0]'
            
        #     pdf.ln(10)

       
        sem_values = "/".join(str(sem[10]) for sem in result)
        pdf.cell(page_width, 0.0, "Semester:- " + sem_values, align='L')
        pdf.ln(6)

        # pdf.cell(page_width, 0.0, "Examination of:",align='L')
        # for exam in result:
        #     pdf.cell(page_width, 0.0, str(exam[17])+'/'+str(exam[18])+"/",align='L')  # Use 'results' instead of 'result[0]'
            
        #     pdf.ln(10)

        exam_values = "/".join(str(exam[17])+str(exam[18]) for exam in result)
        pdf.cell(page_width, 0.0, "Examination of:- " + exam_values, align='L')
        pdf.ln(6)

        pdf.cell(page_width, 0.0, "(Note-Use Separate Bill for each Subject)",align='L')
        pdf.ln(6)
        pdf.cell(page_width, 0.0, "Number of Answer Book Assessed and Moderate Summary.",align='L')
        

        

        col_width=page_width/2
        pdf.ln(8)
        th=pdf.font_size
        th=10
        i=1
        pdf.cell(149.2,th,"A-Remuneration to Examiners /Moderators",border=1)
        pdf.cell(45,th,"Rs.",border=1)
        pdf.ln()
        pdf.cell(149.2,th,"1.Examining /Moderating:",border="LRT")
        pdf.cell(45,th,"",border="TR")
        pdf.ln(5)
        pdf.cell(149.2,th,"    *Total No. of Answer Books Assessed - "+str(totalaccesrupees)+" And Moderated- "+str(totalrupees)+"@Rs--",border="LR")
        pdf.ln(5)
        pdf.cell(149.2,th,"    Assessed + Moderated: ",border="LR")
        pdf.cell(45 ,th,str(totalAssessedModerated),border="R")
        pdf.ln(8)
        pdf.cell(149.2,th,"2.Moderation Allowance:-",border="LR")
        pdf.cell(45,th,"",border="R")

        pdf.ln(8)
        pdf.cell(149.2,th,"3.Minimum Remuneration:-",border="LRB")
        pdf.cell(45,th,"",border="R")
        pdf.ln()
        pdf.cell(149.2,th,"B - Remuneration Tob Staff",border="LBR")
        pdf.cell(45,th,"",border="R")
        pdf.ln()
        pdf.cell(149.2,th,"Designation ______Rs. ______ Per Day for _____Day's",border="LBR")
        pdf.cell(45,th,"",border="RB")
        pdf.ln()
        pdf.cell(149.2,th,"Grant Total",border=1)
        pdf.cell(45,th,str(totalAssessedModerated),border=1)
        pdf.ln()
        pdf.cell(194.2,th,"Rs.(In Word) :-  "+str(totalInWords),border=1)
        pdf.ln(15)
        pdf.cell(194.2,0.0,"Full Address ",align="L")
        pdf.ln()
        pdf.cell(194.2,0.0,"I have Not Claimed This Bill Before ",align="R")
        pdf.ln(10)
        pdf.cell(194.2,0.0,"Received Payment (Singnature & Date)",align="R")
        pdf.ln(5)
        pdf.cell(194.2,0.0,"(Use One Rupee Revenue stamp If Amount Exceeds Rs.5,000/-) ",align="R")
        pdf.ln(5)
        pdf.cell(194.2,0.0," ",align="R")
        pdf.ln(18)
        pdf.cell(194.2,0.0,"Director                              Finance & Account                                    COE                                               Principal",align="L")

        pdf.ln(4)
        pdf.cell(194.2,0.0,"(CAP)                                      Officer",align="L")


        pdf.ln(4)

        pdf.set_font('Times','',12)
        col_width=page_width/7
        pdf.ln(1)
        th=pdf.font_size
        th=10
        i=1
        pdf.cell(15,th,"Sr.No",border=1)
        pdf.cell(col_width,th,"Date",border=1)
        pdf.cell(col_width,th,"Q.P.Code",border=1)
        pdf.cell(20,th,"From:",border=1)
        pdf.cell(20,th,"To:",border=1)
        pdf.cell(40,th,"No Of A.Bs Assessed",border=1)
        pdf.cell(45,th,"No Of A.Bs Moderated",border=1)
        pdf.ln(th)
        for col in result:
            pdf.cell(15,th,str(i),border=1)
            pdf.cell(col_width,th,str(col[2]),border=1)
            pdf.cell(col_width,th,col[16],border=1)
            pdf.cell(20,th,str(col[7]),border=1)
            pdf.cell(20,th,str(col[8]),border=1)
            pdf.cell(40,th,str(col[6]),border=1)
            pdf.cell(45,th,"-",border=1)
            i=i+1
            pdf.ln()

        for col_data in data:
            pdf.cell(15,th,str(i),border=1)
            pdf.cell(col_width,th,str(col_data[2]),border=1)
            pdf.cell(col_width,th,col_data[12],border=1)
            pdf.cell(20,th,str(col_data[8]),border=1)
            pdf.cell(20,th,str(col_data[9]),border=1)
            pdf.cell(40,th,"-",border=1)
            pdf.cell(45,th,str(col_data[7]),border=1)
            
            i=i+1
            pdf.ln()

        pdf.cell(109.2,th,"Total",border=1)
        pdf.cell(40,th,str(total[0]),border=1)
        pdf.cell(45,th,str(total1[0]),border=1)
        pdf.ln()
        pdf.cell(109.2,th,"*Total No .Of Answer Books Assessed And Moderated",border=1)
        pdf.cell(85,th,str(total[0]+total1[0]),border=1)
        pdf.ln(8)









        
        pdf.cell(149.2, 20)
        # pdf.ln(8)
        # pdf.cell(col_width, 0.0, "1. Examining / Moderating:")
        # pdf.ln(8)
        # pdf.cell(col_width, 0.0 ,"*Total No. of Answer Books Assessed -")
        pdf.cell(50, 20)
        pdf.ln()


            

        cursor.close()

        return Response(pdf.output(dest='s').encode('latin-1'), mimetype='', headers={'content-Disposition': 'attachment; filename=report.pdf'})
 




def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)

if __name__ =='__main__':
	app.run(debug=True)	