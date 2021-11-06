# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:16:14 2021

@author: artbo
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    data=request.form
    print(data)
    return render_template("login.html", text="Testing", user="Tim", boolean=True)


@auth.route("/logout")
def logout():
    return"<p>logout<p>"


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method=="POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')
        elif len(first_name) < 2:
            flash("firstName must be greater than 2 character.", category='error')

        elif password1 != password2:
            flash("Passwords don't match.", category='error')

        elif len(password1) < 6:
            flash("Password must be at least 6 characters.", category='error')

        else:
            # add user to database
            new_user=User(email=email, first_name=first_name,password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Accout created! Let's say hello to this EnJoy cooking world!", category="success")


            return redirect(url_for("views.home"))


    return render_template("sign_up.html")
