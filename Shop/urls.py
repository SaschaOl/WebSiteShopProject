import home_page
import authorization_page
import registration_page
import contacts_page
import basket_page
import shop_page
import admin_page
from .settings import shop_project

home_page.home_page_app.add_url_rule(
    rule = "/",
    view_func = home_page.show_home_page,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = home_page.home_page_app)


registration_page.registration_page_app.add_url_rule(
    rule = "/registration/",
    view_func = registration_page.show_registration_page,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = registration_page.registration_page_app)


authorization_page.authorizatiion_page_app.add_url_rule(
    rule = "/authorization/",
    view_func = authorization_page.show_authorizatiion_page,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = authorization_page.authorizatiion_page_app)


basket_page.basket_page_app.add_url_rule(
    rule = "/basket/",
    view_func = basket_page.show_basket_page,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = basket_page.basket_page_app)


contacts_page.contacts_page_app.add_url_rule(
    rule = "/contacts/",
    view_func = contacts_page.show_contacts_page,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = contacts_page.contacts_page_app)


shop_page.shop_page_app.add_url_rule(
    rule = "/shop/",
    view_func = shop_page.show_page,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = shop_page.shop_page_app)

admin_page.admin_page_app.add_url_rule(
    rule = "/admin/",
    view_func = admin_page.show_page,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = admin_page.admin_page_app)


