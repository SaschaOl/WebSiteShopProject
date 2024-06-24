import flask

admin_page_app = flask.Blueprint(
    name= "admin_page",
    import_name= "app",
    template_folder= "admin_page/templates",
    static_folder= "static"
)