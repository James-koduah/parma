#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from mysql_engine.control_orm import control
app = Flask(__name__)
CORS(app)
from sections.hospitals import hospitals
from sections.hospital import hospital
from sections.admin import admin

app.register_blueprint(hospitals)
app.register_blueprint(hospital)
app.register_blueprint(admin)

@app.route('/')
def welcome():
    return render_template('welcome/welcome.html')

@app.route('/login_signup')
def login():
    return render_template('login_signup.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
