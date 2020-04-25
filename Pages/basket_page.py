from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "basket is not empty"
    def should_be_text_basket_is_empty(self):
        text_basket_is_empty=self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY).text
        assert "Your basket is empty" in text_basket_is_empty, "wrong text"

