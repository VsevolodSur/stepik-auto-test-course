from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math

link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture
def browser():
    # print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    yield browser
    # print("\nquit browser..")
    time.sleep(3)
    browser.quit()

@pytest.mark.parametrize('links',
[
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
])
def test_answer(browser, links):
# def test_answer_stepik_lesson(browser):
    link = f"{links}"
    browser.get(link)

    input1 = browser.find_element_by_css_selector("textarea.textarea")
    answer = str(math.log(int(time.time())))
    input1.send_keys(answer)

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()

    hint_text_el = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR , "pre.smart-hints__hint"))
    )
    hint = hint_text_el.text
    with open('../dir_sort.txt', 'a') as ba:
        if "Correct!" == hint:
            assert True
        else:
            ba.write(hint)
            assert False
