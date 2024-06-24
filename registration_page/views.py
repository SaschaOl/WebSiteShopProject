import flask
from .models import User
from Shop.settings import database
from flask_login import current_user, login_user


def show_registration_page():

    if flask.request.method == 'POST':
        users = User(
            name = flask.request.form["name"],
            email = flask.request.form["email"],
            password = flask.request.form["password"]
        )
        database.session.add(users)
        database.session.commit()
        
        name = flask.request.form["name"]
        password = flask.request.form["password"]
        
        for user in User.query.filter_by(name = name):
            if user.password == password:
                login_user(user)
            else:
                return "Невірний пароль"
        
        # if current_user.is_admin == True:
        #     admin = True
    
    return flask.render_template(template_name_or_list = "registration.html", is_auth = current_user.is_authenticated)