# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:12:50 2021

@author: artbo
"""

from flask import Flask

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TheLoneKobra'
    
    from .views import views
    from .auth import auth 
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app