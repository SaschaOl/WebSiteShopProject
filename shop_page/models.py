import flask, flask_sqlalchemy
from Shop.settings import database

class Product(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(120), nullable = False)
    price = database.Column(database.Integer, nullable = False)
    memory_cap = database.Column(database.Integer, nullable = False)
    discount = database.Column(database.Integer, nullable = False)
    picture = database.Column(database.String(120), nullable = False)
    
    def __repr__(self) -> str:
        return f"id - {self.id}, name- {self.name}, price - {self.price}, memory_cap - {self.memory_cap}"