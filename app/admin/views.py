# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from . import admin
from flask import render_template, request, redirect, url_for
from app.admin.functions import admin_login_required

from app.models import Activity


@admin.route('/')
@admin_login_required
def index():
    return render_template('admin/admin.html')


@admin.route('/login')
def login():
    return render_template('admin/login.html')


@admin.route('/admin_detail/<int:acid>')
@admin_login_required
def detail(acid):
    if acid:
        activity = Activity.query.filter_by(acid=acid).first()
        sth = activity.return_dict()
        if sth.get('actual_stus') is None:
            sth['actual_stus'] = 0
        return render_template('admin/admin_detail.html',title=sth['subject'],
                               introduce=sth['introduce'],
                               number=str(sth.get('actual_stus')) + '/' +str(sth['required_stus']),
                               acid=acid, ac_place=activity.ac_place, ac_start=activity.start_time)
    return redirect(url_for('admin.index'))


@admin.route('/admin_index')
@admin_login_required
def admin_index():
    return render_template('admin/admin_index.html')
