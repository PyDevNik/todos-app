import sys
from flask_login import login_user, logout_user, login_required
from forms.login import LoginForm
from db.schemas import User
from app._app import app, db
from flask import redirect, render_template, flash, request

@app.route("/register", methods=["GET", "POST"])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logged in successfully.')
        data = {"username": form.username.data,
                "password": form.password.data}
        user = User(**data)
        db.add_user(user)
        login_user(user, remember=form.remember_me.data)
        next = request.args.get('next')
        return redirect(next or f"/todos/{user.id}")
    return render_template('signup.html', form = form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logged in successfully.')
        data = {"username": form.username.data,
                "password": form.password.data}
        user = db.get_user(**data)
        login_user(user) 
        next = request.args.get('next')
        return redirect(next or f"/todos/{user.id}")
    return render_template('login.html', form = form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")