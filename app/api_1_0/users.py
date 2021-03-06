# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from flask import request, jsonify, session
from flask_login import login_user, login_required, current_user

from app.api_1_0 import api
from app.models import User, Activity, AcUser
from app import db


@api.route('/user/verification', methods=['POST'])
def user_verify():
    data = request.values
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(stuid=username).first()
    if user is None:
        return jsonify(status='fail')
    if (user.password_reviewed and user.verify_password(password)) or user.identified_card[-6:] == password:
        session['stuid'] = username
        login_user(user, remember=True)
        return jsonify(status='ok', stuid=session['stuid'])
    return jsonify(status='fail')


@api.route('/user/activity-registration',methods=['POST'])
@login_required
def registration():
    data = request.values
    acid = data.get('acid')
    stuid = current_user.stuid
    activity = Activity.query.filter_by(acid=acid).first()

    if activity is None:
        return jsonify(status='fail')

    if activity.finished:
        return jsonify(status='finished')

    temp = AcUser.query.filter_by(acid=acid,stuid=stuid).first()
    if temp is not None:
        return jsonify(status='duplicate')

    if activity.actual_stus == activity.required_stus:
        return jsonify(status='full')

    try:
        registration = AcUser(acid=acid,stuid=stuid)
        db.session.add(registration)
        activity.actual_stus += 1
        db.session.add(activity)
        db.session.commit()
        return jsonify(status='ok')
    except:
        db.session.rollback()
        return jsonify(status='fail')


@api.route('/user/activity-unregistration',methods=['POST'])
@login_required
def unregistration():
    data = request.values
    acid = data.get('acid')
    stuid = current_user.stuid
    activity = Activity.query.filter_by(acid=acid).first()
    if activity is None:
        return jsonify(status='fail')

    if activity.finished:
        return jsonify(status='finished')

    temp = AcUser.query.filter_by(acid=acid,stuid=stuid).first()
    if temp is None:
        return jsonify(status='none')

    try:
        db.session.delete(temp)
        activity.actual_stus -= 1
        db.session.add(activity)
        db.session.commit()
        return jsonify(status='ok')
    except:
        return jsonify(status='fail')

