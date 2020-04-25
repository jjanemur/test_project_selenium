from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):#в аргументе фикстура browser, те chromewebdriver
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера из фикстуры и url адрес
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page=LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_empty_basket()
    page.should_be_text_basket_is_empty()


