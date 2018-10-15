# -*- coding: utf-8 -*-
__author__ = 'Terence Jie'
__time__ = '2018/10/12 14:14'

from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
