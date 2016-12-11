#!/usr/bin/env python
#
class Config(object):
    pass


class ProdConfig(Config):
    pass

class DevConfig(Config):
    #DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root123.@127.0.0.1:3306/CarltonXu"
    SQLALCHEMY_ECHO=True
