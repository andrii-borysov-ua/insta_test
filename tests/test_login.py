from core.base_test import BaseTest


class TestLoginPage(BaseTest):

    def test_login(self):
        self.login_page.open()
        self.login_page.login('username','password')
        self.login_page.text_should_be_displayed("Sorry, your password was incorrect. Please double-check your password.")

    def test_go_to_sign_up_page(self):
        self.login_page.open()
        self.login_page.click_link_with_text("Sign up")
        self.login_page.text_should_be_displayed("Sign up to see photos and videos from your friends.")

    def test_forgot_password_page(self):
        self.login_page.open()
        self.login_page.click_link_with_text("Forgot password?")
        self.forgot_password_page.wait_until_element_is_visible(self.forgot_password_page.forgot_password_locators.forgot_password_image)
        self.forgot_password_page.text_should_be_displayed("Enter your email, phone, or username and we'll send you a link to get back into your account.")