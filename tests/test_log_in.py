from conftest import driver, login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import email_log_in, password_log_in, log_in_button, personal_account, login_registration_button


def test_main_page_log_in(driver):
    # Переход на страницу логина
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Ожидание появления поля для ввода email и ввод данных
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(email_log_in)
    )
    email.send_keys("kosurova_16@yandex.ru")

    # Ожидание появления поля для ввода пароля и ввод данных
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(password_log_in)
    )
    password.send_keys("kosurova_16@yandex.ru")

    # Ожидание возможности клика по кнопке входа
    log_in_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(log_in_button)
    )
    log_in_btn.click()

    # Ожидание редиректа на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Проверка, что текущий URL соответствует ожидаемому
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Не произошел редирект на главную страницу."


def test_personal_account_redirect(driver, login):
    # Ожидание кнопки "Личный кабинет" и клик
    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(personal_account)
    )
    personal_account_button.click()

    # Ожидание редиректа на страницу профиля
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
    )

    # Проверка текущего URL
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile", "Не произошел редирект на страницу профиля."


def test_from_registration_to_login(driver):
    # Переход на страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ожидание и клик по кнопке перехода к логину
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(login_registration_button)
    )
    login_button.click()

    # Проверка редиректа на страницу логина
    assert WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    ), "Не произошел редирект на страницу логина."


def test_from_password_recovery_to_login(driver):
    # Переход на страницу восстановления пароля
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    # Ожидание кнопки перехода к логину и клик
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(login_registration_button)
    )
    login_button.click()

    # Проверка редиректа на страницу логина
    assert WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    ), "Не произошел редирект на страницу логина."