# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
"""
数据模型定义
"""

import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request
from flask_login import UserMixin
from app import db, login_manager


class AcUser(db.Model):

    __tablename__ ='ac_user'
    stuid = db.Column('stuid', db.Integer, primary_key=True)
    acid = db.Column('acid', db.Integer)
    checkin = db.Column('check_in', db.DateTime, nullable=True)
    checkout = db.Column('check_out', db.DateTime, nullable=True)
    period = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Activity {self.acid},User {self.stuid}>'.format(self=self)


class User(UserMixin, db.Model):

    __tablename__ = 'users'
    stuid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=True)
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.String(20), nullable=True)
    identified_card = db.Column(db.String(30), unique=True)
    service_time = db.Column(db.Float, default=0)
    password_reviewed = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_image_url(self, size=100, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        the_hash = self.avatar_hash or hashlib.md5(
            self.stuid.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=the_hash, size=size, default=default, rating=rating)

    def get_id(self):
        return unicode(self.stuid)

    def __repr__(self):
        return '<User {self.stuid}>'.format(self=self)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Activity(db.Model):

    __tablename__ = 'activity'
    acid = db.Column(db.Integer, primary_key=True)
    actype = db.Column(db.Integer, nullable=True)              # 活动类型
    ac_place = db.Column(db.String(128), nullable=True)        # 活动地点
    start_time = db.Column(db.DateTime, nullable=True)         # 活动开始时间
    finish_time = db.Column(db.DateTime, nullable=True)        # 活动结束时间
    subject = db.Column(db.String(128), nullable=True)         # 活动主题
    introduce = db.Column(db.Text, nullable=True)              # 活动简介
    required_stus = db.Column(db.Integer, nullable=True, default=0)       # 需求人数
    actual_stus = db.Column(db.Integer, nullable=True, default=0)         # 实际人数
    ac_periods = db.Column(db.Integer, nullable=True)          # 活动期数
    vol_time = db.Column(db.Float, nullable=True)              # 活动时长
    finished = db.Column(db.Boolean, default=False)            # 活动是否完成
    checkin_url = db.Column(db.String(128), nullable=True)          # 签到的二维码
    checkout_url = db.Column(db.String(128), nullable=True)         # 签退的二维码
    in_time_start = db.Column(db.Integer, nullable=True)       # 签到开始时间
    in_time_stop = db.Column(db.Integer, nullable=True)        # 签到结束时间
    out_time_start = db.Column(db.Integer, nullable=True)      # 签退开始时间
    out_time_stop = db.Column(db.Integer, nullable=True)       # 签退结束时间
    linkman = db.Column(db.String(16), nullable=True)          # 联系人（有字长限制）
    contact = db.Column(db.String(16), nullable=True)          # 联系方式

    def __repr__(self):
        return '<Activity {self.acid}>'.format(self=self)

    def return_dict(self):
        return dict(acid=self.acid, actype=self.actype,
                    ac_place=self.ac_place, start_time=self.start_time,
                    finish_time=self.finish_time, subject=self.subject,
                    introduce=self.introduce, required_stus=self.required_stus,
                    actual_stus=self.actual_stus, ac_periods=self.ac_periods,
                    vol_time=self.vol_time, finished=self.finished)

    def return_qrcode(self):
        return dict(checkin_url=self.checkin_url,
                    checkout_url=self.checkout_url,
                    in_time_start=self.in_time_start,
                    in_time_stop=self.in_time_stop,
                    out_time_start=self.out_time_start,
                    out_time_stop=self.out_time_stop)
