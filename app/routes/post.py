from flask import Blueprint,render_template,url_for,redirect,flash,request,abort
from flask_login import login_required,current_user
from app.Extensions import db
from app.models.post import Post
from app.forms.post_forms import CreatePostForm,UpdatePostForm


post =Blueprint("post",__name__)

@post.route("/posts")
def all_posts():
    posts = Post.query.all()
    return render_template("posts.html",posts=posts)

@post.route("/post/new",methods=["GET","POST"])
@login_required
def create_post():
    form = CreatePostForm()

    if form.validate_on_submit():
        post =Post(
            title = form.title.data,
            slug = "temporary slug",
            summary = form.summary.data,
            content = form.content.data,
            cover_img = None,
            author_id =current_user.id
        )
        db.session.add(post)
        db.session.commit()
        flash("Post Uploaded Successfully","success")
        return redirect(url_for("post.all_posts"))

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