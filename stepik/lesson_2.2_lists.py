import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ваш код, который заполняет обязательные поля
    first_element = browser.find_element_by_id("num1")
    second_element = browser.find_element_by_id("num2")
    x = first_element.text
    y = second_element.text
    result = str(int(x) + int(y))

    select = Select(browser.find_element_by_id("dropdown"))
    value = select.select_by_value(result)
    submit = browser.find_element_by_tag_name("button")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
