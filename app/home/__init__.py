# -*- coding: utf-8 -*-
__author__ = 'Terence Jie'
__time__ = '2018/10/12 14:14'

from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views
