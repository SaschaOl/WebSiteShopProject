# Importing the rquiered modules
import flask
import os
from flask_login import current_user
from shop_page.models import Product
from registration_page.models import User
from Shop.settings import database

# Creating the view function
def show_page():
    
    # Checking if the server got a request
    if flask.request.method == "POST":
        # Checking if the form contains the "delete" flag value
        if flask.request.form.get("delete"):
            # Deleting the product from the session
            database.session.delete(Product.query.get(flask.request.form["delete"]))
            # Commiting the changes
            database.session.commit()

        # Checking if the form contains the "create" flag value
        elif flask.request.form.get("create"):
            # Getting the greatest id value from the Product model
            last_id = Product.query.order_by(Product.id.desc())[0].id
            # Creating new product record and filling it with data from the form
            product = Product(
                id = last_id + 1,
                name = flask.request.form["name"],
                price = flask.request.form["price"],
                memory_cap = flask.request.form["memory_cap"],
                discount = flask.request.form["discount"],
                picture = flask.request.form["name"] + ".png"                             
            )
            
            # Getting the image of the new product from the form
            image_save = flask.request.files["image"]
            # Saving the image of the new product
            image_save.save(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{product.picture}"))
            
            # Adding the record to the session
            database.session.add(product)
            # Commiting the changes
            database.session.commit()

        # "esle" means that the request is for changing one of the product values
        else:
            # Getting the target product from the database ba id from the form
            product = Product.query.get(flask.request.form["id"])
            # Checking if there is a request to change the image
            if flask.request.files.get("image"):
                # Using the try expression to avoid errors if the image we are trying to delete doesn't exist
                try:
                    # Deleting the old image 
                    os.remove(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{product.picture}"))
                except Exception as e:
                    print(e)

                # Getting the new image from the form
                image = flask.request.files["image"]
                # Saving the new image
                image.save(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{product.picture}"))
                # Updating the product picture value
                product.picture = f"{product.name}.png"
            else:
                # Checking if the "column" value from the form is equal to name
                if flask.request.form["column"] == "name":
                    # Setting the value "name" of the targeted product to one from the form
                    product.name = flask.request.form["name"]

                # Checking if the "column" value from the form is equal to "price"
                elif flask.request.form["column"] == "price":
                    # Setting the value "price" of the targeted product to one from the form
                    product.price = flask.request.form["name"]

                # Checking if the "column" value from the form is equal to discount
                elif flask.request.form["column"] == "discount":
                    # Setting the value "discount" of the targeted product to one from the form
                    product.discount = flask.request.form["name"]

                # Checking if the "column" value from the form is equal to memmory_cap
                elif flask.request.form["column"] == "memory_cap":
                    # Setting the value "memmory_cap" of the targeted product to one from the form
                    product.memory_cap = flask.request.form["name"]
                
            # Adding the updated product record to the session
            database.session.add(product)
            # Commiting the changes
            database.session.commit()

    # Checking if the user is authenticated 
    if current_user.is_authenticated:
        # If so, setting is_admin to the value of the user
        is_admin = current_user.is_admin
        if is_admin:        
            # Rendering the template and passing the data needed in it as parameters
            return flask.render_template(
                # Setting the template file name
                template_name_or_list = "admin.html", 
                # Passing the current page name as context argument
                page = 'admin', 
                # Passing the list of all products as context argument
                products = Product.query.all(), 
                # Passing the current_user.is_authenticated value as context argument
                is_auth = current_user.is_authenticated,
                # Passing the user data of the current user value as context argument
                user_data = User.query.get(current_user.id) if current_user.is_authenticated else None,
                # Passing the is_admin value as context argument
                is_admin = is_admin
            )

    

    