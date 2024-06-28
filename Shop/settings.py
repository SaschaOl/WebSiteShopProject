# Importing the necessary modules
import flask, flask_sqlalchemy, flask_migrate, flask_mail
import os

# Creating the main application with the Flask class
shop_project = flask.Flask(
    # The name of the application package
    import_name = "settings",
    # Path to the respective folder in static
    static_folder = "static",
    # Path to the templates folder
    template_folder = "Shop/templates",
    # Aplication folder path
    instance_path = os.path.abspath(__file__ + "/..")
)


# Setting the configuration for work with sqlite
shop_project.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
# Configuring the SMTP mail server for work with mail
shop_project.config['MAIL_SERVER'] = "smtp.gmail.com"
# Configuring the mail port for work with mail
shop_project.config['MAIL_PORT'] = 587
# Configuring the use TLS to True for work with mail
shop_project.config['MAIL_USE_TLS'] = True
# Configuring the main email adrees for work with mail
shop_project.config['MAIL_USERNAME'] = "YOUR ADMINISTRATION EMAIL ADRESS HERE"
# Configuring the main email application password for work with mail
shop_project.config['MAIL_PASSWORD'] = "YOUR ADMINISTRATION EMAIL PASSWORD HERE"

# Creating database instance so we can do operations with it
database = flask_sqlalchemy.SQLAlchemy(app = shop_project)
# Creating Migration instance to make migrtions possible
migrate = flask_migrate.Migrate(app = shop_project, db = database)
# Creating the Mail class instance to manage the email messaging 
mail = flask_mail.Mail(app = shop_project)
