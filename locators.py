from selenium.webdriver.common.by import By


class MainPageLocators():
    CATALOGUE_LINK = (By.XPATH, '//ul[@class = "dropdown-menu"]//a')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONF_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.XPATH, "//form[@id='register_form']//button")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
