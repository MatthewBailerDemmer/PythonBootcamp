from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    all_posts: object = response.json()
    print(all_posts)
    return render_template("index.html", posts=all_posts)


@app.route('/<int:num>')
def get_post(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    all_posts: object = response.json()
    return render_template("post.html", post=all_posts[num - 1])


if __name__ == "__main__":
    app.run(debug=True)
