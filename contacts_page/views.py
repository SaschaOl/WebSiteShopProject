# Importing the rquiered modules
import flask
from flask_login import current_user
from registration_page.models import User

# Creating the view function
def show_contacts_page():
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
        template_name_or_list = "contacts.html", 
        # Passing the current page name as context argument
        page = 'contacts', 
        # Passing the current_user.is_authenticated value as context argument
        is_auth = current_user.is_authenticated,
        # Passing the user data of the current user value as context argument
        user_data = User.query.get(current_user.id) if current_user.is_authenticated else None,
        # Passing the is_admin value as context argument
        is_admin = is_admin
        )