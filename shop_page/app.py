# Importing flask
import flask

#  Creating the Blueprint that will represent the application
shop_page_app = flask.Blueprint(
    # Setting the name for the application
    name = "shop_page",
    # Setting the import name to the name of the current file
    import_name = "app",
    # Setting the template folder path
    template_folder = "shop_page/templates",
    # Setting the static folder path
    static_folder = "static"
)