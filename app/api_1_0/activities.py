# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import time
from flask import request, jsonify
from flask_login import login_required, current_user

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
            return jsonify(status='empty')
        a_list = [i.return_dict() for i in activity]
        return jsonify(status='ok', result=a_list)
    elif request.method == 'POST':
        data = request.values
        if data:
            if data.get('acid'):
                acid = data.get('acid')
                activity = Activity.query.filter_by(acid=acid).first()
                activity.actype = data.get('actype')
                activity.vol_time = data.get('vol_time')
                activity.ac_place = data.get('ac_place')
                activity.subject = data.get('title')
                finish_time = data.get('finish_time').encode('utf8')
                start_time = data.get('start_time').encode('utf8')
                activity.introduce = data.get('introduce')
                activity.required_stus = data.get('required_stus')
                activity.finish_time = ' '.join(finish_time.split('T')) + ':00'
                activity.start_time = ' '.join(start_time.split('T')) + ':00'

            else:
                acid = int(time.time())
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
                activity = Activity(acid=acid, actype=actype, vol_time=vol_time,
                                    ac_place=ac_place, subject=subject,
                                    finish_time=finish_time, start_time=start_time,
                                    introduce=introduce, required_stus=required_stus)
            db.session.add(activity)
            db.session.commit()
            return jsonify(status='ok')
        return jsonify(status='fail')


@api.route('/activity', methods=['GET'])
@login_required
def activity():
    activity = db.session.query(Activity).all()
    if activity is None:
        return jsonify(status='empty', stuid=current_user.stuid)
    a_list = [i.return_dict() for i in activity]
    return jsonify(status='ok', result=a_list, stuid=current_user.stuid)


@api.route('/activity', methods=['DELETE'])
@admin_login_required
def delete_activity():
    acid = request.values.get('acid')
    activity = Activity.query.filter_by(acid=int(acid))
    if not activity:
        return jsonify(status='fail', errmsg='wrong acid')
    else:
        db.session.remove(activity)
        db.session.commit()
        return jsonify(status='ok')
