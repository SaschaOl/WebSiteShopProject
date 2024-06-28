# Importing the rquiered modules
import flask, flask_sqlalchemy
# Importing the database instance from the settings file
from Shop.settings import database

# Creating the model class that extends the database.Model template class
class Product(database.Model):
    # Id primary key column, used as the main identifier, aincrement is set to flase to not reuse the ids
    id = database.Column(database.Integer, primary_key = True, autoincrement = False)
    # name stores the name of the product
    name = database.Column(database.String(120), nullable = False)
    # price stores the price value of the product
    price = database.Column(database.Integer, nullable = False)
    # memory_cap stores the memory capacity value of the product
    memory_cap = database.Column(database.Integer, nullable = False)
    # discound stores the discound value of the product
    discount = database.Column(database.Integer, nullable = False)
    # picture stores the picture file name of the product
    picture = database.Column(database.String(120), nullable = False)