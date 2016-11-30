# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import time
from flask import request, jsonify, session
from flask_login import login_required

from app.api_1_0 import api
from app.admin.functions import admin_login_required
from app import db
from app.models import Activity


@api.route('/activities', methods=['GET', 'POST'])
@admin_login_required
def activities():
    if request.method == 'GET':
        activity = db.session.query(Activity).all()
        if activity is None:
            return jsonify(status='empty', stuid=session.get('stuid'))
        a_list = [i.return_dict() for i in activity]
        return jsonify(status='ok', result=a_list, stuid=session.get('stuid'))
    elif request.method == 'POST':
        data = request.values
        if data:
            actype = data.get('actype')
            vol_time = data.get('vol_time')
            ac_place = data.get('ac_place')
            subject = data.get('title')
            finish_time = data.get('finish_time').encode('utf8')
            start_time = data.get('start_time').encode('utf8')
            introduce = data.get('introduce')
            required_stus = data.get('required_stus')
            finish_time = ' '.join(finish_time.split('T'))+':00'
            start_time = ' '.join(start_time.split('T'))+':00'
            acid = int(time.time())
            activity = Activity(acid=acid, actype=actype, vol_time=vol_time,
                                ac_place=ac_place, subject=subject,
                                finish_time=finish_time, start_time=start_time,
                                introduce=introduce, required_stus=required_stus)
            db.session.add(activity)
            db.session.commit()
            return jsonify(status='ok', stuid=session.get('stuid'))
        return jsonify(status='fail', stuid=session.get('stuid'))


@api.route('/activity', methods=['GET'])
@login_required
def activity():
    activity = db.session.query(Activity).all()
    if activity is None:
        return jsonify(status='empty', stuid=session.get('stuid'))
    a_list = [i.return_dict() for i in activity if not i.finished]
    return jsonify(status='ok', result=a_list, stuid=session.get('stuid'))
