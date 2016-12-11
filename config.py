#!/usr/bin/env python
#
class Config(object):
    SECRET_KEY = 'c3f5e2fdf0fcfe60f3d531a8774971b1'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root123.@127.0.0.1:3306/CarltonXu"
    SQLALCHEMY_ECHO=True
