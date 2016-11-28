# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import time
from flask import render_template, request, session, jsonify
from flask_login import login_required

from app import db
from app.main import main
from app.models import Activity, User, AcUser


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('index.html')


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/user')
@login_required
def user():
    return render_template('user.html')


@main.route('/activity')
@login_required
def activity():
    return render_template('deatil.html')


@main.route('/checkin/<code>')
def qrcode_checkin(code):
    if session.get('in_verify') == 'ok':
        return "您已经签到过了！"

    if len(code) != 30 or not code.isdigit():
        return "错误参数！请联系管理员！"
    else:
        acid = int(code[0:10])
        session['acid'] = acid
        start_time = int(code[10:20])
        finish_time = int(code[20:])
        activity = Activity.query.filter_by(acid=acid).first()
        # 以下代码用于确认参数的有效性
        if activity is None:
            return "错误参数！请联系管理员！"
        qrcode = activity.return_qrcode()
        if start_time != qrcode['in_time_start'] or finish_time != qrcode['in_time_stop']:
            return "错误参数！请联系管理员！"

        now = int(time.time())
        session['checkin_time'] = now
        if now < qrcode['in_time_start'] or now > qrcode['in_time_stop']:
            return "尚未到签到时间！"
        else:
            session['checkin'] = 'checked'
            session['checkin_time'] = now
            return render_template('check.html')


@main.route('/checkout/<code>')
def qrcode_checkout(code):
    if session.get('out_verify') == 'ok':
        return "您已经签退过了！"

    if len(code) != 30 or not code.isdigit():
        return "错误参数！请联系管理员！"
    else:
        acid = int(code[0:10])
        session['acid'] = acid
        start_time = int(code[10:20])
        finish_time = int(code[20:])
        activity = Activity.query.filter_by(acid=acid).first()
        # 以下代码用于确认参数的有效性
        if activity is None:
            return "错误参数！请联系管理员！"
        qrcode = activity.return_qrcode()
        if start_time != qrcode['out_time_start'] or finish_time != qrcode['out_time_stop']:
            return "错误参数！请联系管理员！"

        now = int(time.time())
        if now < qrcode['out_time_start'] or now > qrcode['out_time_stop']:
            return "尚未到签退时间！"
        else:
            session['checkout'] = 'checked'
            session['checkout_time'] = now
            return render_template('check.html')


@main.route('/qrcode/verify', methods=['POST'])
def verify():
    if session.get('checkout') or session.get('checkin'):
        data = request.values
        stuid = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(stuid=stuid).first()
        now = int(time.time())

        if user is None:
            return jsonify(status='fail',data="错误的用户名或密码")
        else:
            if user.password_reviewed:
                if user.verify_password(password):
                    if now - session.get('checkout_time',1) < 300:
                        session['out_verify'] = 'ok'
                        checkout = AcUser.query.filter_by(
                            acid=session.get('acid'),stuid=stuid).first()
                        checkout.checkout = time_transfer(now)
                        db.session.add(checkout)
                        db.session.commit()
                        return jsonify(status='ok',data="您已成功签退！")

                    elif now - session.get('checkin_time',1) < 300:
                        session['in_verify'] = 'ok'
                        checkin = AcUser.query.filter_by(
                            acid=session.get('acid'), stuid=stuid).first()
                        checkin.checkin = time_transfer(now)
                        db.session.add(checkin)
                        db.session.commit()
                        return jsonify(status='ok',data="您已成功签到！")

                    else:
                        return jsonify(staus='fail',data="请在规定的时间内验证身份！请重新扫描二维码！")
                return jsonify(status='fail', data="错误的用户名或密码")
            else:
                if user.identified_card == password:
                    if now - session.get('checkout_time',1) < 300:
                        session['out_verify'] = 'ok'
                        checkout = AcUser.query.filter_by(
                            acid=session.get('acid'), stuid=stuid).first()
                        checkout.checkout = time_transfer(now)
                        db.session.add(checkout)
                        db.session.commit()
                        return jsonify(status='ok',data="您已成功签退！")

                    elif now - session.get('checkin_time',1) < 300:
                        session['in_verify'] = 'ok'
                        checkin = AcUser.query.filter_by(
                            acid=session.get('acid'), stuid=stuid).first()
                        checkin.checkin = time_transfer(now)
                        db.session.add(checkin)
                        db.session.commit()
                        return jsonify(status='ok',data="您已成功签到！")

                    else:
                        return jsonify(staus='fail', data="请在规定的时间内验证身份！请重新扫描二维码！")
                return jsonify(status='fail',data="错误的用户名或密码")
    else:
        return jsonify(status='fail',data="请先扫描二维码！！")


def time_transfer(timestamp):
    '''
    transfer time format from timestamp to other style
    :param timestamp: timestamp(int)
    :return: "%Y-%m-%d %H:%M:%S"
    '''
    time_array = time.localtime(timestamp)
    new_style = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return new_style
