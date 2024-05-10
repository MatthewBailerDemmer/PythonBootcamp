from flask import Flask, render_template, request
import requests
import smtplib

my_email = "matheusbailerdemmer@gmail.com"
password = "password"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    flag = False
    if request.method == "POST":
        send_email(request.form['name'], request.form["email"], request.form["phone"], request.form["message"])
        flag = True
    return render_template("contact.html", flag=flag)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def send_email(name, emai, phone, message):
    send_message = f" Name: {name} \n Email: {emai} \n Phone: {phone} \n Message: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Message sent through blog\n\n{send_message}")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
