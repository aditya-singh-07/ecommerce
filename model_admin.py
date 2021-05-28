from datetime import datetime

from . import db
from flask_login import UserMixin


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # vehicledata = db.relationship('VehicleData', backref='author', lazy=True)

    def __init__(self, fname, lname, username, email, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.email = email
        self.password = password


class Apparels(db.Model):
    apparel_id = db.Column(db.Integer, primary_key=True)
    apparel_name = db.Column(db.String(100), nullable=False)
    brand_name = db.Column(db.String(100), nullable=False)
    shop_name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=True)
    material_type = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    occasion_type = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    items_remaining = db.Column(db.Integer, nullable=False)
    items_sold = db.Column(db.Integer, nullable=False)

    def __init__(self, apparel_name, brand_name, shop_name, image, material_type, color, occasion_type, gender, Price,
                 items_remaining, items_sold):
        self.apparel_name = apparel_name
        self.brand_name = brand_name
        self.shop_name = shop_name
        self.image = image
        self.material_type = material_type
        self.color = color
        self.occasion_type = occasion_type
        self.gender = gender
        self.Price = Price
        self.items_remaining = items_remaining
        self.items_sold = items_sold


class Movies(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True, nullable=False)
    movie_name = db.Column(db.String(100), nullable=False)
    movie_description=db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    movie_poster = db.Column(db.String(100), nullable=False)
    director_name = db.Column(db.String(100), nullable=True)
    actors = db.Column(db.String(100), nullable=False)
    review = db.Column(db.String(100), nullable=False)

    def __init__(self, movie_name,movie_description, genre, movie_poster, director_name, actors, review):
        self.movie_name = movie_name
        self.movie_description=movie_description
        self.genre = genre
        self.movie_poster = movie_poster
        self.director_name = director_name
        self.actors = actors
        self.review = review

class Order(db.Model, UserMixin):
    order_id = db.Column(db.Integer, primary_key=True)
    apparel_id=db.Column(db.Integer, db.ForeignKey('apparels.apparel_id'),
              nullable=False)
    apparels = db.relationship('Apparels', backref='author', lazy=True)

    def __init__(self, apparels_id, apparels):
        self.apparels_id = apparels_id
        self.apparels = apparels

# class VehicleData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     vehicle = db.Column(db.String(50), nullable=False)
#     model = db.Column(db.String(50), nullable=False)
#     color = db.Column(db.String(50), nullable=False)
#     type = db.Column(db.String(50), nullable=False)
#     number_plate = db.Column(db.String(100), nullable=False)
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#
#     def __init__(self, user_id, vehicle, model, color, type, number_plate, date_created):
#         self.user_id = user_id
#         self.vehicle = vehicle
#         self.model = model
#         self.color = color
#         self.type = type
#         self.number_plate = number_plate
#         self.date_created = date_created
