from flask import Blueprint,render_template,abort
from flask_login import login_required,current_user
from app.decorators import admin_required

admin = Blueprint("admin",__name__,url_prefix="/admin")

@admin.route("/dashboard")
@login_required
@admin_required
def dashboard():
    return render_template("admin_dashboard.html")