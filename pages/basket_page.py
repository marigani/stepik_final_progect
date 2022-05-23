from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage): 
    def find_button_basket(self):
        button = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        button.click()
    
    def basket_should_by_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOK_IN_BASKET), \
            "Book in basket, but should not be"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Empty message is not presented, but should be"
      