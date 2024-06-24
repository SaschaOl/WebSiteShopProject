import flask

contacts_page_app = flask.Blueprint(
    name = "contacts_page",
    import_name = "app",
    template_folder = "contacts_page/templates",
    static_folder = "static"
)