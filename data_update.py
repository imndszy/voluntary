# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import time

from app import db
from app.models import Activity

def __update():
    activity = Activity.query.all()
    for i in activity:
        dt = i.finish_time.strftime('%Y-%m-%d %H:%M:%S')
        stop_time = time.strptime(dt, '%Y-%m-%d %H:%M:%S')
        stop_time = int(time.mktime(stop_time))
        if stop_time < int(time.time()):
            i.finished = True
            db.session.add(i)
    db.session.commit()

if __name__ == "__main__":
    __update()
    time.sleep(60)