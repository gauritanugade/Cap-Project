from flask import Flask,Blueprint,render_template,request,session,make_response,redirect,flash,Response
from flask_mysqldb import MySQL
from fpdf import FPDF
from datetime import datetime

date = datetime.now()


report = Blueprint('report', __name__, template_folder='templates')

app=report


mysql=MySQL()


@app.route('/reportgenerate')
def home():
    return render_template('report1.html')

@app.route('/download/report/pdf', methods=["POST"])
def download_report():
    if request.method == "POST":
        session['received_date'] = request.form['received_date']
        received_date = session['received_date']

        now = date.today()
        cursor = mysql.connection.cursor()
        cursor.execute(
            " select faculty.faculty,subject.subject,time_table.sem,time_table.year,paper_count.quespaper_code,coursename.course_id,paper_count.count,paper_count.received_date,examsession.month from time_table join paper_count on time_table.timetable_id=paper_count.timetable_id join faculty on time_table.faculty_id=faculty.faculty_id join subject on time_table.subject_id=subject.subject_id join coursename on time_table.coursename_id=coursename.coursename_id join examsession on time_table.examsession_id=examsession.examsession_id where paper_count.received_date=%s;",
            (received_date,))
        result = cursor.fetchall()
        pdf = FPDF()
        pdf.add_page()

        page_width = pdf.w - 2 * pdf.l_margin

        for index, record in enumerate(result):
            if index % 2 == 0:
                pdf.ln(15)
                pdf.set_font('Times', 'B', 20.0)
                pdf.cell(page_width, 0.0, "Central Assessment Process" + '' + '(' + str(record[7]) + ')')
                pdf.ln(20)
                pdf.cell(500, 0.0, "Faculty:-" + str(record[0]) + '-' + str(record[3]))
                pdf.ln(15)
                pdf.cell(20, 0.0, "Subject:-" + record[1])
                pdf.ln(15)
                pdf.cell(page_width, 0.0, "Sem:-" + str(record[2]))
                pdf.ln(15)
                pdf.cell(page_width, 0.0, "Quespaper Code:-" + record[4])
                pdf.ln(15)
                pdf.cell(page_width, 0.0, "Course ID:-" + record[5])
                pdf.ln(15)
                pdf.cell(page_width, 0.0, "Count:-" + str(record[6]))
                pdf.ln(15)
                pdf.line(10, pdf.get_y(), 200, pdf.get_y())
                pdf.ln(15)
            else:
                pdf.ln(5)
                pdf.cell(page_width, 0.0, "Central Assessment Process" + '' + '(' + str(record[7]) + ')')
                pdf.ln(15)
                pdf.cell(500, 0.0, "Faculty:-" + str(record[0]) + '-' + str(record[3]))
                pdf.ln(15)
                pdf.cell(20, 0.0, "Subject:-" + record[1])
                pdf.ln(15)
                pdf.cell(page_width, 0.0, "Sem:-" + str(record[2]))
                pdf.ln(15)
                pdf.cell(page_width, 0.0, "Quespaper Code:-" + record[4])
                pdf.ln(15)
                pdf.cell(page_width, 0.0, "Course ID:-" + record[5])
                pdf.ln(15)
                pdf.cell(page_width, 0.0, "Count:-" + str(record[6]))
                pdf.ln(15)
                pdf.line(10, pdf.get_y(), 200, pdf.get_y())
                pdf.ln(15)

        cursor.close()

        return Response(pdf.output(dest='s').encode('latin-1'), mimetype='', headers={'content-Disposition': 'attachment; filename=report.pdf'})