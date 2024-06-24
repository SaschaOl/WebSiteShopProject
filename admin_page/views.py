import flask
import os
from flask_login import current_user
from shop_page.models import Product
from Shop.settings import database



def show_page():
    if flask.request.method == "POST":
        print(flask.request.form)
        if flask.request.form.get("delete"):
            database.session.delete(Product.query.get(flask.request.form["delete"]))
            database.session.commit()
        elif flask.request.form.get("create"):
            product = Product(
                name = flask.request.form["name"],
                price = flask.request.form["price"],
                memory_cap = flask.request.form["memory_cap"],
                discount = flask.request.form["discount"],
                picture = flask.request.form["name"] + ".png"                             
            )
            
            image_save = flask.request.files["image"]
            image_save.save(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{product.picture}"))
            
            database.session.add(product)
            database.session.commit()

        else:
            product = Product.query.get(flask.request.form["id"])
            if flask.request.files.get("image"):
                try:
                    os.remove(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{product.picture}"))
                except Exception as e:
                    print(e)
                image = flask.request.files["image"]
                image.save(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{product.picture}"))
                # product.picture = f"{product.name}.png"
            else:
                if flask.request.form["column"] == "name":
                    product.name = flask.request.form["name"]
                elif flask.request.form["column"] == "price":
                    product.price = flask.request.form["name"]
                elif flask.request.form["column"] == "discount":
                    product.discount = flask.request.form["name"]
                elif flask.request.form["column"] == "memory_cap":
                    product.memory_cap = flask.request.form["name"]
                
            database.session.add(product)
            database.session.commit()
            
        # if current_user.is_admin == True:
        #     admin = True
    return flask.render_template(template_name_or_list = "admin.html", page = 'admin', products = Product.query.all())

    