import flask

basket_page_app = flask.Blueprint(
    name = "basket_page",
    import_name = "app",
    template_folder = "basket_page/templates",
    static_folder = "static"
)