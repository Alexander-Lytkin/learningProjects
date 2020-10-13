from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (
        By.CSS_SELECTOR,
        "##default > header "
        "div.navbar.primary.navbar-static-top"
        ".navbar-inverse > div > a",
    )


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class DropDownToggle:
    DROP_DOWN_TOGGLE = (By.CSS_SELECTOR, "#browse > li > a")
    BOOKS = (By.LINK_TEXT, "Books")


class Catalog:
    SECTION = (By.TAG_NAME, "section")


class Products:
    THE_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    ITEM_ADDED_TO_CART = (By.CSS_SELECTOR, ".alert-success strong")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")


class Message:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(2)")


class Button:
    BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
