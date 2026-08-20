from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms.fields import StringField, TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

class CreatePostForm(FlaskForm):
    title = StringField("Title",validators=[DataRequired(),Length(min=8,max=100)])
    summary = TextAreaField("Summary",validators=[DataRequired(),Length(min=50,max=300)])
    content = TextAreaField("Content",validators=[DataRequired(),Length(min=100)])
    cover_image = FileField("Cover Image",validators=[FileAllowed(["jpg","jpeg","png"], "Images only!")])
    submit = SubmitField("Publish Post")


class UpdatePostForm(FlaskForm):
    title = StringField("Title",validators=[DataRequired(),Length(min=8,max=100)])
    summary = TextAreaField("Summary",validators=[DataRequired(),Length(min=50,max=300)])
    content = TextAreaField("Content",validators=[DataRequired(),Length(min=100)])
    cover_image = FileField("Cover Image",validators=[FileAllowed(["jpg","jpeg","png"], "Images only!")])
    submit = SubmitField("Update Post")
