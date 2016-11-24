# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from . import main
from flask import render_template
from flask_login import login_user, logout_user, login_required, \
    current_user


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('index.html')


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/user')
@login_required
def user():
    return render_template('user.html')


@main.route('/activity')
@login_required
def activity():
    return render_template('deatil.html')
