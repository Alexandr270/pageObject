class MainPageLocators:
    LOGIN_LINK = '//a[@id="login_link"]'


class LoginPageLocators:
    LOGIN_FORM = '//form[@id="login_form"]'
    REGISTER_FORM = '//form[@id="register_form"]'
    REGISTRATION_EMAIL = '//input[@name="registration-email"]'
    REGISTRATION_PASSWORD = '//input[@name="registration-password1"]'
    REGISTRATION_PASSWORD_REPEAT = '//input[@name="registration-password2"]'
    REGISTRATION_BUTTON = '//button[@name="registration_submit"]'


class ProductPageLocators:
    BASKET_BUTTON = '//button[contains(@class,"btn-add-to-basket")]'
    MESSAGE_ABOUT_ADDING = '//div[@id="messages"]/div[1]/div/strong'
    PRODUCT_NAME = '//div[contains(@class, "product_main")]/h1'
    BASKET_TOTAL = '//div[@id="messages"]/div[3]/div/p/strong'
    BOOK_PRICE = '//div[contains(@class, "product_main")]/p'


class BasePageLocators:
    LOGIN_LINK = '//a[@id="login_link"]'
    LOGIN_LINK_INVALID = '//a[@id="login_link_inc"]'
    USER_ICON = '//i[@class="icon-user"]'


class BasketPageLocators:
    BASKET_LINK = '//a[@class="btn btn-default"]'
    EMPTY_BASKET_MESSAGE = '//div[@id="content_inner"]/p'
    SOME_STUFF_IN_BASKET = '//h2[contains(text(), "Товары в корзине")]'
