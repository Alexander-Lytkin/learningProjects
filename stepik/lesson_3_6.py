import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize(
    "link",
    [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
    ],
)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    time.sleep(5)
    text_area = browser.find_element(By.CSS_SELECTOR, ".textarea")
    answer = str(math.log(int(time.time())))
    text_area.send_keys(answer)
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "smart-hints__hint"), "Correct!"
        )
    )
    message = browser.find_element_by_class_name("smart-hints__hint")
    message_answer = message.text
    assert "Correct!" == message_answer
