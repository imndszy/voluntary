# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import functools

def admin_login_required(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        pass