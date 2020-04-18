from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):#наследуем от класса BasePage для доступа к атрибутам и методам
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)