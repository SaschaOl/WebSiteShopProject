import flask, sqlalchemy
from Shop.settings import database

class Cart(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String, nullable = False)
    surname = database.Column(database.String, nullable = False)
    number_user = database.Column(database.Integer, nullable = False)
    email_user = database.Column(database.String, nullable = False)
    city_user = database.Column(database.String, nullable = False)
    nova_poshta = database.Column(database.String, nullable = False)
    additional_wishes = database.Column(database.String, nullable = False)
    price = database.Column(database.Integer, nullable = False)
    products = database.Column(database.String, nullable = False)
    is_done = database.Column(database.Boolean, nullable = False)
    canceled = database.Column(database.Boolean, nullable = False)
    
    