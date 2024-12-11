from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import personal_account
from conftest import driver, login


def test_personal_account_redirect(driver, login):
    # Ожидание кнопки "Личный кабинет" и клик по ней
    personal_account_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(personal_account)
    )
    personal_account_button.click()

    # Проверка, что произошел редирект на страницу профиля
    assert WebDriverWait(driver, 20).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
    ), "Не произошел редирект на страницу профиля."
