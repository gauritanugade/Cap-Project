from flask import Flask,Blueprint,render_template,request,session,make_response,redirect,flash,Response,url_for
from flask_mysqldb import MySQL
from fpdf import FPDF
from datetime import datetime
import inflect
from os.path import join, dirname, realpath

date = datetime.now()


scrutanybilling = Blueprint('scrutanybilling', __name__, template_folder='templates')

app=scrutanybilling

mysql=MySQL()

@app.route('/scrutany')
def home():
    return render_template('scrutanybilling1.html')

@app.route('/download/report/scrutanybill', methods=["POST"])
def generatescrutany_bill():
    if request.method == "POST":
        session['name'] = request.form['name']
        name = session['name']

        cursor = mysql.connection.cursor()
        cursor.execute("select name from cap_faculty where cap_faculty.name=%s",(name,))
        capfacname = cursor.fetchone()
        print("capfacname",capfacname)


        # cursor.execute(" select scrutany.scrutany_id,scrutany.issue_date,scrutany.return_date,scrutany.papercount_id,scrutany.capfaculty_id,scrutany.timetable_id,scrutany.scrutany_paper_count,scrutany.from_count,scrutany.to_count,time_table.year,time_table.sem,faculty.faculty,subject.subject,coursename.coursename,coursename.course_id,cap_faculty.name,paper_count.quespaper_code,examsession.month,examsession.exam_year from scrutany JOIN time_table ON time_table.timetable_id = scrutany.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN examsession ON time_table.examsession_id = examsession.examsession_id inner join cap_faculty on cap_faculty.capfaculty_id=scrutany.capfaculty_id inner join paper_count on paper_count.papercount_id=scrutany.papercount_id where cap_faculty.name=%s and scrutany.return_date is not null;",(name,))
        # result = cursor.fetchall()
        # print("result",result)
        
        cursor.execute("select scrutany.scrutany_id,scrutany.issue_date,scrutany.return_date,scrutany.papercount_id,scrutany.capfaculty_id,scrutany.timetable_id,scrutany.scrutany_paper_count,scrutany.from_count,scrutany.to_count,time_table.year,time_table.sem,faculty.faculty,subject.subject,coursename.coursename,coursename.course_id,cap_faculty.name,paper_count.quespaper_code,examsession.month,examsession.exam_year, DATEDIFF(return_date,issue_date) AS 'Days difference' from scrutany JOIN time_table ON time_table.timetable_id = scrutany.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id JOIN examsession ON time_table.examsession_id = examsession.examsession_id inner join cap_faculty on cap_faculty.capfaculty_id=scrutany.capfaculty_id inner join paper_count on paper_count.papercount_id=scrutany.papercount_id where cap_faculty.name=%s and scrutany.return_date is not null",(name,))
        query = cursor.fetchall()
        print("results",query)

        if len(query)<=0:
            return redirect("/scrutany")
        
        Differnceday=0
        days=0
        for result in query:
            Differnceday=result[19]
            print("Differnceday",Differnceday)
            if result != None:
                days= int(Differnceday)+days
                print("days:", days)

                cursor.execute('select scrutanyremuneration.rupees,cap_faculty.name,cap_faculty.designation from scrutanyremuneration inner join cap_faculty on cap_faculty.capfaculty_id=scrutanyremuneration.capfaculty_id where cap_faculty.name=%s',(name,))
                scrutanyrupees = cursor.fetchone()
                print("scrutanyrupees",scrutanyrupees)
                if scrutanyrupees!=None:
                    scrutanytotal=days*scrutanyrupees[0]
                    print("scrutanytotal",scrutanytotal)
                else:
                    print("No data found.")

            
            
            else:
                print("No data found.")
 


        scrutanytotalInWords=number_to_words(scrutanytotal)
        print("scrutanytotalInWords",scrutanytotalInWords)

        pdf = FPDF()
        pdf.add_page()
        
        path = join(dirname(realpath(__file__)), 'static/vck_logo.png')
        print("path=", path)

        pdf.image(path, x=pdf.get_x(), y=pdf.get_y(), w=40)
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
        
       
        # faculty_values = "/".join(all)
        pdf.cell(page_width, 0.0, "Faculty:- " + '(All)', align='C')

        
        pdf.ln(6)
        
        pdf.cell(page_width, 0.0, "Examination:",align='C')
        pdf.ln(6)
        pdf.set_font('Times')
        pdf.cell(page_width, 0.0, "To",align='L')
        pdf.ln(6)
        pdf.cell(page_width, 0.0, "Full Name:"+" "+str(name),align='L')
        pdf.ln(6)
        # pdf.cell(page_width, 0.0, "Examiner/Moderator in the Subject:",align='L')
        # for resultt in result:
        #     pdf.cell(page_width, 0.0, (resultt[13])+(resultt[14])+"/",align='L')  # Use 'results' instead of 'result[0]'
            
       
        # subject_values = "/".join(str(resultt[13]) for resultt in result)
        pdf.cell(page_width, 0.0, "Examiner/Moderator in the Subject:- " + '(All)', align='L')
        pdf.ln(6)

        # pdf.cell(page_width, 0.0, "at the class:",align='L')
        # for resultss in result:
        #     pdf.cell(page_width, 0.0, str(resultss[9])+"/",align='L')  # Use 'results' instead of 'result[0]'
            
        #     pdf.ln(10)

        # class_values = "/".join(str(resultss[9]) for resultss in result)
        pdf.cell(page_width, 0.0, "at the class:-" + '(All)', align='L')
        pdf.ln(6)
        # pdf.cell(page_width, 0.0, "Semester:",align='L')
        # for sem in result:
        #     pdf.cell(page_width, 0.0, str(sem[10])+"/",align='L')  # Use 'results' instead of 'result[0]'
            
        #     pdf.ln(10)

       
        # sem_values = "/".join(str(sem[10]) for sem in result)
        pdf.cell(page_width, 0.0, "Semester:- " + '(All)', align='L')
        pdf.ln(6)

        # pdf.cell(page_width, 0.0, "Examination of:",align='L')
        # for exam in result:
        #     pdf.cell(page_width, 0.0, str(exam[17])+'/'+str(exam[18])+"/",align='L')  # Use 'results' instead of 'result[0]'
            
        #     pdf.ln(10)

        exam_values = "/".join(str(exam[17])+str(exam[18]) for exam in query)
        pdf.cell(page_width, 0.0, "Examination of:- ",exam_values, align='L')
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
        pdf.cell(149.2,th,"    *Total No. of Answer Books Assessed -  And Moderated @Rs--",border="LR")
        pdf.ln(5)
        pdf.cell(149.2,th,"    Assessed + Moderated: ",border="LR")
        pdf.cell(45 ,th,border="R")
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
        pdf.cell(149.2,th,"Designation"+str(scrutanyrupees[2])+ "Rs. "+str(scrutanyrupees[0])+" Per Day for  "+str(days)+"Day's  ",border="LBR")
        pdf.cell(45 ,th,str(scrutanytotal),border="R")

        #pdf.cell(45,th,"",border="RB")
        pdf.ln()
        pdf.cell(149.2,th,"Grant Total",border=1)
        pdf.cell(45,th,str(scrutanytotal),border=1)

        pdf.cell(45,th,border=1)
        pdf.ln()
        pdf.cell(194.2,th,"Rs.(In Word) :-  "+str(scrutanytotalInWords),border=1)
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

       


            

        cursor.close()

        return Response(pdf.output(dest='s').encode('latin-1'), mimetype='', headers={'content-Disposition': 'attachment; filename=report.pdf'})
 





def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)


 



        #return render_template("srutanybilling_form.html",name=name,result=result,days= days,scrutanyrupees=scrutanyrupees,scrutanytotal=scrutanytotal,scrutanytotalInWords=scrutanytotalInWords)

def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)


       

