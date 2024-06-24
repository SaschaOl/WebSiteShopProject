import flask
from shop_page.models import Product
from flask_login import current_user
from .models import Cart
from Shop.settings import database
from bot import send_cart

def show_basket_page():
    if flask.request.method == "POST":
        cart_products = Cart(
            name =  flask.request.form["name"],
            surname = flask.request.form["surname"],
            number_user = flask.request.form["number_user"], 
            email_user = flask.request.form["email_user"],
            city_user = flask.request.form["city_user"],
            nova_poshta = flask.request.form["nova_poshta"],
            additional_wishes = flask.request.form["additional_wishes"],
            price = flask.request.form["price"],
            products = flask.request.form["products"],
            is_done = False,
            canceled = False
        )
        database.session.add(cart_products)
        database.session.commit()

        send_cart()

    list_cart = []
    list_ids = []

    if flask.request.cookies and flask.request.cookies.get(key = "product") != "":
        cookie = flask.request.cookies.get(key = "product").split(" ")
        
        for id_cookie in cookie:
            if id_cookie not in list_ids:
                list_cart.append(Product.query.get(id_cookie))
                list_ids.append(id_cookie)
    
    
    print(list_cart)

    # if current_user.is_admin == True:
    #     admin = True
    return flask.render_template(template_name_or_list = "basket.html", list_cart = list_cart, page = "basket")

