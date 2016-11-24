# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from . import admin
from flask import render_template
from app.admin.functions import admin_login_required


@admin.route('/')
@admin_login_required
def index():
    return render_template('admin/admin.html')


@admin.route('/login')
def login():
    return render_template('admin/login.html')


@admin.route('/admin_detail')
@admin_login_required
def detail():
    return render_template('admin/admin_detail.html')


@admin.route('/index')
@admin_login_required
def admin_index():
    return render_template('admin/admin_index.html')
