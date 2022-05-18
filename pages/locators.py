from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK_BASKET = (By.CSS_SELECTOR, "#messages strong")
    COST_BOOK_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    COST_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK_BASKET = (By.CSS_SELECTOR, "#messages strong")
    COST_BOOK_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    COST_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
