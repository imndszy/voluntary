# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from flask import request, jsonify
from app.api_1_0 import api
from app.admin.functions import admin_login_required
from app import db
from app.models import Unfinished_activity

@api.route('/activities', methods=['POST'])
@admin_login_required
def activity():
    data = request.values
    print data
    return jsonify(status='ok')