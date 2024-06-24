import flask

shop_page_app = flask.Blueprint(
    name = "shop_page",
    import_name = "app",
    template_folder = "shop_page/templates",
    static_folder = "static"
)