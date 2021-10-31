# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:16:14 2021

@author: artbo
"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login<p>"

@auth.route("/logout")
def logout():
    return"<p>logout<p>"

@auth.route("/sing-up")
def sign_up():
    return "<p>Sign up<p>"

