# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, url_for
from flask_login import UserMixin
from app import db
# login_manager


fa_user = db.Table('fa_user',
                   db.Column('stuid', db.Integer, db.ForeignKey('users.stuid')),
                   db.Column('acid', db.Integer, db.ForeignKey('finished_activity.acid')),
                   db.Column('check_in', db.DateTime),
                   db.Column('check_out', db.DateTime))

ufa_user = db.Table('ufa_user',
                    db.Column('stuid', db.Integer, db.ForeignKey('users.stuid')),
                    db.Column('acid', db.Integer, db.ForeignKey('unfinished_activity.acid')))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    stuid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=True)
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.String(20), nullable=True)
    identified_card = db.Column(db.String(30), unique=True)
    service_time = db.Column(db.Float)
    finished_activities = db.relationship('Finished_activity',
                                          secondary=fa_user)
    unfinished_activities = db.relationship('Unfinished_activity',
                                            secondary=ufa_user)

    def gravatar(self, size=100, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or hashlib.md5(
            self.stuid.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

class Finished_activity(db.Model):
    __tablename__ = 'finished_activity'
    acid = db.Column(db.Integer, primary_key=True)
    actype = db.Column(db.Integer,nullable=True)          #活动类型
    ac_place = db.Column(db.String(128),nullable=True)        #活动地点
    start_time = db.Column(db.DateTime,nullable=True)          #活动开始时间
    finish_time = db.Column(db.DateTime,nullable=True)        #活动结束时间
    subject = db.Column(db.String(128),nullable=True)         #活动主题
    introduce = db.Column(db.Text,nullable=True)             #活动简介
    required_stus = db.Column(db.Integer,nullable=True)       #需求人数
    actual_stus = db.Column(db.Integer,nullable=True)       #实际人数
    ac_periods = db.Column(db.Integer,nullable=True)    #活动期数
    # linkman = db.Column(db.String(16))  #联系人（有字长限制）
    # contact = db.Column(db.String(16))  #联系方式
    users = db.relationship('User',secondary=fa_user)


class Unfinished_activity(db.Model):
    __tablename__ = 'unfinished_activity'
    acid = db.Column(db.Integer, primary_key=True)
    actype = db.Column(db.Integer,nullable=True)          #活动类型
    ac_place = db.Column(db.String(128),nullable=True)        #活动地点
    start_time = db.Column(db.DateTime,nullable=True)          #活动开始时间
    finish_time = db.Column(db.DateTime,nullable=True)        #活动结束时间
    subject = db.Column(db.String(128),nullable=True)         #活动主题
    introduce = db.Column(db.Text,nullable=True)             #活动简介
    required_stus = db.Column(db.Integer,nullable=True)       #需求人数
    actual_stus = db.Column(db.Integer,nullable=True)       #实际人数
    ac_periods = db.Column(db.Integer,nullable=True)    #活动期数
    # linkman = db.Column(db.String(16))  # 联系人（有字长限制）
    # contact = db.Column(db.String(16))  # 联系方式
    users = db.relationship('User',secondary=ufa_user)

