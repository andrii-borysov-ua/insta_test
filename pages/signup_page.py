from core.base_page import BasePage
from utils.logger import get_logger
from locators.signup_page_locators import EmailSignUpLocators


logger = get_logger(__name__)


class EmailSignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sign_up_locators = EmailSignUpLocators

    def open(self):
        self.go_to(self.base_url + 'accounts/emailsignup/')