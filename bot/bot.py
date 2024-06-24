import telebot
import telebot.callback_data
from .get_users import *
import os

token = "7489742120:AAGegVoj6q3U1P-iKZM-Ys0qKMqw0Q5zzVQ"
bot = telebot.TeleBot(token, num_threads= 3)

button_get = telebot.types.InlineKeyboardButton(text = "GET USERS", callback_data = "get_users")
button_products = telebot.types.InlineKeyboardButton(text = "GET PRODUCTS", callback_data = "get_products")
add_product = telebot.types.InlineKeyboardButton(text = "ADD PRODUCT", callback_data = "add_product")
keyboard_inline = telebot.types.InlineKeyboardMarkup(keyboard = [[button_get],[button_products, add_product]])



def callback_filter(value, callback: telebot.types.CallbackQuery):
    return callback.data.split("-")[0] == value

@bot.message_handler(commands = ["start"])
def bot_start(message: telebot.types.Message):
    print(message.chat.id)
    bot.send_message(chat_id = message.chat.id, text = "Привіт, користувач", reply_markup = keyboard_inline)

@bot.callback_query_handler(func = lambda callback: callback_filter(value = "get_users", callback= callback))
def send_users(callback: telebot.types.CallbackQuery):
    users = get_users()
    for user in users:
        button_delete = telebot.types.InlineKeyboardButton(text = "DELETE USER", callback_data = f"delete_user-{user[0]}")
        if user[4] == True:
            button_toggle = telebot.types.InlineKeyboardButton(text = "REMOVE ADMIN", callback_data = f"toggle_admin-{user[0]}")
        elif user[4] == False:
            button_toggle = telebot.types.InlineKeyboardButton(text = "GIVE ADMIN", callback_data = f"toggle_admin-{user[0]}")
        keyboard_inline_delete_remove = telebot.types.InlineKeyboardMarkup(keyboard = [[button_delete], [button_toggle]])
        bot.send_message(callback.message.chat.id, text = f"ID: {user[0]} \nName: {user[1]} \nPassword: {user[3]} \n➡️Is_admin: {user[4]}⚠️", reply_markup = keyboard_inline_delete_remove, message_thread_id = 3)

@bot.callback_query_handler(func = lambda callback: callback_filter(value = "delete_user", callback = callback))
def delete_user(callback: telebot.types.CallbackQuery):
    delete_user(id = callback.data.split("-")[1])
    bot.delete_message(chat_id = callback.message.chat.id, message_id = callback.message.message_id)
    
@bot.callback_query_handler(func = lambda callback: callback_filter(value = "toggle_admin", callback = callback) )
def toggle_admin(callback): 
    toggle_admin(id = callback.data.split("-")[1])
    user = get_user(id = callback.data.split("-")[1])[0]
    
    bot.edit_message_text(text = f"ID: {user[0]} \nName: {user[1]} \nPassword: {user[3]} \n➡️Is_admin: {user[4]}⚠️", chat_id = callback.message.chat.id, message_id = callback.message.message_id)
    
    button_delete = telebot.types.InlineKeyboardButton(text = "DELETE USER", callback_data = f"delete_user-{user[0]}")
    if user[4] == True:
        button_toggle = telebot.types.InlineKeyboardButton(text = "REMOVE ADMIN", callback_data = f"toggle_admin-{user[0]}")
    elif user[4] == False:
        button_toggle = telebot.types.InlineKeyboardButton(text = "GIVE ADMIN", callback_data = f"toggle_admin-{user[0]}")
    keyboard_inline_delete_remove = telebot.types.InlineKeyboardMarkup(keyboard = [[button_delete], [button_toggle]])
    
    bot.edit_message_reply_markup(chat_id = callback.message.chat.id, message_id = callback.message.message_id, reply_markup = keyboard_inline_delete_remove)



@bot.callback_query_handler(func = lambda callback: callback_filter(value = "get_products", callback = callback))
def send_products(callback: telebot.types.CallbackQuery):
    products = get_products()
    for product in products:
        image_button = telebot.types.InlineKeyboardButton(text = "change image", callback_data = f"change_image-{product[0]}")
        name_button = telebot.types.InlineKeyboardButton(text = "change name", callback_data = f"change_name-{product[0]}")
        capacity_button = telebot.types.InlineKeyboardButton(text = "change capacity", callback_data = f"change_capacity-{product[0]}")
        price_button = telebot.types.InlineKeyboardButton(text = "change price", callback_data = f"change_price-{product[0]}")
        discount_button = telebot.types.InlineKeyboardButton(text = "change discount", callback_data = f"change_discount-{product[0]}")
        delete_button = telebot.types.InlineKeyboardButton(text = "DELETE PRODUCT", callback_data = f"delete_product-{product[0]}")
    
        inline_keyboard = telebot.types.InlineKeyboardMarkup(keyboard = [
            [image_button],
            [name_button, capacity_button],
            [price_button, discount_button],
            [delete_button]
        ])
        with open(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{product[5]}"), "rb") as photo:
            bot.send_photo(
                chat_id = callback.message.chat.id,
                photo = photo,
                caption = 
                f"""
                Продукт:
                  Ім'я: {product[1]}
                  Ціна: {product[2]}
                  Знижка: {product[4]}
                  Об'єм пам'яті: {product[3]}    
                """,
                reply_markup = inline_keyboard,
                message_thread_id = 5 
                )

@bot.callback_query_handler(func = lambda callback: callback_filter(value = "delete_product", callback = callback))
def delete_product(callback: telebot.types.CallbackQuery):
    id_product = callback.data.split("-")[1]
    delete_product(id = id_product)
    bot.delete_message(chat_id = callback.message.chat.id, message_id = callback.message.id)

@bot.callback_query_handler(func = lambda callback: callback_filter(value = "change_image", callback = callback))    
def ask_name(callback: telebot.types.CallbackQuery):
    id_product = callback.data.split("-")[1]
    message = bot.send_message(chat_id = callback.message.chat.id, text = "Надішліть нову картинку:", message_thread_id = 5)
    original_message = callback.message
    bot.register_next_step_handler(message = message, callback = change_image, id = id_product, bot_message = message, original_message = original_message)

def change_image(message: telebot.types.Message, id, bot_message, original_message):
    save_image = bot.get_file(message.photo[-1].file_id).file_path
    image = bot.download_file(save_image)
    image_name = get_product(id = id)[0][5]
    try:
        os.remove(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{image_name}"))
    except Exception as e:
        print(f"помилка: {e}")
    with open(file = os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{image_name}"), mode = "wb") as image_file:
        image_file.write(image)
    bot.delete_message(chat_id = message.chat.id, message_id = message.id)
    bot.delete_message(chat_id = bot_message.chat.id, message_id = bot_message.id)
    bot.delete_message(chat_id = original_message.chat.id, message_id = original_message.id)
    send_updated_product(id = id, chat_id = message.chat.id)


@bot.callback_query_handler(func = lambda callback: callback_filter(value = "change_name", callback = callback))    
def ask_name(callback: telebot.types.CallbackQuery):
    id_product = callback.data.split("-")[1]
    message = bot.send_message(chat_id = callback.message.chat.id, text = "Введіть нове ім'я:", message_thread_id = 5)
    original_message = callback.message
    bot.register_next_step_handler(message = message, callback = change_name, id = id_product, bot_message = message, original_message = original_message)

def change_name(message: telebot.types.Message, id, bot_message, original_message):
    edit_product(id = id, column = "name", value = message.text)
    bot.delete_message(chat_id = message.chat.id, message_id = message.id)
    bot.delete_message(chat_id = bot_message.chat.id, message_id = bot_message.id)
    bot.delete_message(chat_id = original_message.chat.id, message_id = original_message.id)
    send_updated_product(id = id, chat_id = message.chat.id)



@bot.callback_query_handler(func = lambda callback: callback_filter(value = "change_capacity", callback = callback))    
def ask_capacity(callback: telebot.types.CallbackQuery):
    id_product = callback.data.split("-")[1]
    message = bot.send_message(chat_id = callback.message.chat.id, text = "Ведіть новий об'эм:", message_thread_id = 5)
    original_message = callback.message
    bot.register_next_step_handler(message = message, callback = change_capacity, id = id_product, bot_message = message, original_message = original_message)

def change_capacity(message: telebot.types.Message, id, bot_message, original_message):
    edit_product(id = id, column = "memory_cap", value = message.text)
    bot.delete_message(chat_id = message.chat.id, message_id = message.id)
    bot.delete_message(chat_id = bot_message.chat.id, message_id = bot_message.id)
    bot.delete_message(chat_id = original_message.chat.id, message_id = original_message.id)
    send_updated_product(id = id, chat_id = message.chat.id)
    


@bot.callback_query_handler(func = lambda callback: callback_filter(value = "change_price", callback = callback))    
def ask_price(callback: telebot.types.CallbackQuery):
    id_product = callback.data.split("-")[1]
    message = bot.send_message(chat_id = callback.message.chat.id, text = "Введіть нову ціну:", message_thread_id = 5)
    original_message = callback.message
    bot.register_next_step_handler(message = message, callback = change_price, id = id_product, bot_message = message, original_message = original_message)

def change_price(message: telebot.types.Message, id, bot_message, original_message):
    edit_product(id = id, column = "price", value = message.text)
    bot.delete_message(chat_id = message.chat.id, message_id = message.id)
    bot.delete_message(chat_id = bot_message.chat.id, message_id = bot_message.id)
    bot.delete_message(chat_id = original_message.chat.id, message_id = original_message.id)
    send_updated_product(id = id, chat_id = message.chat.id)


    
@bot.callback_query_handler(func = lambda callback: callback_filter(value = "change_discount", callback = callback))    
def ask_name(callback: telebot.types.CallbackQuery):
    id_product = callback.data.split("-")[1]
    message = bot.send_message(chat_id = callback.message.chat.id, text = "Введіть нову знижку:", message_thread_id = 5)
    original_message = callback.message
    bot.register_next_step_handler(message = message, callback = change_discount, id = id_product, bot_message = message, original_message = original_message)

def change_discount(message: telebot.types.Message, id, bot_message, original_message):
    edit_product(id = id, column = "discount", value = message.text)
    bot.delete_message(chat_id = message.chat.id, message_id = message.id)
    bot.delete_message(chat_id = bot_message.chat.id, message_id = bot_message.id)
    bot.delete_message(chat_id = original_message.chat.id, message_id = original_message.id)
    send_updated_product(id = id, chat_id = message.chat.id)



def send_updated_product(id, chat_id):
    product = get_product(id = id)[0]
    image_button = telebot.types.InlineKeyboardButton(text = "change image", callback_data = f"change_image-{product[0]}")
    name_button = telebot.types.InlineKeyboardButton(text = "change name", callback_data = f"change_name-{product[0]}")
    capacity_button = telebot.types.InlineKeyboardButton(text = "change capacity", callback_data = f"change_capacity-{product[0]}")
    price_button = telebot.types.InlineKeyboardButton(text = "change price", callback_data = f"change_price-{product[0]}")
    discount_button = telebot.types.InlineKeyboardButton(text = "change discount", callback_data = f"change_discount-{product[0]}")


    inline_keyboard = telebot.types.InlineKeyboardMarkup(keyboard = [
        [image_button],
        [name_button, capacity_button],
        [price_button, discount_button]
    ])
    with open(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{product[5]}"), "rb") as photo:
        bot.send_photo(
            chat_id = chat_id,
            photo = photo,
            caption = 
            f"""
            Продукт:
              Ім'я: {product[1]}
              Ціна: {product[2]}
              Знижка: {product[4]}
              Об'єм пам'яті: {product[3]}    
            """,
            reply_markup = inline_keyboard,
            message_thread_id= 5
            )
        

@bot.callback_query_handler(func = lambda callback: callback_filter(value = "add_product", callback = callback))
def ask_new_name(callback: telebot.types.CallbackQuery):
    message_next = bot.send_message(chat_id = callback.message.chat.id, text = "Введіть назву продукту:", message_thread_id = 9)
    bot.register_next_step_handler(message = message_next, callback = ask_new_image)

def ask_new_image(message: telebot.types.Message):
    product_data = [message.text]
    message_next = bot.send_message(chat_id = message.chat.id, text = "Задайте зображення продукту:", message_thread_id = 9)
    bot.register_next_step_handler(message = message_next, callback = ask_new_price, product_data = product_data)

def ask_new_price(message: telebot.types.Message, product_data):
    product_data.append(message.photo[-1])
    message_next = bot.send_message(chat_id = message.chat.id, text = "Введіть ціну продукту:", message_thread_id = 9)
    bot.register_next_step_handler(message = message_next, callback = ask_new_capacity, product_data = product_data)

def ask_new_capacity(message: telebot.types.Message, product_data):
    product_data.append(message.text)
    message_next = bot.send_message(chat_id = message.chat.id, text = "Введіть об'єм пам'яті:", message_thread_id = 9)
    bot.register_next_step_handler(message = message_next, callback = save_product, product_data = product_data)

def save_product(message: telebot.types.Message, product_data):
    product_data.append(message.text)
    new_product(name = product_data[0], price = product_data[2], capacity = product_data[3])
    save_image = bot.get_file(product_data[1].file_id).file_path
    image = bot.download_file(save_image)
    image_name = product_data[0] + ".png"
    with open(file = os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{image_name}"), mode = "wb") as image_file:
        image_file.write(image)
    
    with open(os.path.abspath(__file__ + f"/../../static/shop_page/image/products/{image_name}"), "rb") as photo:
        bot.send_photo(
            chat_id = message.chat.id,
            photo = photo,
            caption = 
            f"""
            Продукт
                Ім'я: {product_data[0]}
                Ціна: {product_data[2]}
                Об'єм пам'яті: {product_data[3]}    
            """,
            message_thread_id = 9
            )


def send_cart():
    cart = get_last_cart()
    products = ""
    print(cart[9])
    for product_id in cart[9].split(" "):
        products += f"{get_product(int(product_id))[0][1]}\n    "

    button_done = telebot.types.InlineKeyboardButton(text= "Познчити виконаним", callback_data= f"done-{cart[0]}")
    button_cancel = telebot.types.InlineKeyboardButton(text= "Відхилити", callback_data= f"cancel-{cart[0]}")
    keyboard_inline = telebot.types.InlineKeyboardMarkup(keyboard= [[button_done, button_cancel]])

    bot.send_message(
        chat_id = "-1002201151189",
        text = 
        f"""
НЕ ВИКОНАНО🔴

Замовлення <{cart[0]}>:
    Ім'я замовника: {cart[1]}
    Прізвизще замовника: {cart[2]}
    Номер Телефону: {cart[3]}
    Е-Пошта: {cart[4]}
    Місто: {cart[5]}
    Віділення Нової пошти: {cart[6]}

Побажання:
    {cart[7]}

Загальна сума замовоення: {cart[8]} грн

Товари:
    {products}        
    """,
        reply_markup = keyboard_inline,
        message_thread_id = 7
    )

@bot.callback_query_handler(func= lambda callback: callback_filter(value= "done", callback = callback))
def order_done(callback: telebot.types.CallbackQuery):
    
    edit_cart(callback.data.split("-")[1], "is_done", True)
    products = ""
    cart = get_cart(callback.data.split("-")[1])
    print(cart[9])
    for product_id in cart[9].split(" "):
        products += f"{get_product(int(product_id))[0][1]}\n    "

    bot.edit_message_text(
        text = 
        f"""
ВИКОНАНО✅

Замовлення <{cart[0]}>:
    Ім'я замовника: {cart[1]}
    Прізвизще замовника: {cart[2]}
    Номер Телефону: {cart[3]}
    Е-Пошта: {cart[4]}
    Місто: {cart[5]}
    Віділення Нової пошти: {cart[6]}

Побажання:
    {cart[7]}

Загальна сума замовоення: {cart[8]} грн

Товари:
    {products}        
        """,
        chat_id= callback.message.chat.id,
        message_id= callback.message.id,
    )

@bot.callback_query_handler(func= lambda callback: callback_filter(value= "cancel", callback = callback))
def cancel_order(callback: telebot.types.CallbackQuery):

    edit_cart(callback.data.split("-")[1], "canceled", True)

    bot.delete_message(chat_id= callback.message.chat.id, message_id= callback.message.id)

# bot.infinity_polling()