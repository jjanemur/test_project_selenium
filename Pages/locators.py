from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK=(By.CSS_SELECTOR, "span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION=(By.CSS_SELECTOR,'[name = "registration-email"]')
    PASSWORD_REGISTRATION=(By.CSS_SELECTOR,'[name="registration-password1"]')
    PASSWORD_CONFIRMATION=(By.CSS_SELECTOR,'[name="registration-password2"]')
    REGISTRATION_BUTTON=(By.CSS_SELECTOR,'[name="registration_submit"]')

class ProductPageLocators():
    PRODUCT_NAME=(By.CSS_SELECTOR,".col-sm-6:nth-child(2)>h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR,".col-sm-6:nth-child(2)>p")
    ADD_TO_BASKET=(By.CSS_SELECTOR,"#add_to_basket_form>button")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,"#messages>:nth-child(1)>.alertinner>strong")
    PRICE_OF_BASKET=(By.CSS_SELECTOR,"#messages>:nth-child(3)>.alertinner>p>strong")

class BasketPageLocators():
    BASKET_ITEMS=(By.CSS_SELECTOR,".basket-items")
    TEXT_BASKET_IS_EMPTY=(By.CSS_SELECTOR,"div>p")