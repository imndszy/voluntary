# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from flask import Blueprint

api = Blueprint('api', __name__)

from . import activities, admin, users, create_qrcode
