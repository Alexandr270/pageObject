from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input_reg_email = self.browser.find_element_by_xpath(LoginPageLocators.REGISTRATION_EMAIL)
        input_reg_password = self.browser.find_element_by_xpath(LoginPageLocators.REGISTRATION_PASSWORD)
        input_reg_password_repeat = self.browser.find_element_by_xpath(LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        input_reg_email.send_keys(email)
        input_reg_password.send_keys(password)
        input_reg_password_repeat.send_keys(password)
        self.browser.find_element_by_xpath(LoginPageLocators.REGISTRATION_BUTTON).click()

