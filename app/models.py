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
    service_time = db.Column(db.Float,nullable=True)
    finished_activities = db.relationship('Finished_activity',
                                          secondary=fa_user)
    unfinished_activities = db.relationship('Unfinished_activity',
                                            secondary=ufa_user)

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
        hash = self.avatar_hash or hashlib.md5(
            self.stuid.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)

    def __repr__(self):
        return '<User {self.stuid}>'.format(self=self)


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
    vol_time = db.Column(db.Float, nullable=True)   #活动时长
    # linkman = db.Column(db.String(16))  #联系人（有字长限制）
    # contact = db.Column(db.String(16))  #联系方式
    users = db.relationship('User',secondary=fa_user)

    def __repr__(self):
        return '<Finished activity {self.acid}>'.format(self=self)

    def return_dict(self):
        return dict(acid=self.acid, actype=self.actype,
                       ac_place=self.ac_place, start_time=self.start_time,
                       finish_time=self.finish_time, subject=self.subject,
                       introduce=self.introduce, required_stus=self.required_stus,
                       actual_stus=self.actual_stus, ac_periods=self.ac_periods,
                       vol_time=self.vol_time)


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
    vol_time = db.Column(db.Float,nullable=True)
    # linkman = db.Column(db.String(16))  # 联系人（有字长限制）
    # contact = db.Column(db.String(16))  # 联系方式
    users = db.relationship('User',secondary=ufa_user)

    def __repr__(self):
        return '<Unfinished activity {self.acid}>'.format(self=self)

    def return_dict(self):
        return dict(acid=self.acid,actype=self.actype,
                       ac_place=self.ac_place,start_time=self.start_time,
                       finish_time=self.finish_time,subject=self.subject,
                       introduce=self.introduce,required_stus=self.required_stus,
                       actual_stus=self.actual_stus,ac_periods=self.ac_periods,
                       vol_time=self.vol_time)

