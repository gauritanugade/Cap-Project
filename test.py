from flask import Blueprint, render_template

test_app = Blueprint('test_app', __name__, template_folder='templates')

@test_app.route('/test')
def test():
    return "Test app"