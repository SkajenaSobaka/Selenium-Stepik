from selenium import webdriver

import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
fname = 'Игорь'
lname = 'Дугушкин'
email = 'kruciusf2k@mail.ru'
field1 = browser.find_element_by_name("firstname").send_keys(fname)
field2 = browser.find_element_by_name("lastname").send_keys(lname)
field3 = browser.find_element_by_name("email").send_keys(email)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

field_text = browser.find_element_by_name("file").send_keys(file_path)

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

submit = browser.find_element_by_css_selector(".btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit.click()

