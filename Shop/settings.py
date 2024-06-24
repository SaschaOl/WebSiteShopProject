import flask, flask_sqlalchemy, flask_migrate
import os

shop_project = flask.Flask(
    import_name = "settings",
    static_folder = "static",
    template_folder = "Shop/templates",
    instance_path = os.path.abspath(__file__ + "/..")
)

shop_project.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

database = flask_sqlalchemy.SQLAlchemy(app = shop_project)
migrate = flask_migrate.Migrate(app = shop_project, db = database)

