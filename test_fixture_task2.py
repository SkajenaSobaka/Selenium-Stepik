import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestAliensMessage():


    urls = ["236895", "236896", "236897", "236898",  "236899", "236903", "236904", "236905", ]


    @pytest.mark.parametrize("number_of_link", urls)
    def test_scenario(self, browser, number_of_link):
        link = "https://stepik.org/lesson/{}/step/1".format(number_of_link)
        browser.get(link)
        answer = str(math.log(int(time.time())))
        browser.find_element_by_css_selector('.textarea.ember-view').send_keys(answer)
        browser.find_element_by_css_selector('.submit-submission').click()
        feedback = browser.find_element_by_css_selector('.smart-hints__feedback').text
        assert "Correct!" in feedback, f"ожидался ответ 'Correct!', но был получен '{feedback}'"

# The owls are not what they seem! OvO