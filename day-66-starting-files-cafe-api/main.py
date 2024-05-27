from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import random, choice

TOP_SECRET_API_TOKEN = "TopSecretApiToken"
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random():
    with app.app_context():
        cafes = list(db.session.execute(db.select(Cafe)).scalars())
        cafe = choice(cafes)
        return jsonify(cafe={
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
            "has_sockets": cafe.has_sockets,
            "has_wifi": cafe.has_wifi,
            "id": cafe.id,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "map_url": cafe.map_url,
            "name": cafe.name,
            "seats": cafe.seats
        })


@app.route("/all")
def get_all():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    # This uses a List Comprehension but you could also split it into 3 lines.
    return jsonify(
        cafes=[{column.name: getattr(cafe, column.name) for column in cafe.__table__.columns} for cafe in all_cafes])


@app.route("/search", methods=["GET"])
def search():
    loc = request.args.get("loc")
    try:
        cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
        if cafes:
            return jsonify(
                cafes=[{column.name: getattr(cafe, column.name) for column in cafe.__table__.columns} for cafe in
                       cafes])
        else:
            raise Exception("Couldn´t find caffe")
    except Exception:
        return jsonify({"error": {
            "Not found": "Sorry we don´t have a cafe in that location"
        }})


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    cafe = request.form
    try:
        new_cafe = Cafe(name=cafe.get("name"), map_url=cafe.get("map_url"), img_url=cafe.get("img_url"),
                        location=cafe.get("location"), seats=cafe.get("seats"), has_toilet=bool(cafe.get("has_toilet")),
                        has_wifi=bool(cafe.get("has_wifi")), has_sockets=bool(cafe.get("has_sockets")),
                        can_take_calls=bool(cafe.get("can_take_calls")),
                        coffee_price=cafe.get("coffee_price"))
        db.session.add(new_cafe)
        db.session.commit()
    except Exception as e:
        return jsonify({"response": {
            "error": str(e)
        }})
    return jsonify({"response": {
        "success": "Successfully added the new cafe."
    }})


# HTTP PUT/PATCH - Update Record
@app.route("/updated_price/<caffe_id>", methods=["PATCH"])
def update_price(caffe_id):
    try:
        cafe_to_update = db.get_or_404(Cafe, caffe_id)
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({"error": {
            "Not Found": "Sorry but a cafe with that id was not found in our database"
        }})
    return jsonify({"success": "Successfully updated the price"})


# HTTP DELETE - Delete Record
@app.route("/report_closed/<int:caffe_id>", methods=["DELETE"])
def report_closed(caffe_id):
    try:
        cafe_to_delete = db.get_or_404(Cafe, caffe_id)
        api_key = request.args.get("api-key")

        if api_key != TOP_SECRET_API_TOKEN:
            return jsonify(error="Invalid API key"), 403

        db.session.delete(cafe_to_delete)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({"error": {
            "Not Found": "Sorry but a cafe with that id was not found in our database"
        }}), 400
    return jsonify({"success": "Cafe successfully deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
