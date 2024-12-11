import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, login
from locators import personal_account, log_out_button


def test_log_out(driver, login):
    # Переход в личный кабинет
    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(personal_account)
    )
    personal_account_button.click()

    # Ожидание кнопки выхода и клик
    log_out_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(log_out_button)
    )
    log_out_button_element.click()

    # Проверка редиректа на страницу логина
    assert WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    ), "Не произошел редирект на страницу логина после выхода."
