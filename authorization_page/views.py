# Importing the rquiered modules
import flask
from Shop.settings import database
from registration_page.models import User
from flask_login import login_user, current_user

# Creating the view function
def show_authorizatiion_page():
    # Checking if the user is authenticated 
    if current_user.is_authenticated:
        # If so, setting is_admin to the value of the user
        is_admin = current_user.is_admin
    else:
        # If not, setting is_admin to False
        is_admin = False

    # As for the beginning setting the password_valid variable to False 
    password_valid = False
    
    # Checking if the server got a request
    if flask.request.method == "POST":
        # Getting the name form the request form
        name = flask.request.form["name"]
        # Getting the password form the request form
        password = flask.request.form["password"]
        
        # Iterating through all the user with matching usernmaes 
        for user in User.query.filter_by(name = name):
            # Checking if the password is also matching
            if user.password == password:
                # Logging the user in
                login_user(user)
                # Then setting the password_valid variable to True 
                password_valid = True
                # Ending the cycle
                break
    else:
        # Then setting the password_valid variable to True, that the user won|t get the warning if they didn't try to authorize
        password_valid = True
    
    # Rendering the template and passing the data needed in it as parameters
    return flask.render_template(
        # Setting the template file name
        template_name_or_list= "authorization.html", 
        password_valid = password_valid, 
        # Passing the current_user.is_authenticated value as context argument
        is_auth = current_user.is_authenticated,
        # Passing the user data of the current user value as context argument
        user_data = User.query.get(current_user.id) if current_user.is_authenticated else None,
        # Passing the is_admin value as context argument
        is_admin = is_admin
    )


