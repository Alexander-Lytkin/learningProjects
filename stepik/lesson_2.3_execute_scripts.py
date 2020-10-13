import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ваш код, который заполняет обязательные поля
    x_value = browser.find_element_by_id("input_value")
    x = int(x_value.text)
    x = calc(x)
    browser.execute_script("window.scrollBy(0, 190);")
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(x)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
