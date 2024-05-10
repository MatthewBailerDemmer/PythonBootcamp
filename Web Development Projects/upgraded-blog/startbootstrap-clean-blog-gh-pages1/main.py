from flask import Flask, render_template, request
import requests
import smtplib

my_email = "matheusbailerdemmer@gmail.com"
password = "password"

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/171284d078e16adefede")
    response.raise_for_status()
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts/<int:num>")
def get_post(num):
    response = requests.get("https://api.npoint.io/171284d078e16adefede")
    response.raise_for_status()
    all_posts = response.json()
    return render_template("post.html", post=all_posts[int(num) - 1])


@app.route("/contact", methods=["GET", "POST"])
def contact():
    flag = False
    if request.method == "POST":
        send_email(request.form['name'], request.form["email"], request.form["phone"], request.form["message"])
        flag = True
    return render_template("contact.html", flag=flag)


def send_email(name, emai, phone, message):
    send_message = f" Name: {name} \n Email: {emai} \n Phone: {phone} \n Message: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Message sent through blog\n\n{send_message}")


if __name__ == "__main__":
    app.run(debug=True)
