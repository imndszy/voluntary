# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from app.api_1_0 import api
import os

from flask import request, jsonify, session


@api.route('/admin', methods=['POST'])
def verify():
    data = request.values
    username = data.get('username')
    passwd = data.get('password')
    if username == os.environ.get('FLASK_ADMIN') and passwd == os.environ.get('FLASK_ADMIN_PASS'):
        session['admin'] = 'logged'
        return jsonify(status='ok')
    else:
        return jsonify(status='fail')
