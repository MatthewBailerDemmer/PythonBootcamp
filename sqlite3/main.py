#import sqlite3
#
# db = sqlite3.connect("book-collection.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
# #                "title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL,"
# #                " rating FLOAT NOT NULL)")
#
# cursor.execute("UPDATE books SET rating='★★★★★' WHERE id=1")
# db.commit()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[str] = mapped_column(String(5), nullable=False)


with app.app_context():
    db.create_all()

with app.app_context():
    new_book = Books(id=1, title="Harry Potter", author="J.K. Rowling", rating="★★★★★")
    db.session.add(new_book)
    db.session.commit()

with app.app_context():
    new_book = Books(title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()

with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()

with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Books, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()