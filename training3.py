from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
money = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

submit = browser.find_element_by_css_selector(".btn").click()

x = browser.find_element_by_id('input_value')
x = x.text
x = int(x)
y = calc(x)

browser.find_element_by_id("answer").send_keys(y)

submit = browser.find_element_by_css_selector(".form-group .btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit.click()