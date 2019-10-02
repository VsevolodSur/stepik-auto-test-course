from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

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
    assert "Correct!" == hint

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
