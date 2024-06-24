import flask_login
from .settings import shop_project
from registration_page.models import User

shop_project.secret_key = "1234567890"

login_manager = flask_login.LoginManager(shop_project)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)