from flask import Flask,render_template, request, session, url_for

import os
import datetime

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=360)
app.secret_key = os.environ.get('secret_key')

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/login')
def login():
    return render_template('/login.html')