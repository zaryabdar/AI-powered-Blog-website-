from flask import Blueprint, render_template, redirect, url_for, flash,current_app,request
from flask_login import login_required, logout_user, login_user, current_user
from app.forms.auth_forms import RegistrationForm,LoginForm,EditProfileForm
from app.models.user import User
from app.Extensions import db
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os

auth = Blueprint("auth",__name__)


@auth.route("/register", methods=["GET","POST"])
def register():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        hash_password = generate_password_hash(registration_form.password.data)
        user = User(
            username = registration_form.username.data,
            email = registration_form.email.data,
            password_hash = hash_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully.", "success")
        return redirect(url_for("auth.login"))
    login_form = LoginForm()
    return render_template("authentication.html", registration_form = registration_form, login_form = login_form) 

@auth.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email= login_form.email.data).first()
        if user and check_password_hash(user.password_hash, login_form.password.data):
            login_user(user, remember=login_form.remember_me.data)
            flash("Welcome back!", "success")
            if current_user.is_authenticated:
                return redirect(url_for("post.all_posts"))
        flash("Invalid email or password.", "danger")
    registration_form = RegistrationForm()
    return render_template("authentication.html",registration_form = registration_form, login_form = login_form)

@auth.route("/profile")
@login_required
def profile():
    return render_template("profile.html",user = current_user)

@auth.route("/profile-edit", methods =["GET","POST"])
def update_profile():
    form = EditProfileForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.bio = form.bio.data
        image = form.profile_img.data
        if image:
            filename = secure_filename(image.filename)
            upload_folder = os.path.join(current_app.static_folder,"uploads")

            os.makedirs("upload_folder", exist_ok=True)
            image.save(os.path.join(upload_folder,filename))

            current_user.profile_img =filename

        db.session.commit()
        flash("Profile updated Successfully","success")
        return redirect(url_for("auth.profile"))
    if request.method == "GET":
        form.username.data = current_user.username
        form.bio.data = current_user.bio
    return render_template("edit_profile.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth.login"))