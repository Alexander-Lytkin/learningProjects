import pytest
from pages.product_page import ProductPage


@pytest.mark.need_review
@pytest.mark.parametrize(
    "promo", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
)
def test_guest_can_add_product_to_basket(browser, promo):
    link = (
        f"http://selenium1py.pythonanywhere.com"
        f"/catalogue/coders-at-work_207/?promo=offer'{promo}'"
    )
    page = ProductPage(browser, link)
    page.open()
    page.press_button()
    page.solve_quiz_and_get_code()
    page.book_price_is_equal_to_added_book()
    page.title_name_is_equal_to_added_book_name()


@pytest.mark.need_review
def test_guest_cant_see_success_message_adding_product_to_basket(browser):
    link = (
        "http://selenium1py.pythonanywhere.com/"
        "ru/catalogue/coders-at-work_207/"
    )
    page = ProductPage(browser, link)
    page.open()
    page.press_button()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_success_message(browser):
    link = (
        "http://selenium1py.pythonanywhere.com/"
        "ru/catalogue/coders-at-work_207/"
    )
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = (
        "http://selenium1py.pythonanywhere.com/"
        "ru/catalogue/coders-at-work_207/"
    )
    page = ProductPage(browser, link)
    page.open()
    page.press_button()
    page.disappeared_success_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = (
        "http://selenium1py.pythonanywhere.com/"
        "en-gb/catalogue/the-city-and-the-stars_95/"
    )
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
