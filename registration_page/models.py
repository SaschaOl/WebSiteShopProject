# importing the rquired modules
import flask, flask_sqlalchemy
# Importing the database instance from the settings file
from Shop.settings import database
# Importing the UserMixin class that is used to make the model adapted to work with flask login 
from flask_login import UserMixin

# Creating the model class that extends the database.Model and UserMixin templates classes
class User(database.Model, UserMixin):
    # Id primary key column, used as the main identifier
    id = database.Column(database.Integer, primary_key = True)
    # name sotres the name of the user
    name = database.Column(database.String(60), nullable = False)
    # password strores the password of the user
    email = database.Column(database.String(60), nullable = False)
    # email strores the email of the user
    password = database.Column(database.String(60), nullable = False)
    # Stores the boolean value tha defines if the user is an admin
    is_admin = database.Column(database.Boolean, nullable = False)
    # Stores the boolean value tha defines if the user has a pending order
    order_pending = database.Column(database.Boolean, nullable = False)