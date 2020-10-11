from pages.base_page import BasePage
from pages.locators import Button, Message, Products
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def go_to_product_page(self):
        link = self.browser.find_element(*Products.THE_BOOK)
        link.click()
        return ProductPage(browser=self.browser, url=self.browser.current_url)

    def press_button(self):
        button = self.browser.find_element(*Button.BUTTON)
        button.click()

    def should_be_title_book(self):
        assert self.is_element_present(
            *Products.THE_BOOK
        ), "Title is not presented"
        return self.browser.find_element(*Products.THE_BOOK).text

    def should_be_price_of_book(self):
        assert self.is_element_present(*Products.PRICE), "Price is not empty"
        return self.browser.find_element(*Products.PRICE).text

    def should_be_add_button(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            By.LINK_TEXT, "Добавить в корзину"
        ), "Нет элемента 'Добавить в корзину'"

    def title_name_is_equal_to_added_book_name(self):
        title_book = self.should_be_title_book()
        added_book = self.browser.find_element(
            *Products.ITEM_ADDED_TO_CART
        ).text
        assert added_book == title_book, "Titles are not the same"

    def book_price_is_equal_to_added_book(self):
        book_price = self.should_be_price_of_book()
        added_book = self.browser.find_element(*Products.CART_TOTAL_PRICE).text
        assert added_book == book_price, "Prices are not the same"

    def should_be_success_message(self):
        assert self.is_element_present(
            *Message.SUCCESS_MESSAGE
        ), "Successfully added to cart message"

    def should_not_be_success_message(self):
        assert not self.is_not_element_present(
            *Message.SUCCESS_MESSAGE
        ), "Success message is presented"

    def disappeared_success_message(self):
        assert not self.is_disappeared(
            *Message.SUCCESS_MESSAGE
        ), "Success message is not disappeared"
