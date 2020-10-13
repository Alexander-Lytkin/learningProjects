from .admin import Admin

LINK = "http://ocs-app.local:8019/"


def test_success_login(browser):
    page = Admin(browser, LINK)
    page.open()
    page.login()
