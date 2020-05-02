from .Pages.product_page import ProductPage
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage
import pytest
import time

product_base_link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
ignore=7
promo_links=[f"{product_base_link}/?promo=offer{no}" for no in range(10)if no!=ignore]

@pytest.mark.parametrize("link",promo_links)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser,link):#предаем параметризуемый аргумент
    page=ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_correct_price_of_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, product_base_link)
    page.open()
    page.go_to_basket()
    page.should_be_empty_basket()
    page.should_be_text_basket_is_empty()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        login_link="http://selenium1py.pythonanywhere.com/accounts/login/"
        page=LoginPage(browser,login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email,"lalala001")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        page.add_to_basket()
        page.should_be_success_message()
    def test_user_can_add_product_to_basket(self,browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        page.add_to_basket()
        page.should_be_correct_price_of_basket()


