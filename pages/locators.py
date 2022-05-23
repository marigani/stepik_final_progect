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
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, ".content #content_inner p")
    BOOK_IN_BASKET = (By. CSS_SELECTOR, ".basket-items .col-sm-4")

class LoginPageLocators():
    FILD_EMAIL = (By. ID, "id_registration-email")
    FILD_PASSORD = (By. ID, "id_registration-password1")
    FILD_CONFIRM_PASSWORD = (By. ID, "id_registration-password2")
    BUTTON_REGISTER = (By. NAME, "registration_submit")
