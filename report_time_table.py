from flask import Flask, request, render_template, Response, session,Blueprint
from flask_mysqldb import MySQL
from fpdf import FPDF
from datetime import datetime


report_time_table = Blueprint('report_time_table', __name__, template_folder='templates')

app = report_time_table

mysql = MySQL()

@app.route('/reporttimetable')
def home():
    return render_template('report_timetable.html')

@app.route('/download/reports/pdfs', methods=["POST"])
def download_reports():
    if request.method == "POST":
        date = request.form['date']  # Get the selected date string from the form
        date = datetime.strptime(date, '%Y-%m-%d')  # Convert string to datetime object
  
        cursor = mysql.connection.cursor()
        cursor.execute("select cap_project.time_table.date,cap_project.time_table.starttime,time_table.endtime,coursename.course_id,coursename.coursename,faculty.faculty,time_table.year,time_table.sem,examsession.month,examsession.exam_year,pattern.pattern from time_table inner join cap_project.coursename on time_table.coursename_id=cap_project.coursename.coursename_id inner join cap_project.examsession  on cap_project.time_table.examsession_id=cap_project.examsession.examsession_id inner join cap_project.faculty on time_table.faculty_id=faculty.faculty_id inner join pattern on examsession.pattern_id=pattern.pattern_id where time_table.date=%s;",
            (date,))
        result = cursor.fetchall()        
        print("Result",result)

        if result[0][6]==1:
            yearRom = "I"
        elif result[0][6] ==2:
            yearRom = "II"
        elif result[0][6] ==3:
            yearRom = "III"
        elif result[0][6] == 4:
            yearRom = "IV"
        else:
            yearRom = ""

        print("yearRom",yearRom)
            
        

        pdf = FPDF()
        pdf.add_page()

        page_width = pdf.w - 2 * pdf.l_margin
        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, "TimeTable Report", align='C')
        
        page_width = pdf.w - 2 * pdf.l_margin
        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, "Vivekanand College,kolhapur", align='C')
        
        


        current_date = datetime.now()
        
        pdf.ln(10)
        pdf.set_font('Times', 'B', 12.0)
        pdf.cell(page_width, 0.0, 'Date:- ' + current_date.strftime('%Y-%m-%d'), align='L')


        pdf.ln(10)
        pdf.set_font('courier', '', 12)
        col_width = page_width / 8
        pdf.ln(1)

        th = pdf.font_size
        i = 1
        pdf.cell(col_width, th, "Sr_No", border=1)
        pdf.cell(col_width, th, "Starttime", border=1)
        pdf.cell(col_width, th, "Endtime", border=1)
        pdf.cell(col_width, th, "course_id", border=1)
        pdf.cell(col_width, th, "coursename", border=1)
        pdf.cell(col_width, th, "Faculty", border=1)
        pdf.cell(col_width, th, "year", border=1)
        pdf.cell(col_width, th, "Sem", border=1)
     

        pdf.ln(th)
        for col in result:
            pdf.cell(col_width, th, str(i), border=1)
            pdf.cell(col_width, th, str(col[1]), border=1)
            pdf.cell(col_width, th, str(col[2]), border=1)
            pdf.cell(col_width, th, str(col[3]), border=1)  
            pdf.cell(col_width, th, str(col[4]), border=1)  
            pdf.cell(col_width, th, str(col[5]), border=1)  
            pdf.cell(col_width, th, str(yearRom), border=1)  
            pdf.cell(col_width, th, str(col[7]), border=1)  

            i = i + 1
            pdf.ln(th)

        pdf.ln(10)

        pdf.set_font('Times', '', 10.0)
        pdf.cell(page_width, 0.0, '-end of report -', align='C')
        cursor.close()

        return Response(pdf.output(dest='s').encode('latin-1'), mimetype='', headers={'content-Disposition': 'attachment; filename=report.pdf'})