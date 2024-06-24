import flask

home_page_app = flask.Blueprint(
    name = "home_app",
    import_name = "app",
    template_folder = "home_page/templates",
    static_folder = "static"
)