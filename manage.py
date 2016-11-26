#!/usr/bin/env python
#

from flask.ext.script import Manager, Server
from main import app

manager = Manager(app)
manager.add_command("server", Server(host='192.168.40.88', port='8089'))

@manager.shell
def make_shell_context():
    return dict(app=app)

if __name__ == "__main__":
    manager.run()
