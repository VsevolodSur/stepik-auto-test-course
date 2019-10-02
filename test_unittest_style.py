import math
from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element_by_css_selector("input.first[required]")
        input1.send_keys("Ivan")
        # time.sleep(1)
        input2 = browser.find_element_by_css_selector("input.second[required]")
        input2.send_keys("Petrov")
        # time.sleep(1)
        input3 = browser.find_element_by_css_selector("input.third[required]")
        input3.send_keys("ivan.pet@gmail.com")
        # time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element_by_css_selector("input.first[required]")
        input1.send_keys("Ivan")
        # time.sleep(1)
        input2 = browser.find_element_by_css_selector("input.second[required]")
        input2.send_keys("Petrov")
        # time.sleep(1)
        input3 = browser.find_element_by_css_selector("input.third[required]")
        input3.send_keys("ivan.pet@gmail.com")
        # time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()
