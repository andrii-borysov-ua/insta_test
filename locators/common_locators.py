from locators import Locator


class CommonLocators(Locator):
    common_text_locator = '//*[text()="%s"]'
    common_link_locator = '//a[descendant-or-self::*[text()="%s"]]'
    common_button_locator = '//*[@role="button" and descendant-or-self::*[text()="%s"]]'

