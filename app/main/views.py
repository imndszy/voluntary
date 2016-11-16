# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from . import main
from flask import render_template


@main.route('/')
def index():
    return render_template('advanced.html')


@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/user')
def user():
    return render_template('user.html')