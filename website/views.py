# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:16:55 2021

@author: artbo
"""

from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>TestersGonnaTest<h1>"