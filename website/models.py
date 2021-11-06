# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:16:38 2021

@author: artbo
"""
from . import db
from flask_login import UserMixin
from sqlalchemy import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    #   user.id пишется с маленькой буквы, так как мы используем db.ForeignKey
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Note пишется с большой буквы так как мы пишем название класса в db.relationship
    # db.relationship испольхуется тогда,
    # когда мы должны настроить множественное отнощение( Один пользователь имеет много постов)
    notes = db.relationship('Note')
