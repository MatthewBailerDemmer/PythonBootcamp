from flask import Flask
from random import randint

app = Flask(__name__)

RANDOM_NUMBER = randint(0, 9)
@app.route("/")
def main_page():
    return ("<h1><b>Guess a number between 0 and 9</b><h1>"
            "<img src='https://media4.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.webp?cid=790b7611q9mw66dhy4wdpghb2zsextwplrr0tlr3kjdh6n8a&ep=v1_gifs_search&rid=giphy.webp&ct=g'>")


@app.route("/<int:number>")
def check_random(number):
    if number > RANDOM_NUMBER:
        return ("<h1 style='color: blue'>Too high<h1>"
                "<img widith=500 height=500 src='https://media3.giphy.com/media/3o6wrebnKWmvx4ZBio/200.webp?cid=790b76116yav4weizxfjkm1bb09d9mnjseshne04i931ly3x&ep=v1_gifs_search&rid=200.webp&ct=g'>")
    elif number < RANDOM_NUMBER:
        return ("<h1 style='color:red'>Too Low</h1>"
                "<img widith=500 height=500 src='https://media3.giphy.com/media/T1WqKkLY753dZghbu6/giphy.webp?cid=790b76116yav4weizxfjkm1bb09d9mnjseshne04i931ly3x&ep=v1_gifs_search&rid=giphy.webp&ct=g'>")
    else:
        return ("<h1 style='color: green'>You got it!!!</h1>"
                "<img widith=500 height=500 src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHd5YWZ1YjA1bTV3MTJ1MWU0bGZ5ZGRmbHY4aWUyenUzeHgxMHRidyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lnlAifQdenMxW/200.webp'>")


if __name__ == "__main__":
    app.run(debug=True)
