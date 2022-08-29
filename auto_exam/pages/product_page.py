from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element_by_xpath(ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_message_about_adding_product(self):
        assert self.is_element_present(ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message adding is not presented"
        product_name = self.browser.find_element_by_xpath(ProductPageLocators.PRODUCT_NAME).text
        message_about_adding = self.browser.find_element_by_xpath(ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        print(product_name)
        print(message_about_adding)
        assert product_name == message_about_adding, "No product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(ProductPageLocators.BOOK_PRICE), "Book price is not presented"
        assert self.is_element_present(ProductPageLocators.BASKET_TOTAL), "Basket total is not presented"
        book_price = self.browser.find_element_by_xpath(ProductPageLocators.BOOK_PRICE).text
        basket_total = self.browser.find_element_by_xpath(ProductPageLocators.BASKET_TOTAL).text
        print(book_price)
        print(basket_total)
        assert book_price == basket_total, "Book price is not equal basket total"
