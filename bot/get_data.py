import sqlite3
import os

# Gets the list of all users from the database
def get_users():
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall() 
    data.close()
    return users

# Deletes the user from the database by id
def delete_user(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"DELETE FROM user WHERE id = {id}")
    data.commit()
    data.close()
    
# Toggles the is_admin value of the user by id
def toggle_admin(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"SELECT is_admin FROM user WHERE id = {id}")
    is_admin = cursor.fetchall()
    print(is_admin)
    cursor.execute(f"UPDATE user SET is_admin = {not is_admin[0][0]} WHERE id = {id}")
    data.commit()
    data.close()

# Gets user by id
def get_user(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"SELECT * FROM user WHERE id = {id}")
    user = cursor.fetchall() 
    data.close()
    return user

# Gets the list of all products from the database
def get_products():
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    data.close()
    return products

# Gets product by id
def get_product(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"SELECT * FROM product WHERE id = {id}")
    product = cursor.fetchall() 
    data.close()
    return product

# Sets product's "column" value to "value" by id
def edit_product(id, column, value):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"UPDATE product SET {column} = '{value}' WHERE id = {id}")
    data.commit()
    data.close()

# Creates new product with data passed as parameters
def new_product(name, price, capacity):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"INSERT INTO product (name, price, memory_cap, discount, picture) VALUES ('{name}', '{price}', '{capacity}', '0', '{name}.png')")
    data.commit()
    data.close()

# Deletes the product from the database by id
def delete_product(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"DELETE FROM product WHERE id = {id}")
    data.commit()
    data.close()

# Sets cart's "column" value to "value" by id
def edit_cart(id, column, value):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"UPDATE cart SET {column} = '{value}' WHERE id = {id}")
    data.commit()
    data.close()

# Gets product by id
def get_cart(id):
    data = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = data.cursor()
    cursor.execute(f"SELECT * FROM cart WHERE id = {id}")
    cart = cursor.fetchall() 
    data.close()
    return cart[0]
