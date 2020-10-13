from .base_page import BasePage
from .locators import LoginForm


class Admin(BasePage):
    def login(self):
        email = self.browser.find_element(*LoginForm.EMAIL)
        email.send_keys("a.lytkin@omprussia.ru")
        password = self.browser.find_element(*LoginForm.PASSWORD)
        password.send_keys("SP~Jk:F;FF32")
        button = self.browser.find_element(*LoginForm.BUTTON)
        button.click()
