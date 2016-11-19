# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from app.api_1_0 import api

from flask import request,jsonify,session


@api.route('/admin', methods = ['POST'])
def verify():
    data = request.values
    username = data.get('username')
    passwd = data.get('password')
    if username == 'admin' and passwd == 'pass':
        session['admin'] = 'logged'
        print 'ok'
        return jsonify(status='ok')
    else:
        return jsonify(status='fail')