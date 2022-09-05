from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.is_element_present(BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty message is not presented"

    def should_not_be_stuff_in_basket(self):
        assert self.is_not_element_present(BasketPageLocators.SOME_STUFF_IN_BASKET), \
            "Some stuff in basket is presented, but should not be"
