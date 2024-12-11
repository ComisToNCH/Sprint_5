import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import log_in_button, password_log_in, email_log_in


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Явное ожидание для поля email
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(email_log_in)
    ).send_keys("kosurova_16@yandex.ru")

    # Явное ожидание для поля password
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(password_log_in)
    ).send_keys("kosurova_16@yandex.ru")

    # Явное ожидание для кнопки log in
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(log_in_button)
    ).click()

    # Ожидание, пока URL изменится на главную страницу
    WebDriverWait(driver, 20).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )
    return driver
