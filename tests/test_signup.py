from core.base_test import BaseTest


class TestSignupPage(BaseTest):

    def test_open_signup_page(self):
        self.signup_page.open()
        self.signup_page.text_should_be_displayed("Sign up to see photos and videos from your friends.")