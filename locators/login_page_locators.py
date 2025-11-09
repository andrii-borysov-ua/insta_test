from locators import Locator


class LoginPageLocators(Locator):

    logo = '//i[@aria-label="Instagram"]'
    username = '//input[@name="username"]'
    password = '//input[@name="password"]'
    login_button = '//button[@type="submit"]'
    facebook_login_button = '//button[.//span[text()="Log in with Facebook"]]'



