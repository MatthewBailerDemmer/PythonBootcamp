from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph<p>'
            '<img width=500 src="https://media4.giphy.com/media/Dg4TxjYikCpiGd7tYs/giphy.webp?cid=790b7611ttdj1p0kj8ouiekfslroy9vbpmcknk53em55e666&ep=v1_gifs_trending&rid=giphy.webp&ct=g">')


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def good_bye():
    return "<p>GoodBye!</p>"


#flask --app hello run
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you ar {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
