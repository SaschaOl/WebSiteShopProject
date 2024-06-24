import flask 

authorizatiion_page_app = flask.Blueprint(
    name= "authorizatiion_page",
    import_name= "app",
    template_folder= "authorization_page/templates",
    static_folder= "static"
)