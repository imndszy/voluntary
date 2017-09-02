# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import os
import sys
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import subprocess
from app import create_app, db
from app.models import User, Activity
from flask import session
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from datetime import timedelta


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# subprocess.Popen(['python', PATH + '/data_update.py'])

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=100)

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Activity=Activity)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

