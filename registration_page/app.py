import flask

registration_page_app = flask.Blueprint(
    name = "registration_page",
    import_name = "app",
    template_folder = "registration_page/templates",
    static_folder = "static"
)