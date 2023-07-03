from flask import render_template
from __main__ import app

@app.route('/')
def home():
    return render_template('index.html')
