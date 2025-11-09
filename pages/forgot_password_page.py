import os
from core.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from utils.logger import get_logger


logger = get_logger(__name__)


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        base_url = os.environ.get('BASE_URL')
        self.login_url = base_url+ 'accounts/login/'
        self.forgot_password_locators = ForgotPasswordLocators()