# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from . import main
from flask import render_template

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/user')
def user():
    return render_template('user.html')

@main.route('/activity')
def activity():
    return render_template('deatil.html')