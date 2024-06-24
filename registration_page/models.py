import flask, flask_sqlalchemy
from Shop.settings import database
from flask_login import UserMixin

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(60), nullable = False)
    email = database.Column(database.String(60), nullable = False)
    password = database.Column(database.String(60), nullable = False)
    is_admin = database.Column(database.Boolean, nullable = True)

    def __repr__(self):
        return f"id - {self.id}, name - {self.name}, email - {self.email}, password - {self.password}, is_admin = {self.is_admin}" 