import unittest

from selenium import webdriver


class Registration:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        self.browser.get(link)

    def input_registration(self):
        first_name = self.browser.find_element_by_class_name("first")
        first_name.send_keys("Ivan")
        second_name = self.browser.find_element_by_css_selector(
            "div.first_block > div.form-group.second_class > input"
        )
        second_name.send_keys("Ivanov")
        email = self.browser.find_element_by_class_name("third")
        email.send_keys("ivan@ivanov.ru")
        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        return welcome_text

    def end_test(self):
        self.browser.quit()


class TestUnitTests(unittest.TestCase, Registration):
    def test_registration_1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        registration = Registration(self.link)
        self.assertEqual(
            registration.input_registration(),
            "Congratulations" "! You have " "successfully " "registered!",
        )
        registration.end_test()

    def test_registration_2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        registration = Registration(self.link)
        self.assertEqual(
            registration.input_registration(),
            "Congratulations" "! You have " "successfully " "registered!",
        )
        registration.end_test()


if __name__ == "__main__":
    unittest.main()
