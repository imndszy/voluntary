# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import time
from flask import request, jsonify

from app.api_1_0 import api
from app.admin.functions import admin_login_required
from app import db
from app.models import Unfinished_activity


@api.route('/activities', methods=['GET','POST'])
@admin_login_required
def activity():
    if request.method == 'GET':
        ac = db.session.query(Unfinished_activity).all()
        print ac
        return jsonify(ac='ok')
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
            finish_time = (' ').join(finish_time.split('T'))+':00'
            start_time = (' ').join(start_time.split('T'))+':00'
            acid = int(time.time())
            activity = Unfinished_activity(acid=acid,actype=actype,vol_time=vol_time,
                                           ac_place=ac_place,subject=subject,
                                           finish_time=finish_time,start_time=start_time,
                                           introduce=introduce,required_stus=required_stus)
            db.session.add(activity)
            db.session.commit()
            return jsonify(status='ok')
        return jsonify(status='fail')