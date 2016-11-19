# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from app.api_1_0 import api
from app.admin.functions import admin_login_required

@api.route('/activities')
@admin_login_required
def activity():
    return 'a'