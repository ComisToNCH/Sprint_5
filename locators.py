from selenium.webdriver.common.by import By

# Локаторы для страницы регистрации
name_field = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")  # Поле для ввода имени
email_field = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  # Поле для ввода почты
password_field = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")  # Поле для ввода пароля
register_button = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")  # Кнопка регистрации
error_message = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение об ошибке пароля

# Локаторы для страницы входа
email_log_in = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  # Поле для ввода почты на странице входа
password_log_in = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")  # Поле для ввода пароля на странице входа
log_in_button = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка входа
login_registration_button = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")


# Локаторы для работы с личным кабинетом
personal_account = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and contains(., 'Личный Кабинет')]")  # Ссылка на личный кабинет
log_out_button = (By.XPATH, "//button[contains(@class, 'Account_button') and text()='Выход']")  # Кнопка выхода из аккаунта

# Локаторы для возврата на главную страницу
constructor = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Ссылка на конструктор бургеров
logo = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")  # Логотип сайта

# Локаторы для вкладок конструктора
bun = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]/span[text()='Булки']")  # Вкладка "Булки"
sauce = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]/span[text()='Соусы']")  # Вкладка "Соусы"
fillings = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]/span[text()='Начинки']")  # Вкладка "Начинки"

# Локаторы для заголовков разделов конструктора
bun_header = (By.XPATH, "//h2[text()='Булки']")  # Заголовок "Булки"
sauce_header = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок "Соусы"
fillings_header = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок "Начинки"
