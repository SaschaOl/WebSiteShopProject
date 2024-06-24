import flask
from flask_login import current_user
from .models import Product
from Shop.settings import database



def show_page():
    # product = Product(
    #     name = "iPhone 15 Pro Max 1TB Natural Titanium",
    #     price = "69 999",
    #     memory_cap = "1 TB",
    #     discount = 20,
    #     picture = "phone"
    # )  
    # product1 = Product(
    #     name = "Samsung Galaxy S23 Ultra 12/256GB ",
    #     price = "49 999",
    #     memory_cap = "256 GB",
    #     discount = 10,
    #     picture = "phone"
    # ) 
    # product2 = Product(
    #     name = "Apple MacBook Pro 13 Space Gray M2 8/256GB",
    #     price = "54 999",
    #     memory_cap = "256 GB",
    #     discount = 0,
    #     picture = "phone"
    # ) 
    # product3 = Product(
    #     name = "Apple Watch Ultra 49mm Titanium",
    #     price = "28 999",
    #     memory_cap = "128 GB",
    #     discount = 0,
    #     picture = "phone"
    # )    
    # database.session.add(product)
    # database.session.add(product1)
    # database.session.add(product2)
    # database.session.add(product3)
    # database.session.commit()

    # if current_user.is_admin == True:
    #     admin = True

    return flask.render_template(template_name_or_list = "shop.html", products = Product.query.all(), page = 'shop')

    