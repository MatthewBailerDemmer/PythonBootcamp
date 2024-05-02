from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=datetime.date.today().strftime("%Y"))

@app.route("/guess/<name>")
def guess(name):
    name = str(name).capitalize()
    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    gender = response.json()["gender"]
    response = requests.get(f"https://api.agify.io?name={name}")
    response.raise_for_status()
    age = response.json()["age"]
    return render_template("NameGuess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
