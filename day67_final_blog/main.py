from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

app = Flask(__name__)
# initialize the extention ckeditor for the app
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create FLASK-WTF form


class NewPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('img_url', validators=[URL()])
    body = CKEditorField('Body')
    submit = SubmitField('Submit')

# CONFIGURE TABLE


class BlogPost(Base):
    __tablename__ = 'blog_post'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), unique=True, nullable=False)
    subtitle = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    body = Column(Text, nullable=False)
    author = Column(String(250), nullable=False)
    img_url = Column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    '''Query the database for all the posts. Convert the data to a python list.'''
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/<post_id>')
def show_post(post_id):
    ''' Get an individule post by id '''
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    ''' Create new post '''
    form = NewPost()
    if request.method == 'POST' and form.validate_on_submit():
        now = datetime.datetime.now()
        date_format = now.strftime("%B %d, %Y")
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date=date_format
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    ''' Edit an existing post. If a GET render pre filled out form. If a 
        POST then update database with changes to the pre filled form on submit '''
    requested_post = db.get_or_404(BlogPost, post_id)
    form = NewPost(
        title=requested_post.title,
        subtitle=requested_post.subtitle,
        author=requested_post.author,
        img_url=requested_post.img_url,
        body=requested_post.body
    )
    if request.method == 'POST':
        requested_post.title = form.title.data
        requested_post.subtitle = form.subtitle.data
        requested_post.author = form.author.data
        requested_post.img_url = form.img_url.data
        requested_post.body = form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    return render_template('make-post.html', form=form)

# TODO: delete_post() to remove a blog post from the database


@app.route('/delete/<post_id>')
def delete_post(post_id):
    ''' Delete post with post_id'''
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
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
