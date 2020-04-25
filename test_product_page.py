from .Pages.product_page import ProductPage
import pytest
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage

product_base_link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
promo_links=[f"{product_base_link}/?promo=offer{no}" for no in range(10)]
@pytest.mark.parametrize("link",promo_links)
def test_guest_can_add_product_to_basket(browser,link):#предаем параметризуемый аргумент
    page=ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_correct_price_of_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_empty_basket()
    page.should_be_text_basket_is_empty()




