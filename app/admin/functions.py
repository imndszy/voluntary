# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import functools
from flask import session, redirect, url_for


def admin_login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('admin') == 'logged':
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.login'))
    return wrapper
