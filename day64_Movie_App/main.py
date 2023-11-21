''' Movie App with SQLite database that we can search for movie
    using the TMDB api and CRUD the movie to our database using
    our API. Movies get a rating so you can see your top movies'''
import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


load_dotenv()
TMDB_TOKEN = os.getenv('TMDB_TOKEN')

# create the Flask WTForms


class MovieForm(FlaskForm):
    rating = StringField(label='Your Rating out of 10, e.g. 7.5', validators=[
                         DataRequired(message='Needs a rating 10 - 0')])
    review = StringField(label='Your Review', validators=[
                         DataRequired(message='Write short review')])
    submit = SubmitField(label='Update')


class AddMovie(FlaskForm):
    movie = StringField(label='Movie Title', validators=[
        DataRequired(message='Needs a Movie Title')])
    submit = SubmitField(label='Add Movie')


# Create the db object
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
# initialize the app with the extension
db.init_app(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# initialize the Bootstrap5 extension on the app
bootstrap = Bootstrap5(app)


class Movie(db.Model):
    ''' Define the Movie model class
        Need to subclass db.Model to define a model class that represents the Movie table
    '''
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[String] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[Text] = mapped_column(Text, nullable=False)
    rating: Mapped[Float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[Text] = mapped_column(Text, nullable=True)
    img_url: Mapped[String] = mapped_column(String, nullable=False)


# Create the table schema in the database. You need to call db.create_all()
with app.app_context():
    db.create_all()


def create_movie(data):
    ''' Given request.form data, add movie to database '''
    # "poster_sizes": "w92","w154","w185","w342","w500","w780","original"
    base_img_url = "https://image.tmdb.org/t/p/w342/"
    movie = Movie(
        title=data['original_title'],
        year=data['release_date'],
        description=data['overview'],
        img_url=base_img_url + data['poster_path']
    )
    # add the movie object to the session
    db.session.add(movie)
    # commit the changes to the database
    db.session.commit()
    return movie.id


def get_moviesdb(title):
    ''' Query the TMDB for a title of a movie and return a list of movie dicts '''
    url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    response = requests.get(url, headers=headers, timeout=10)
    data = response.json()
    results = data['results']
    for movie in results:
        movies = [{'id': movie['id'], 'title': movie['original_title'],
                   'year': movie['release_date']}for movie in results]
    return movies


def get_moviedb(movie_id):
    ''' Get the movie details from TMDB for a given movie id add to database
        and return the primary key of movie just added '''
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }
    response = requests.get(url, headers=headers, timeout=10)
    data = response.json()
    primary_key = create_movie(data)
    return primary_key


@app.route("/")
def home():
    ''' Gets all the movies in database and renders to index.html '''
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars().all()
    for idx, movie in enumerate(all_movies):
        movie.ranking = idx + 1
    db.session.commit()
    return render_template('index.html', movies=all_movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    ''' Uses WTForm to search for movie title and give list of movies with
        that word to to select.html '''
    add_form = AddMovie()
    if request.method == 'POST':
        title = add_form.movie.data
        movies = get_moviesdb(title)
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=add_form)


@app.route("/select")
def select():
    ''' Shows a list of movies to select from '''
    return render_template('select.html')


@app.route('/get-movie/<int:movie_id>')
def get_movie(movie_id):
    ''' takes the movie you select and passes the  TMDB id to rate_movie route /edit'''
    primary_key = get_moviedb(movie_id)
    return redirect(url_for('rate_movie', id=primary_key))


@app.route('/edit', methods=['GET', 'POST'])
def rate_movie():
    ''' Update movie by its primary key  '''
    movie_form = MovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if movie_form.validate_on_submit():
        rating = movie_form.rating.data
        review = movie_form.review.data
        movie.rating = rating
        movie.review = review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=movie_form)


@app.route('/delete', methods=['GET', 'POST'])
def delete_movie():
    ''' Delete movie by primary key'''
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
