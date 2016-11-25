# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import qrcode
import base64
from StringIO import StringIO
from flask import request, jsonify, send_file, make_response

from app.api_1_0 import api
from app.admin.functions import admin_login_required


@api.route('/qrcode/checkin', methods=['POST'])
@admin_login_required
def check_in():
    data = request.values
    acid = data.get('acid')
    if acid:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        qr.add_data('https://www.njuszy.cn/qrcode/checkin/'+str(acid))
        qr.make(fit=True)
        out = StringIO()
        qr_img = qr.make_image()
        qr_img.save(out, 'PNG')
        return jsonify(data="data:image/png;base64," + base64.b64encode(out.getvalue()).decode('ascii'))
    else:
        return jsonify(status='fail')


@api.route('/qrcode/checkout', methods=['POST'])
@admin_login_required
def check_out():
    data = request.values
    acid = data.get('acid')
    if acid:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        qr.add_data('https://www.njuszy.cn/qrcode/checkout/'+str(acid))
        qr.make(fit=True)
        out = StringIO()
        qr_img = qr.make_image()
        qr_img.save(out, 'PNG')
        return jsonify(data="data:image/png;base64," + base64.b64encode(out.getvalue()).decode('ascii'))
    else:
        return jsonify(status='fail')
