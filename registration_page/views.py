# Importing the rquiered modules
import flask
from .models import User
from Shop.settings import database
from flask_login import current_user, login_user

# Creating the view function
def show_registration_page():

    # Checking if the server got a request
    if flask.request.method == 'POST':
        # Creating a datebase record for the new user
        users = User(
            name = flask.request.form["name"],
            email = flask.request.form["email"],
            password = flask.request.form["password"],
            is_admin = False,
            order_pending = False
        )
        # Adding the record to session
        database.session.add(users)
        # Commiting the changes
        database.session.commit()

        # Setting the variable that is used to define if a new user got registred to True     
        is_registred = True
    else:
        # Setting the variable that is used to define if a new user got registred to False
        is_registred = False

    # Checking if the user is authenticated 
    if current_user.is_authenticated:
        # If so, setting is_admin to the value of the user
        is_admin = current_user.is_admin
    else:
        # If not, setting is_admin to False
        is_admin = False

    # Rendering the template and passing the data needed in it as parameters
    return flask.render_template(
        # Setting the template file name
        template_name_or_list = "registration.html",
        # Passing the is_registred value as context argument
        is_registred = is_registred,
        # Passing the current_user.is_authenticated value as context argument
        is_auth = current_user.is_authenticated, 
        # Passing the user data of the current user value as context argument
        user_data = User.query.get(current_user.id) if current_user.is_authenticated else None,
        # Passing the is_admin value as context argument
        is_admin = is_admin
    )