from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_NAME=(By.CSS_SELECTOR,".col-sm-6:nth-child(2)>h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR,".col-sm-6:nth-child(2)>p")
    ADD_TO_BASKET=(By.CSS_SELECTOR,"#add_to_basket_form>button")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,"#messages>:nth-child(1)>.alertinner>strong")
    PRICE_OF_CART=(By.CSS_SELECTOR,"#messages>:nth-child(3)>.alertinner>p>strong")
