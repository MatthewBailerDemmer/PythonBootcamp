from flask import Flask
import random
app = Flask(__name__)

print(random.__name__)
print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def good_bye():
    return "<p>GoodBye!</p>"
#flask --app hello run

if __name__ == "__main__":
    app.run()