from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, login
from locators import constructor, logo, personal_account


def test_click_on_constructor(driver, login):
    # Переход в личный кабинет
    personal_account_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(personal_account)
    )
    personal_account_button.click()

    # Ожидание исчезновения модального окна (если оно есть)
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
    )

    # Переход в конструктор
    constructor_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(constructor)
    )
    constructor_button.click()

    # Проверка редиректа на главную страницу
    assert WebDriverWait(driver, 20).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    ), "Не произошел редирект на главную страницу из конструктора."

def test_click_on_logo(driver, login):
    # Переход в личный кабинет
    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(personal_account)
    )
    personal_account_button.click()

    # Клик по логотипу
    logo_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(logo)
    )
    logo_button.click()

    # Проверка редиректа на главную страницу
    assert WebDriverWait(driver, 20).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    ), "Не произошел редирект на главную страницу при клике по логотипу."
