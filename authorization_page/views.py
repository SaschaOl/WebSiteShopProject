import flask
from Shop.settings import database
from registration_page.models import User
from flask_login import login_user, current_user

password_valid = True

def show_authorizatiion_page():
    
    global password_valid
    
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        password = flask.request.form["password"]
        print(User.query.filter_by(name = name))
        
        for user in User.query.filter_by(name = name):
            if user.password == password:
                login_user(user)
                break
            else:
                print("wrong password")
                password_valid = False
        else:
            password_valid = False
        # if current_user.is_admin == True:
        #     admin = True
    return flask.render_template(template_name_or_list= "authorization.html", password_valid = password_valid)


