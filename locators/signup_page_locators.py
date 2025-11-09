from locators import Locator


class EmailSignUpLocators(Locator):

    login_field = '//input[@name="emailOrPhone"]'
    password_field = '//input[@name="password"]'
    full_name_field = '//input[@name="fullName"]'
    username_field = '//input[@name="username"]'