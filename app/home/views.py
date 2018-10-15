# -*- coding: utf-8 -*-
__author__ = 'Terence Jie'
__time__ = '2018/10/12 14:28'

from . import home


@home.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"
