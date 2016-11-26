#!/usr/bin/env python
#
class Config(object):
    pass


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
