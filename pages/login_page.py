from core.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from utils.logger import get_logger


logger = get_logger(__name__)


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    def open(self):
        self.go_to(self.base_url + 'accounts/login/')

    def login(self, email, password):
        self.fill_text(self.locators.username, email)
        self.fill_text(self.locators.password, password)
        self.click_element(self.locators.login_button)


