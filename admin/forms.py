from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField,TextAreaField,FileField


class BlogForm(FlaskForm):
    blog_title = StringField('Title')
    blog_image = FileField('Photo')
    blog_content = TextAreaField('Content')
    submit = SubmitField()


