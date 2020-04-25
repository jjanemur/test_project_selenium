from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "no success message"
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text==self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "wrong product"

    def should_be_correct_price_of_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_OF_BASKET), "no price of basket"
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]
        price_of_basket=self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET).text[1:]
        assert product_price==price_of_basket, "prices don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    def success_message_should_dissappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message has not disappeared"