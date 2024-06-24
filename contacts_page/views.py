import flask


def show_contacts_page():
    return flask.render_template(template_name_or_list = "contacts.html")