import os
import time

from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ваш код, который заполняет обязательные поля
    name = browser.find_element_by_name("firstname")
    name.send_keys("Ivan")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Ivanov")
    email = browser.find_element_by_name("email")
    email.send_keys("ivan@ivanov.ru")
    file_path = os.path.join(
        "/home/alexandrlytkin/learningProjects/stepik", "file.txt"
    )  # добавляем к этому пути имя файла
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector("body > div > form > button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
