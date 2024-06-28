# Importing the required modules 
import flask, sqlalchemy
# Importing the database instance from the settings file
from Shop.settings import database

# Creating the model class that extends the database.Model template class
class Cart(database.Model):
    # Id primary key column, used as the main identifier
    id = database.Column(database.Integer, primary_key = True)
    # user_id column stores id of the user who did this order
    user_id = database.Column(database.Integer, nullable = True)
    # name stores the name of that user
    name = database.Column(database.String, nullable = False)
    # surname stores the surname of that user
    surname = database.Column(database.String, nullable = False)
    # number_user stores the phone number of that user
    number_user = database.Column(database.Integer, nullable = False)
    # email_user stores the email of that user
    email_user = database.Column(database.String, nullable = False)
    # city_user stores the city of that user
    city_user = database.Column(database.String, nullable = False)
    # nova_poshta stores the chosen nova post site of that user
    nova_poshta = database.Column(database.String, nullable = False)
    # additional_wishes stores the entered additional wishes of that user
    additional_wishes = database.Column(database.String, nullable = False)
    # price stores the total price of the order
    price = database.Column(database.Integer, nullable = False)
    # products stores the list of ids if ordered products
    products = database.Column(database.String, nullable = False)
    # is_done shows if the order is done
    is_done = database.Column(database.Boolean, nullable = False)#
    # is canceled shows if the order is canceled
    canceled = database.Column(database.Boolean, nullable = False)
    
    