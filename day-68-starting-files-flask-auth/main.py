from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


login_manager = LoginManager()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
login_manager.init_app(app)
db.init_app(app)


@login_manager.user_loader
def user_loader(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(250))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", is_logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if not current_user.is_authenticated:
        if request.method == "POST":
            try:
                form = request.form
                password = generate_password_hash(form.get("password"), 'pbkdf2:sha256', salt_length=8)
                user_to_add = User(email=form.get("email"), password=password, name=form.get("name"))
                db.session.add(user_to_add)
                db.session.commit()
                login_user(user_to_add)
            except Exception:
                flash("You've already signed up with that email, log in instead!", "email_error")
                return redirect(url_for('login'))
            return redirect(url_for('secrets', name=user_to_add.name))
        return render_template("register.html")
    return redirect(url_for('home', is_logged_in=current_user.is_authenticated))


@app.route('/login', methods=["GET", "POST"])
def login():
    if not current_user.is_authenticated:
        if request.method == "POST":
            form = request.form
            try:
                user = db.session.execute(db.select(User).where(User.email == form.get("email"))).scalar_one()
                correct_password = check_password_hash(user.password, form.get("password"))
                if correct_password:
                    login_user(user)
                    return redirect(url_for('secrets', name=user.name))
                else:
                    flash("Incorrect password", "password_error")
            except Exception:
                flash("User email not found", "email_error")
        return render_template("login.html")
    return redirect(url_for('home', is_logged_in=current_user.is_authenticated))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/secrets', methods=["GET"])
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, is_logged_in = current_user.is_authenticated)


@app.route('/download', methods=["GET"])
@login_required
def download():
    return send_from_directory("static/files", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
