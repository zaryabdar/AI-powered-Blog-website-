from flask import Blueprint,render_template,url_for,redirect,flash,request,abort
from flask_login import login_required,current_user
from Extensions import db
from models.post import Post
from forms.post_forms import CreatePostForm,UpdatePostForm


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

@post.route("/post/<int>id>/edit",methods=["GET","POST"])
@login_required
def update_post(id):
    post = Post.query.filter_by(id =id).first()
    if post.author_id != current_user.id:
        abort(403)
    form =UpdatePostForm()
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


    