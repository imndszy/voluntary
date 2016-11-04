# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from . import main
from flask import render_template


@main.route('/')
def index():
    # return render_template('main/index.html')
    return 'hello'