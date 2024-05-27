from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ckeditor = CKEditor(app)


class PostForm(FlaskForm):
    title = StringField('Post title', validators=[DataRequired()])
    subtitle = StringField("Post subtitle", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/add_new_post", methods=["POST", "GET"])
def add_new_post():
    form = PostForm()
    print(form.data)
    if form.validate_on_submit():
        try:
            new_post = BlogPost(title=form.title.data, subtitle=form.subtitle.data, date=date.today().strftime("%B %d,%Y"),
                                body=form.body.data, author=form.author.data, img_url=form.img_url.data)
            db.session.add(new_post)
            db.session.commit()
        except Exception as e:
            return str(e)
        else:
            return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    form = PostForm()
    post_to_update = db.get_or_404(BlogPost, post_id)
    if form.validate_on_submit():
        print("entrei")
        post_to_update.title = form.title.data
        post_to_update.subtitle = form.subtitle.data
        post_to_update.author = form.author.data
        post_to_update.img_url = form.img_url.data
        post_to_update.body = form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_to_update.id))
    else:
        form = PostForm(
            title=post_to_update.title,
            subtitle=post_to_update.subtitle,
            img_url=post_to_update.img_url,
            author=post_to_update.author,
            body=post_to_update.body
        )
        print(form.data)
        return render_template("make-post.html", form=form, post_id=post_to_update.id)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
