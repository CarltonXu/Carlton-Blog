#!/usr/bin/env python
#

from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from main import app, db, User, Post, Comment, Tag

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("server", Server(host='192.168.40.86', port='5000'))
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment, Tag=Tag)

if __name__ == "__main__":
    manager.run()
