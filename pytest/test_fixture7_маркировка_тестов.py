import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

link = "http://selenium1py.pythonanywhere.com/"

'''
example: Маркировка тестов

Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке 
параметр -m и нужную метку =>
$ pytest -s -v -m smoke test_fixture.py

Как же регистрировать метки?
Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
Текст после знака ":" является поясняющим — его можно не писать.

'''


@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test suite..")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
