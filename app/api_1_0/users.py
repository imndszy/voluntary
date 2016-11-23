# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from flask import request,jsonify
from flask_login import login_user, logout_user, login_required

from app.api_1_0 import api
from app.models import User

@api.route('/user/verification',methods=['POST'])
def user_verify():
    data = request.values
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(stuid=int(username)).first()
    if user is None:
        return jsonify(status='fail')
    if user.password_reviewed:
        if user.verify_password(password):
            login_user(user, True)
            return jsonify(status='ok')
        return jsonify(status='fail')
    else:
        if user.identified_card == password:
            login_user(user, True)
            return jsonify(status='ok')
        return jsonify(status='fail')


