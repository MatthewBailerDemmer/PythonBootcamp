import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Float, String, DateTime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import json
from datetime import datetime

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

TOKEN_BEARER = ("eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjOTgzNjMyZTA5NjY4NWY3O"
                "TM4NWFlNmRhOGFhOGQxYyIsInN1YiI6IjY2NGY2YTcxYmMyMjhiZWI5MjA2N"
                "TFlMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OtOpNk"
                "yXdw6ZU2F4XypBG1dDjBftDJhKndfvFhoLoi4")


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///movies.db'
db.init_app(app)

global movie_data


# CREATE TABLE
class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# with app.app_context():
#     new_movie = Movies(title="Phone Booth", year=datetime.datetime(2020, 6, 1),
#                       description="Publicist Stuart Shepard finds himself trapped in a phone booth,"
#                                   " pinned down by an extortionist's sniper rifle. Unable to leave or "
#                                   "receive outside help, Stuart's negotiation with the caller leads to a"
#                                   " jaw-dropping climax.",
#                       rating="☆☆☆", ranking=10, review="My favourite character was the caller.",
#                       img_url="https://m.media-amazon.com/images/M/MV5BY2NkMjRhODMtYWRjYi00M2YwLTlmNGEtYzVkOWI4YmE4ZmEwXkEyXkFqcGdeQXVyMTUzMDUzNTI3._V1_.jpg")
#     db.session.add(new_movie)
#     db.session.commit()

class MovieForm(FlaskForm):
    rating = FloatField(label="Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddMovieForm(FlaskForm):
    title = StringField("Title")
    submit = SubmitField("Add Movie")


def rating_to_stars(rating):
    n_stars = int(rating / 2)
    stars = ""
    for i in range(n_stars):
        stars += "★"
    return stars


@app.route("/", methods=["GET", "POST"])
def home():
    movie_id = request.args.get("id")
    action = request.args.get("action")
    if movie_id is not None:
        if action == "delete":
            with app.app_context():
                movie_to_delete = db.get_or_404(Movies, movie_id)
                db.session.delete(movie_to_delete)
                db.session.commit()
        else:
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {TOKEN_BEARER}"
            }
            response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", headers=headers)
            response.raise_for_status()
            data = response.json()
            new_movie = Movies(id=movie_id, title=data["title"],
                               year=datetime.strptime(data["release_date"], "%Y-%m-%d"),
                               description=data["overview"],
                               img_url=f"https://image.tmdb.org/t/p/original{data['poster_path']}",
                               rating=0, review="", ranking=0)
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for("edit_movie", movie_id=movie_id))
    movies = list(db.session.execute(db.select(Movies).order_by(Movies.rating.desc())).scalars())
    for movie in movies:
        movie_to_update = db.get_or_404(Movies, movie.id)
        movie_to_update.ranking = movies.index(movie) + 1
        db.session.commit()
    return render_template("index.html", movies=movies, rating_to_stars=rating_to_stars)


@app.route("/edit", methods=["GET", "POST"])
def edit_movie():
    form = MovieForm()
    movie_id = request.args.get("movie_id")
    movie_to_edit = db.get_or_404(Movies, movie_id)
    if form.validate_on_submit():
        if form.rating.data != "":
            movie_to_edit.rating = form.rating.data
        if form.review.data != "":
            movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=form, movie=movie_to_edit)


@app.route("/add", methods=["GET", "POST"])
def add():
    global movie_data
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        params = {
            "query": movie_title,
            "Language": "English",
            "Page": 1
        }
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TOKEN_BEARER}"
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=params, headers=headers)
        response.raise_for_status()
        movie_data = response.json()["results"]
        return redirect("/select")
    return render_template("add.html", form=form)


@app.route("/select")
def select():
    return render_template("select.html", movies=movie_data)


if __name__ == '__main__':
    app.run(debug=True)
