import sqlite3
from flask import Flask
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from flask_sqlalchemy import SQLAlchemy


# # create a connection to a databse, if it dosen't exist it will be created
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute(
#     "INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
# db.commit()

# create the extension
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


# define the model
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(
        String(250), unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(Float, unique=False, nullable=False)


# provide the Flask "app context" and create the schema in the database
with app.app_context():
    db.create_all()

# create record
with app.app_context():
    book = Books(title='Harry Potter', author='J.K Rowling', rating=9.3)
    db.session.add(book)
    db.session.commit()
