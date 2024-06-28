# Importing the rquiered modules
import flask
import telebot
from shop_page.models import Product
from registration_page.models import User
from flask_login import current_user
from .models import Cart
from Shop.settings import database
from flask_mail import Message
from Shop.settings import mail


# Creating the view function
def show_basket_page():

    # List that will represent the products in the user's cart
    list_cart = []
    # List that will represent the ids of products in the the user's cart
    list_ids = []

    # Checking if cookies with the key "product" are not empty
    if flask.request.cookies and flask.request.cookies.get(key = "product") != None and flask.request.cookies.get(key = "product") != "" :
        # Getting the cookies and turning them into a list
        cookie = flask.request.cookies.get(key = "product").split(" ")
        
        # Iterating through cookies
        for id_cookie in cookie:
            # Checking if the id value from cookies is not already in the id list
            if id_cookie not in list_ids:
                # Adding the product with respective id to the product list
                list_cart.append(Product.query.get(id_cookie))
                # Adding the id the id list
                list_ids.append(id_cookie)
    

    # Checking if the user is authenticated 
    if current_user.is_authenticated:
        # If so, setting is_admin to the value of the user
        is_admin = current_user.is_admin
    else:
        # If not, setting is_admin to False
        is_admin = False
    
    # Checking if the server got a request
    if flask.request.method == "POST":
        # Checking if the user has no pending order
        if current_user.order_pending == 0:
            # Creating a database record for the new cart with data from the form
            cart_products = Cart(
                user_id = current_user.id,
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

            # Getting the user's respective database record to change it 
            user = User.query.get(current_user.id)
            # Changing the order_pending value to True
            user.order_pending = True
            
            # Adding the updated user record to session
            database.session.add(user)
            # Adding the new cart record to session
            database.session.add(cart_products)
            # Commiting the changes
            database.session.commit()

            # Defining the token for the telegram bot
            token = "YOUR TELEGRAM BOT TOKEN HERE"
            # Creating thebot instance and passing the token as an arguament
            bot = telebot.TeleBot(token)

            # Creating a string for the list of product names
            products = ""
            # Iterating through the products from the cart and adding the name to the string
            for product_id in cart_products.products.split(" "):
                products += f"{Product.query.get(int(product_id)).name}\n    "

            # Creating an inline button for the maessage tha will be responsible for marking the order as done 
            button_done = telebot.types.InlineKeyboardButton(text= "Познчити виконаним", callback_data= f"done-{cart_products.id}")
            # Creating an inline button for the maessage tha will be responsible for canceling the order
            button_cancel = telebot.types.InlineKeyboardButton(text= "Відхилити", callback_data= f"cancel-{cart_products.id}")
            # Assembling the inline keyboard markup with two above buttons
            keyboard_inline = telebot.types.InlineKeyboardMarkup(keyboard= [[button_done, button_cancel]])

            # Calling bot to send the message 
            bot.send_message(
                    chat_id = "YOUR GROUP ID HERE",
                    text = 
                    f"""
            НЕ ВИКОНАНО🔴
            
            Замовлення:
                Ім'я замовника: {cart_products.name}
                Прізвизще замовника: {cart_products.surname}
                Номер Телефону: {cart_products.number_user}
                Е-Пошта: {cart_products.email_user}
                Місто: {cart_products.city_user}
                Віділення Нової пошти: {cart_products.nova_poshta}

            Побажання:
                {cart_products.additional_wishes}

            Загальна сума замовоення: {cart_products.price} грн

            Товари:
                {cart_products.products}          
                """,
                    reply_markup = keyboard_inline,
                    message_thread_id = 7
            )
            
            # Creating the message text for the mail message 
            message_text = f"""
            Замовлення:
                Ім'я замовника: {cart_products.name}
                Прізвизще замовника: {cart_products.surname}
                Номер Телефону: {cart_products.number_user}
                Е-Пошта: {cart_products.email_user}
                Місто: {cart_products.city_user}
                Віділення Нової пошти: {cart_products.nova_poshta}

            Побажання:
                {cart_products.additional_wishes}

            Загальна сума замовоення: {cart_products.price} грн

            Товари:
                {cart_products.products}   
            """

            # Creating the message instance for the mail message
            message = Message(
                # Setting the message subject
                "Замовлення оформлено",
                # Setting the sender to administration mail
                sender = "YOUR ADMINISTRATION EMAIL ADRESS HERE",
                # Setting the recipient's email to user's email 
                recipients = [current_user.email],
                # Setting the message text
                body = f"{message_text}"
            )

            # Sending the message
            mail.send(message)

        else:
            # Getting the user's respective database record to change it 
            user = User.query.get(current_user.id)
            # Deleting the order(cart object) from the session
            database.session.delete(Cart.query.filter_by(user_id = current_user.id)[0])
            # Changing the order_pending value to False
            user.order_pending = False
            # Adding the updated usser record to session
            database.session.add(user)
            # Commiting the changes
            database.session.commit()

            # Creating the message text for the mail message
            message_text = f"Дорогий {current_user.name}, ваше замовлення скасовано (:"
            
            # Creating the message instance for the mail message
            message = Message(
                # Setting the message subject
                "Замовлення скасовано",
                # Setting the sender to administration mail
                sender = "YOUR ADMINISTRATION EMAIL ADRESS HERE",
                # Setting the recipient's email to user's email 
                recipients = [current_user.email],
                # Setting the message text
                body = f"{message_text}"
            )
            # Sending the message
            mail.send(message)

         
    
    
    # Checking if the user has no pending order
    if current_user.order_pending == 0:
        # Rendering the standart template for the basket page
        return flask.render_template(
            # Setting the template file name
            template_name_or_list = "basket.html",
            # Passing the list of product in cart as context argument 
            list_cart = list_cart,
            page = "basket", 
            # Passing the current_user.is_authenticated value as context argument
            is_auth = current_user.is_authenticated,
            # Passing the user data of the current user value as context argument
            user_data = User.query.get(current_user.id) if current_user.is_authenticated else None,
            # Passing the is_admin value as context argument
            is_admin = is_admin
        )
    else:
        # Rendering the template for the pending order
        return flask.render_template(
            # Setting the template file name
            template_name_or_list = "cart.html", 
            # Passing the list of products in cart as context argument
            list_cart = list_cart,
            # Passing the current page name as context argument
            page = "basket", 
            # Passing the current_user.is_authenticated value as context argument
            is_auth = current_user.is_authenticated,
            # Passing the user data of the current user value as context argument
            user_data = User.query.get(current_user.id) if current_user.is_authenticated else None,
            # Passing the is_admin value as context argument
            is_admin = is_admin
        )
