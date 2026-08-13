from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user, current_user
from ..forms.auth_forms import RegistrationForm,LoginForm
from app.models.user import User
from app.Extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth",__name__)

@auth.route("/")
def index():
    return redirect(url_for("auth.register"))

@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = generate_password_hash(form.password.data)
        user = User(
            username = form.username.data,
            email = form.email.data,
            password_hash = hash_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully.", "success")
        return redirect(url_for("auth.login"))
    return render_template("authentication.html", form = form) 

@auth.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Welcome back!", "success")
            if current_user.is_authenticated:
                return redirect(url_for("main.dashboard"))
        flash("Invalid email or password.", "danger")
    return render_template("login.html", form = form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth.login"))