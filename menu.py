# -*- coding:utf8 -*- 
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import json
import urllib2
import os
import time

basedir = os.path.abspath(os.path.dirname(__file__))

APP_ID = ''
SECRET = ''

def get_token():
    with open(basedir + '/acc_token','rw') as f:
        data = f.read()
    if data:
        past_time = int(data[0:10])
        acc_token = data[10:]
    else:
        past_time = 1400000000
    now_time = int(time.time())
    if now_time - past_time > 1000:
        app_id = APP_ID
        app_secret = SECRET
        url = 'https://api.weixin.qq.com/cgi-bin/'\
              'token?grant_type=client_credential&appid=%s&secret=%s' % \
              (app_id, app_secret)
        result = urllib2.urlopen(url).read()
        if json.loads(result).get('errcode'):            
            acc_token = "fail to get acc_token --get_acc_token.py"

        else:
            acc_token = json.loads(result).get('access_token')
            string = str(int(time.time())) + acc_token
            with open(basedir + '/acc_token', 'w') as f:
                f.write(string)
    return acc_token

MENU = {
    "button": [
        {

            "name": "管理员",
            "sub_button": [                
                {
                    "type": "view",
                    "name": "发布活动",
                    "url": "http://voluntary.njuszy.cn/admin"
                }
                ]

        },
        {
            "name": "志愿者活动",
            "sub_button": [
                {
                    "type": "view",
                    "name": "活动信息",
                    "url": "http://voluntary.njuszy.cn"
                },
                {
                    "type": "scancode_push",
                    "name": "签退",
                    "key": "rselfmenu_0_1",
                    "sub_button": []
                },
                {
                    "type": "scancode_push",
                    "name": "签到",
                    "key": "rselfmenu_0_1",
                    "sub_button": []
                }
            ]

        }

    ]
}

def create_menu():
    acc_token = get_token()
    if acc_token:
        url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % acc_token
        data = MENU
        request = urllib2.urlopen(url, json.dumps(data, ensure_ascii=False))
        return json.loads(request.read())
    else:
        return "failed to get access_token!--menu.py"


if __name__ == "__main__":
    print create_menu()
