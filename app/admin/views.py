# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from . import admin
from flask import render_template, redirect, url_for, jsonify
from app.admin.functions import admin_login_required

from app.models import Activity

from app.main.handle_railway import get_not_fill


@admin.route('/')
@admin_login_required
def index():
    return render_template('admin/admin_index.html')


@admin.route('/publish')
@admin_login_required
def publish():
    return render_template('admin/admin.html')


@admin.route('/login')
def login():
    return render_template('admin/login.html')


#活动详情页
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

@admin.route('/get_not_filled')
@admin_login_required
def get_not_filled():
    return jsonify(data=get_not_fill())