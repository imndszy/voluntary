# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import re
from . import main
from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, \
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


@main.route('/qrcode/checkin/<acid>')
def qrcode_checkin(acid):
    if len(acid) != 30 or not acid.isdigit():
        return redirect(url_for('main.login'))
