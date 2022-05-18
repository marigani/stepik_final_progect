from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def find_button_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button.click()

    def should_be_cost_book(self):
        cost_text = self.browser.find_element(*ProductPageLocators.COST_BOOK)
        cost_text = cost_text.text
        cost_basket_text = self.browser.find_element(*ProductPageLocators.COST_BOOK_BASKET)
        cost_basket_text = cost_basket_text.text
        assert cost_text == cost_basket_text, \
             f"Wrong cost of book, got {cost_basket_text} instead of {cost_text}"
    
    def should_be_name_book(self):
        name_text = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        name_text = name_text.text
        name_basket_text = self.browser.find_element(*ProductPageLocators.NAME_BOOK_BASKET)
        name_basket_text = name_basket_text.text
        assert name_text == name_basket_text, \
             f"Wrong name of book, got {name_basket_text} instead of {name_text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should be"
    
