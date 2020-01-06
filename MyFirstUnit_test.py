from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first_class .first")
        input1.send_keys("Ivan")
        input1 = browser.find_element_by_css_selector(".first_block .second_class .second")
        input1.send_keys("Semenov")
        input3 = browser.find_element_by_css_selector(".first_block .third_class .third")
        input3.send_keys("Ivan@as.ru")
        input4 = browser.find_element_by_css_selector(".second_block .first_class .first")
        input4.send_keys("9654454528")
        input5 = browser.find_element_by_css_selector(".second_block .second_class .second")
        input5.send_keys("Kyev")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_css_selector(".container")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Ожидаемый текст не найден")


    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first_class .first")
        input1.send_keys("Ivan")
        input1 = browser.find_element_by_css_selector(".first_block .second_class .second")
        input1.send_keys("Semenov")
        input3 = browser.find_element_by_css_selector(".first_block .third_class .third")
        input3.send_keys("Ivan@as.ru")
        input4 = browser.find_element_by_css_selector(".second_block .first_class .first")
        input4.send_keys("9654454528")
        input5 = browser.find_element_by_css_selector(".second_block .second_class .second")
        input5.send_keys("Kyev")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_css_selector(".container")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Ожидаемый текст не найден")

if __name__ == "__main__":
    unittest.main()