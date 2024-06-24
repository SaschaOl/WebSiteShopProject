import flask
from flask_login import current_user, logout_user
import flask_login
from registration_page.models import User


def show_home_page():
    # if current_user.is_admin == True:
    #     admin = True

    return flask.render_template(
        template_name_or_list = "index.html",
        is_auth = current_user.is_authenticated,
        user_data = User.query.get(current_user.id) if current_user.is_authenticated else None,
        page = "home"
    )