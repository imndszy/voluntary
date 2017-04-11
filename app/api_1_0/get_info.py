# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from flask import make_response, send_file

from app.api_1_0 import api
from app.admin.functions import admin_login_required


@api.route('/acuser', methods=['GET'])
@admin_login_required
def acuser():
    response = make_response(send_file("/home/ubuntu/www/voluntary/info.xlsx"))
    response.headers["Content-Disposition"] = "attachment; filename=information.xlsx"
    return response
