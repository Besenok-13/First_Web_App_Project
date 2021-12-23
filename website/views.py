# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:16:55 2021

@author: artbo
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note=request.form.get("note")
        if len(note) < 1:
            flash("Напиши хотя-бы один символ, лол", category="error")
        else:
            new_note=Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("какой молодчинка, твоя запись была добавлена)", category="success")

    return render_template("home.html",user=current_user)

@views.route("/delete-note",methods=["POST"])
def delete_note():
    note=json.loads(request.data)
    noteId=note['noteId']
    note=Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
"""
Всё что идёт дальше - бред гения, или просто бред, смотря по работоспособности.
НАСТОЯТЕЛЬНО НЕ СОВЕТУЮ ЧТО-ЛИБО МЕНЯТЬ, ибо только я знаю, что в каком костыле используется.
Приятного чтения и поменьше крови из глаз.
"""
@views.route("/posts")
def posts():
    users = User.query.order_by(User.id).all()
    return render_template("posts.html",users=users, user=current_user)


@views.route("/userpost/<int:noteId>/delete")
def post_del(noteId):
    note=Note.query.get(noteId)
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()
        else:
            flash("Ты чорт, чо делаешь не в своём аккаунте?", category="error")
    return redirect(url_for("views.home"))
