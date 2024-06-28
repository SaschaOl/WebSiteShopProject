# Importing flask
import flask 

#  Creating the Blueprint that will represent the application
authorizatiion_page_app = flask.Blueprint(
    # Setting the name for the application
    name= "authorizatiion_page",
    # Setting the import name to the name of the current file
    import_name= "app",
    # Setting the template folder path
    template_folder= "authorization_page/templates",
    # Setting the static folder path
    static_folder= "static"
)