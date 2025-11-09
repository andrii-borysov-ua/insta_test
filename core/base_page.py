import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.common_locators import CommonLocators
from utils.logger import get_logger


logger = get_logger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = os.environ.get('BASE_URL')
        self.common_locators = CommonLocators()

    def wait_until_element_is_visible(self, locator, timeout=10, message=''):
        logger.info(f"Wait until element is visible <<{locator}>>")
        message = f"Element with locator {locator} wasn't appear in {timeout} seconds." if not message else message
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator), message=message)
        return element

    def find_element_with_text(self, locator, text, timeout=10):
        logger.info(f"Find element with text: <<{locator}>> <<{text}>> ")
        by, loc = locator
        return self.wait_until_element_is_visible((by, loc % text), timeout)

    def go_to(self, url):
        logger.info(f"Get url: <<{url}>>")
        self.driver.get(url)

    def fill_text(self, locator, text):
        logger.info(f"Filling in <<{locator}>> with text: <<{text}>>")
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, locator):
        logger.info(f"Click element with locator <<{locator}>>")
        self.wait_until_element_is_visible(locator).click()

    def text_should_be_displayed(self, text, timeout=10):
        logger.info(f"Text should be displayed <<{text}>>")
        by, loc = self.common_locators.common_text_locator
        msg = f"Text <<{text}>> wasn't displayed in {timeout} seconds."
        assert self.wait_until_element_is_visible((by, loc % text), timeout, msg).text == text

    def click_link_with_text(self, text):
        logger.info(f"Click link with text <<{text}>>")
        by, loc = self.common_locators.common_link_locator
        self.wait_until_element_is_visible((by, loc % text)).click()

    def click_button_with_text(self, text):
        self.find_element_with_text(self.common_locators.common_button_locator, text).click()

