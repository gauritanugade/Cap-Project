from flask import Flask, request, render_template, Response, session, Blueprint
from flask_mysqldb import MySQL
from fpdf import FPDF
from datetime import datetime


report_okpending = Blueprint(
    'report_okpending', __name__, template_folder='templates')

app = report_okpending

mysql = MySQL()


@app.route('/report_okpending')
def home():
    return render_template('report_okpending.html')


@app.route('/download/reportss/pdfs_okpending', methods=["POST"])
def download_reports_okpending():
    if request.method == "POST":
        # Get the selected date string from the form
        received_date = request.form['received_date']
        # Convert string to datetime object
        received_date = datetime.strptime(received_date, '%Y-%m-%d')

        cursor = mysql.connection.cursor()
        cursor.execute(" select faculty.faculty, subject.subject , coursename.course_id,coursename.coursename,time_table.year,time_table.sem,quespaper_code,count,remark,reason,received_date  from paper_count JOIN time_table ON time_table.timetable_id = paper_count.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id where received_date=%s",
                    (received_date,))
        result = cursor.fetchall()
        print("REsult_ok", result)
        cursor = mysql.connection.cursor()
        cursor.execute("select faculty.faculty, subject.subject , coursename.course_id,coursename.coursename,time_table.year,time_table.sem,quespaper_code,count,remark,reason,received_date  from paper_count_pending JOIN time_table ON time_table.timetable_id = paper_count_pending.timetable_id JOIN faculty ON time_table.faculty_id = faculty.faculty_id  JOIN subject ON time_table.subject_id = subject.subject_id JOIN coursename ON time_table.coursename_id = coursename.coursename_id where received_date=%s",
                       (received_date,))
        result1 = cursor.fetchall()
        print("REsult_pending", result1)

        try:
            if result[0][4] == 1:
                yearRom = "I"
            elif result[0][4] == 2:
                yearRom = "II"
            elif result[0][4] == 3:
                yearRom = "III"
            elif result[0][4] == 4:
                yearRom = "IV"
            else:
                yearRom = ""
            print("yearRom", yearRom)
        except:
            yearRom = ""
            print("year rom error")

        try:
            if result[0][5] == 1:
                semRom = "I"
            elif result[0][5] == 2:
                semRom = "II"
            elif result[0][5] == 3:
                semRom = "III"
            elif result[0][5] == 4:
                semRom = "IV"
            elif result[0][5] == 5:
                semRom = "V"
            elif result[0][5] == 6:
                semRom = "VI"
            else:
                semRom = ""
            print("semRom", semRom)
        except:
            semRom = ""
            print("semRom error")

        try:
            if result1[0][4] == 1:
                yearRom = "I"
            elif result1[0][4] == 2:
                yearRom = "II"
            elif result1[0][4] == 3:
                yearRom = "III"
            elif result1[0][4] == 4:
                yearRom = "IV"
            else:
                yearRom = ""
            print("yearRom", yearRom)
        except:
            yearRom = ""
            print("yearRom2 error")  

        try:
            if result1[0][5] == 1:
                semRom = "I"
            elif result1[0][5] == 2:
                semRom = "II"
            elif result1[0][5] == 3:
                semRom = "III"
            elif result1[0][5] == 4:
                semRom = "IV"
            elif result1[0][5] == 5:
                semRom = "V"
            elif result1[0][5] == 6:
                semRom = "VI"
            else:
                semRom = ""
            print("semRom", semRom)
        except:
            semRom = ""
            print("semRom error")


        combined_result = result + result1

        pdf = FPDF()
        pdf.add_page('A3')

        page_width = pdf.w
        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, "Ok_Pending Report", align='C')

        page_width = pdf.w
        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, "Vivekanand College,kolhapur", align='C')

        current_date = datetime.now()

        pdf.ln(10)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(page_width, 0.0, 'Date:- ' +
                 current_date.strftime('%Y-%m-%d'), align='L')

        pdf.ln(10)
        pdf.set_font('courier', '', 10)
        col_width = page_width / 17
        pdf.ln(1)

        th = pdf.font_size
        i = 1

        pdf.cell(10, th, "Sr", border=1)
        pdf.cell(col_width, th, "faculty", border=1)
        pdf.cell(col_width*2.5, th, "subject", border=1)
        pdf.cell(col_width*1.5, th, "course_id", border=1)
        pdf.cell(col_width*3.8, th, "coursename", border=1)
        pdf.cell(12, th, "year", border=1)
        pdf.cell(12, th, "sem", border=1)
        pdf.cell(col_width*1.7, th, "Q.Paper code", border=1)
        pdf.cell(col_width, th, "count", border=1)
        pdf.cell(col_width, th, "remark", border=1)
        pdf.cell(col_width*1.7, th, "received_date", border=1)

        pdf.ln(th)
        for col in combined_result:
            pdf.cell(10, th, str(i), border=1)
            pdf.cell(col_width, th, str(col[0]), border=1)
            pdf.cell(col_width*2.5, th, str(col[1]), border=1)
            pdf.cell(col_width*1.5, th, str(col[2]), border=1)
            pdf.cell(col_width*3.8, th, str(col[3]), border=1)
            pdf.cell(12, th, str((yearRom)), border=1)
            pdf.cell(12, th, str((semRom)), border=1)
            pdf.cell(col_width*1.7, th, str(col[6]), border=1)
            pdf.cell(col_width, th, str(col[7]), border=1)
            pdf.cell(col_width, th, str(col[8]), border=1)
            pdf.cell(col_width*1.7, th, str(col[10]), border=1)

            i = i + 1
            pdf.ln(th)

        pdf.ln(10)

        pdf.set_font('Times', '', 11.0)
        pdf.cell(page_width, 0.0, '-end of report -', align='C')
        cursor.close()

        return Response(pdf.output(dest='s').encode('latin-1'), mimetype='', headers={'content-Disposition': 'attachment; filename=report.pdf'})
