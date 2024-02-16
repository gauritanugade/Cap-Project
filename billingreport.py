from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def remuneration_form():
    return render_template('billingform.html')

@app.route('/submit', methods=['POST'])
def submit_bill():

    return render_template('billingform.html', user_name=request.form['name'])  # Example

if __name__ == '__main__':
    app.run(debug=True)
