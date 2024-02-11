from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def current_date():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    return render_template('currentdate.html', current_date=formatted_date)

if __name__ == '__main__':
    app.run(debug=True)