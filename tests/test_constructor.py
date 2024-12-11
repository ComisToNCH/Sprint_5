from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators import sauce, sauce_header, bun, bun_header, fillings, fillings_header
from conftest import driver, login


def test_switch_to_sauce(driver, login):
    wait = WebDriverWait(driver, 10)

    # Клик на вкладку "Соусы"
    wait.until(EC.element_to_be_clickable(sauce)).click()

    # Прокрутка к заголовку "Соусы"
    sauce_header_element = wait.until(EC.presence_of_element_located(sauce_header))
    driver.execute_script("arguments[0].scrollIntoView();", sauce_header_element)

    # Проверка, что заголовок видим
    assert sauce_header_element.is_displayed(), "Заголовок 'Соусы' не отображается."


def test_scroll_to_bun(driver, login):
    wait = WebDriverWait(driver, 10)

    # Клик на вкладку "Соусы"
    wait.until(EC.element_to_be_clickable(sauce)).click()

    # Клик на вкладку "Булки"
    wait.until(EC.element_to_be_clickable(bun)).click()

    # Прокрутка к заголовку
    bun_header_element = wait.until(EC.presence_of_element_located(bun_header))
    driver.execute_script("arguments[0].scrollIntoView();", bun_header_element)

    # Проверка, что заголовок видим
    assert bun_header_element.is_displayed(), "Заголовок 'Булки' не отображается."


def test_switch_to_fillings(driver, login):
    wait = WebDriverWait(driver, 10)

    # Клик на вкладку "Начинки"
    wait.until(EC.element_to_be_clickable(fillings)).click()

    # Прокрутка к заголовку "Начинки"
    fillings_header_element = wait.until(EC.presence_of_element_located(fillings_header))
    driver.execute_script("arguments[0].scrollIntoView();", fillings_header_element)

    # Проверка, что заголовок видим
    assert fillings_header_element.is_displayed(), "Заголовок 'Начинки' не отображается."
