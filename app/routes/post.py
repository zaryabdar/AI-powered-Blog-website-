from flask import Blueprint,render_template,url_for,redirect,flash,request,abort, current_app
from flask_login import login_required,current_user
from app.Extensions import db
from app.models.post import Post
from app.forms.post_forms import CreatePostForm,UpdatePostForm
from werkzeug.utils import secure_filename
import os


post =Blueprint("post",__name__)

@post.route("/")
def home():
    posts = Post.query.filter_by(is_published=True).order_by(Post.created_at.desc()).all()
    return render_template("templates/home.html", posts = posts)

@post.route("/posts")
def all_posts():
    posts = Post.query.all()
    return render_template("posts.html",posts=posts)

@post.route("/post/new",methods=["GET","POST"])
@login_required
def create_post():
    form = CreatePostForm()
    print("Form VALIDATED")

    if form.validate_on_submit():
        post =Post(
            title = form.title.data,
            slug = "temporary slug",
            summary = form.summary.data,
            content = form.content.data,
            cover_img = None,
            author_id =current_user.id
        )

        image = request.files.get("cover_image")
        if image and image.filename:
            filename = secure_filename(image.filename)

            upload_folder = os.path.join(
                current_app.static_folder,
                "uploads"
            )
            os.makedirs(upload_folder, exist_ok=True)
            image.save(os.path.join(upload_folder,filename))
            post.cover_img = filename
        db.session.add(post)
        db.session.commit()
        print("POST SAVED:", post.id)
        flash("Post Uploaded Successfully","success")
        return redirect(url_for("post.all_posts"))
    print("FORM ERRORS:", form.errors)
    return render_template("create_post.html",form = form)

@post.route("/post/<int:id>/edit",methods=["GET","POST"])
@login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    if post.author_id != current_user.id:
        abort(403)
    form =UpdatePostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.slug = "New temporary slug"
        post.summary = form.summary.data
        post.content = form.content.data
        post.cover_img = None
        db.session.commit()
        flash("Post Updated Successfully","success")
        return redirect(url_for("post.all_posts"))
    if request.method == "GET":
        form.title.data = post.title
        form.summary.data = post.summary
        form.content.data = post.content
    return render_template("edit_post.html",form=form)

@post.route("/post/<int:id>/delete",methods=["POST"])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash("Post Deleted Successfully","success")
    return redirect(url_for("post.all_posts"))