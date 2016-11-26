#!/usr/bin/env python
#
from flask import Flask
form config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)


app.route('/')
def home():
    return '<h1>hello world!</h1>'

if __name__ == '__main__':
    app.run()
