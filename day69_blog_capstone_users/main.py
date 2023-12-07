''' Flask Blog with authentication and Users '''
from datetime import date
from functools import wraps
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
# from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Integer, String, Text, ForeignKey, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginrForm

app = Flask(__name__)
# A secret key that will be used for securely signing the session cookie and
# can be used for any other security related needs by extensions or your application.
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts_day69.db'

# create the db object using the SQLAlchemy constructor and pass a subclass
# of either DeclarativeBase or DeclarativeBaseNoMeta to the constructor


class Base(DeclarativeBase):
    ''' The DeclarativeBase allows for the creation of new declarative bases
        in such a way that is compatible with type checkers:'''
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Define a User table model for all your registered users.


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    blogposts = db.relationship('BlogPost', backref='user', lazy=True)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    subtitle = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# class User(UserMixin, db.Model):
#     __tablename__ = "user"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     username: Mapped[str] = mapped_column(
#         String(250), unique=True, nullable=False)
#     email: Mapped[str] = mapped_column(String(250), unique=True)
#     password: Mapped[str] = mapped_column(String(250), nullable=False)
#     # This will act like a List of BlogPost objects attached to each User.
#     # The "author" refers to the author property in the BlogPost class.
#     posts: Mapped[int] = relationship("BlogPost", back_populates="author")


# # Define the blog table model
# class BlogPost(db.Model):
#     __tablename__ = "blog_posts"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(
#         String(250), unique=True, nullable=False)
#     subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
#     date: Mapped[str] = mapped_column(String(250), nullable=False)
#     body: Mapped[str] = mapped_column(Text, nullable=False)
#     # Create reference to the User object, the "posts" refers to the posts protperty in the User class.
#     author: Mapped["User"]= relationship("User", back_populates="posts")
#     img_url: Mapped[str] = mapped_column(String(250), nullable=False)
#     # Create Foreign Key, "users.id" the users refers to the tablename of User.
#     # author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

# After all models and tables are defined, create the table schema in the
# database. This requires an application context
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    ''' Flask-Login: provied a user_loader callback to reload the user object
        from the user ID stored in the session. It should take the str ID of a
        user, and return the corresponding user object or None. '''
    return User.query.get(int(user_id))
    # return db.get_or_404(User, user_id)
    # user = db.session.execute(db.select(User).where(
    #     User.id == user_id)).scalar_one_or_none
    # return user


def admin_only(func):
    ''' Decorator to only allow admin access '''
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return func(*args, **kwargs)
    return wrapper_function


@app.route('/register', methods=['GET', 'POST'])
def register():
    ''' Use Werkzeug to hash the user's password when creating a new user. '''
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        # check if email already in database
        email = register_form.email.data
        if db.session.execute(db.select(User).where(User.email == email)).scalar():
            flash(f'The email {email} already exists: Login with it.', 'error')
            return redirect(url_for('login'))
        hashed_password = generate_password_hash(
            register_form.password.data, method='pbkdf2:sha256', salt_length=8)
        user = User(
            username=register_form.username.data,
            email=register_form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("register.html", form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' Retrieve a user from the database based on their email.'''
    login_form = LoginrForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            email = login_form.email.data
            user = db.session.execute(db.select(User).where(
                User.email == email)).scalar()

            if user:
                # check password matches database
                if check_password_hash(user.password, password=login_form.password.data):
                    login_user(user)
                    return redirect(url_for('get_all_posts'))
                flash('The password is wrong', 'error')
                return redirect(url_for('login'))
            flash(
                f'The email {email} is not in the database. Register here', 'error')
            return redirect(url_for('register'))
    return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/', methods=['GET', 'POST'])
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
@login_required
def show_post(post_id):
    ''' Allow logged-in users to comment on posts'''
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    print(current_user.username)
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user.username,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user.username
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
