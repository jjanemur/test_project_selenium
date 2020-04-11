from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "no success message"
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text==self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "wrong product"
    def should_be_correct_price_of_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_OF_CART), "no price of cart"
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]
        price_of_cart=self.browser.find_element(*ProductPageLocators.PRICE_OF_CART).text[1:]
        assert product_price==price_of_cart, "prices don't match"