from faker import Faker
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import name_field, email_field, password_field, register_button, error_message

faker = Faker()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration_successful(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ожидание поля имени и ввод данных
    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(name_field)
    )
    name.send_keys(faker.name())

    # Ожидание поля email и ввод данных
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(email_field)
    )
    email.send_keys(faker.email())

    # Ожидание поля пароля и ввод данных
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(password_field)
    )
    password.send_keys(faker.password(6))

    # Ожидание кнопки регистрации и клик
    register_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(register_button)
    )
    register_button_element.click()

    # Ожидание редиректа на страницу логина
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Проверка текущего URL
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Не произошел редирект на страницу входа."


def test_password_error_message_displayed(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ожидание поля пароля и ввод некорректного пароля
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(password_field)
    )
    password.send_keys(faker.password(5))  # Пароль короче минимального значения

    # Ожидание кнопки регистрации и клик
    register_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(register_button)
    )
    register_button_element.click()

    # Ожидание сообщения об ошибке
    error_message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(error_message)
    )

    # Проверка, что сообщение об ошибке отображается
    assert error_message_element.is_displayed(), "Сообщение об ошибке не было выведено."

