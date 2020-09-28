import math
import time

from selenium import webdriver


def calc(el):
    return str(math.log(abs(12 * math.sin(el))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ваш код, который заполняет обязательные поля
    button = browser.find_element_by_tag_name("button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_value = browser.find_element_by_id("input_value")
    x = int(x_value.text)
    x = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(x)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
