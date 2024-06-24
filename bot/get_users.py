import sqlite3
import os

def get_users():
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall() 
    data.close()
    return users

def delete_user(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"DELETE FROM user WHERE id = {id}")
    data.commit()
    data.close()
    
def toggle_admin(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"SELECT is_admin FROM user WHERE id = {id}")
    is_admin = cursor.fetchall()
    print(is_admin)
    cursor.execute(f"UPDATE user SET is_admin = {not is_admin[0][0]} WHERE id = {id}")
    data.commit()
    data.close()

def get_user(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"SELECT * FROM user WHERE id = {id}")
    user = cursor.fetchall() 
    data.close()
    return user


def get_products():
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    data.close()
    return products

def get_product(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"SELECT * FROM product WHERE id = {id}")
    product = cursor.fetchall() 
    data.close()
    return product

def edit_product(id, column, value):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"UPDATE product SET {column} = '{value}' WHERE id = {id}")
    data.commit()
    data.close()

def new_product(name, price, capacity):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"INSERT INTO product (name, price, memory_cap, discount, picture) VALUES ('{name}', '{price}', '{capacity}', '0', '{name}.png')")
    data.commit()
    data.close()

def delete_product(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"DELETE FROM product WHERE id = {id}")
    data.commit()
    data.close()

def get_last_cart():
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute("SELECT * FROM cart")
    list_cart = cursor.fetchall()
    data.close()
    return list_cart[-1]

def edit_cart(id, column, value):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"UPDATE cart SET {column} = '{value}' WHERE id = {id}")
    data.commit()
    data.close()

def get_cart(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"SELECT * FROM cart WHERE id = {id}")
    cart = cursor.fetchall() 
    data.close()
    return cart[0]
