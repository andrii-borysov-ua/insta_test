import pytest
import os
from pages import EmailSignUpPage, ForgotPasswordPage, HomePage, LoginPage
from utils.logger import get_logger


logger = get_logger(__name__)


class BaseTest:

    @pytest.fixture(autouse=True, scope='class')
    def init_pages(self, driver, request):
        request.cls.login_page = LoginPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.signup_page = EmailSignUpPage(driver)
        request.cls.forgot_password_page = ForgotPasswordPage(driver)

    @pytest.fixture(scope='class')
    def login_to_the_app(self, driver, init_pages):
        self.login_page.open()
        self.login_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))
        self.home_page.click_element(self.home_page.home_locators.save_login_info_not_now_link)
        self.home_page.handle_modal_dialog_with_text_if_needed("The messaging tab has a new look", "OK")
