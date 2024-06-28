# Importing required modules
import flask_login
from .settings import shop_project
from registration_page.models import User

# Setting the secret key for rhe seesion (should be changed)
shop_project.secret_key = "1234567890"
# Creating Login Manager instance to work with users
login_manager = flask_login.LoginManager(shop_project)

# Decorator that ckecks if there is any atempt to load a user
@login_manager.user_loader
def load_user(id):
    # Returnig the User object from the database that will represtent the user
    return User.query.get(id)