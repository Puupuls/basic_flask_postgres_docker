from flask import Blueprint, render_template

from models import User

hello = Blueprint('hello', __name__)

@hello.route('/')
def hello_world():  # put application's code here
    return render_template(
        'hello/hello.html',
        user=User.query.filter_by(username='admin').first()
    )