'''' App demonstrating Authentication using flask_login'''
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from flask_login import UserMixin, login_user, LoginManager, login_required, \
    current_user, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f60317fce3ddce0ff27c29fcf28c0b8d73cc16afdd57541f8460ecf1b20e9d2f'
app.config['UPLOAD_FOLDER'] = 'static/files'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)

# configure the app to login wiht LoginManager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    ''' create a user_loader callback'''
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))

    def __repr__(self):
        return f'<User {self.name!r}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Passing True or False if the user is authenticated.
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # check if user email already exists
        email = request.form.get('email')
        user = db.session.execute(
            db.select(User).where(User.email == email)).scalar()
        if user:
            flash('User Email already registered')
            return render_template("login.html")
        # user email doesn't exist
        name = request.form['name']
        password_hash = generate_password_hash(
            request.form['password'], method='pbkdf2:sha256', salt_length=8)
        user = User(
            name=request.form["name"],
            email=request.form['email'],
            password=password_hash
        )
        db.session.add(user)
        db.session.commit()
        # Log in user after registering
        login_user(user)

        # flask.flash('Logged in successfully.')
        return redirect(url_for('secrets', name=name))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' If POST then check credentials and login the user in 
        if GET then render a login form'''
    if request.method == 'POST':
        # Find user by email
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.session.execute(
            db.select(User).where(User.email == email)).scalar()
        if user:
            # check password matches database
            if check_password_hash(user.password, password=password):
                login_user(user)
                return redirect(url_for('secrets'))
        flash('Invalid Email')
        return render_template("login.html")
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    ''' Only logged in user can access the route '''

    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    '''Logout a user'''
    logout_user()
    return redirect(url_for('home'))


@app.route('/download', methods=['GET'])
@login_required
def download():
    '''Only logged in users can download the pdf'''
    return send_from_directory(
        'static', path='files/cheat_sheet.pdf', as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
