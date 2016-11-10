# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from . import admin
from flask import render_template

@admin.route('/')
def index():
    return render_template('advanced.html')

@admin.route('login')
def login():
    return render_template('login.html')