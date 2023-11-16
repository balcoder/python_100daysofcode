''' Library book tracker and rating app '''
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy import Integer, String, Float

# First create the db object using the SQLAlchemy constructor.
# Pass a subclass of either DeclarativeBase or DeclarativeBaseNoMeta to the constructor


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
# sqlite followed by 3 forward slashes means relative path or present
# working directory, 4 forward slashes means full or absolute path
# (e.g. sqlite:////usr/local/flask/database/example.db)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
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


@app.route('/')
def home():
    # books = db.session.execute(db.select(Books).order_by(Books.id)).scalars()
    # print(books)
    # if len(books) == 0:
    #     return render_template('index.html', data=None)
    # return render_template('index.html', data=books)
    books = db.session.query(Books).all()
    if not books:  # Check if the books list is empty
        return render_template('index.html', data=None)
    return render_template('index.html', data=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # create new record
        new_book = Books(
            title=request.form['name'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
@app.route("/edit", methods=['POST'])
def edit(book_id):
    book = db.get_or_404(Books, book_id)
    if request.method == 'POST':
        book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", data=book)


@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    book = db.get_or_404(Books, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
