# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import time
import qrcode
import base64
from StringIO import StringIO
from flask import request, jsonify

from app import db
from app.api_1_0 import api
from app.appconfig import HOST
from app.admin.functions import admin_login_required
from app.models import Activity


@api.route('/qrcode/checkin', methods=['POST'])
@admin_login_required
def check_in():
    data = request.values
    acid = data.get('acid')
    if acid:
        start_time = data.get('checkin_start')
        work = int(data.get('checkin_work'))
        # 获取时间戳
        if len(start_time.split(':')) == 2:
            time_array = time.strptime(start_time, "%Y-%m-%dT%H:%M")
            start_timestamp = int(time.mktime(time_array))
        elif len(start_time.split(':')) == 3:
            time_array = time.strptime(start_time[:16], "%Y-%m-%dT%H:%M")
            start_timestamp = int(time.mktime(time_array))
        else:
            return jsonify(status='fail',data='错误的时间格式！')
        finish_time = start_timestamp + work*60
        activity = Activity.query.filter_by(acid=acid).first()
        activity.in_time_start = start_timestamp
        activity.in_time_stop = finish_time

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        checkin_url = HOST+'checkin/'+str(acid)+str(start_timestamp)+str(finish_time)     # 签到扫描二维码指向链接
        qr.add_data(checkin_url)
        qr.make(fit=True)
        out = StringIO()
        qr_img = qr.make_image()
        qr_img.save(out, 'PNG')

        activity.checkin_url = checkin_url
        db.session.add(activity)
        db.session.commit()

        return jsonify(status='ok',data="data:image/png;base64," + base64.b64encode(out.getvalue()).decode('ascii'))
    else:
        return jsonify(status='fail')


@api.route('/qrcode/checkout', methods=['POST'])
@admin_login_required
def check_out():
    data = request.values
    acid = data.get('acid')
    if acid:
        start_time = data.get('checkout_start')
        work = int(data.get('checkout_work'))
        if len(start_time.split(':')) == 2:
            time_array = time.strptime(start_time, "%Y-%m-%dT%H:%M")
            start_timestamp = int(time.mktime(time_array))
        elif len(start_time.split(':')) == 3:
            time_array = time.strptime(start_time[:16], "%Y-%m-%dT%H:%M")
            start_timestamp = int(time.mktime(time_array))
        else:
            return jsonify(status='fail', data='错误的时间格式！')
        finish_time = start_timestamp + work * 60
        activity = Activity.query.filter_by(acid=acid).first()
        activity.out_time_start = start_timestamp
        activity.out_time_stop = finish_time

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        checkout_url = HOST + 'checkout/' + str(acid) + str(start_timestamp) + str(finish_time)
        qr.add_data(checkout_url)
        qr.make(fit=True)
        out = StringIO()
        qr_img = qr.make_image()
        qr_img.save(out, 'PNG')

        activity.checkout_url = checkout_url
        db.session.add(activity)
        db.session.commit()

        return jsonify(status='ok',data="data:image/png;base64," + base64.b64encode(out.getvalue()).decode('ascii'))
    else:
        return jsonify(status='fail')
