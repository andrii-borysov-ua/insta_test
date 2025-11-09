from pyexpat.errors import messages

from selenium.common import TimeoutException

from core.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from utils.logger import get_logger
from utils.helper import extract_likes

logger = get_logger(__name__)


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.home_locators = HomePageLocators()

    def handle_modal_dialog_with_text_if_needed(self, modal_dialog_text, buton_text):
        try:
            modal = self.find_element_with_text(self.home_locators.modal_dialog, modal_dialog_text, timeout=30)
            by, loc = self.home_locators.element_button
            modal.find_element(by, loc % buton_text).click()
        except TimeoutException:
            pass    # NOP

    def search_article_by_likes_number(self, number_of_likes, articles_limit=1000):
        result = None
        article = self.wait_until_element_is_visible(self.home_locators.article_item)
        for i in range(articles_limit):
            self.driver.execute_script("arguments[0].scrollIntoView();", article)
            likes = article.find_elements(*self.home_locators.article_likes)
            logger.info(f"likes elems: {likes}")
            if len(likes) > 0:
                likes = extract_likes(likes[-1].text)
                logger.info(f"likes: {likes}")
                if likes >= number_of_likes:
                    result = article
                    break
            article = article.find_element(*self.home_locators.next_article_item)
            self.driver.execute_script("arguments[0].scrollIntoView();", article)
        return result

    def get_chats(self):
        self.wait_until_element_is_visible(self.home_locators.chat_item)
        chats = self.driver.find_elements(*self.home_locators.chat_item)
        result = {}
        for chat in chats:
            name = self.driver.execute_script("return arguments[0].innerText;", chat).split("\n")[0]
            result[name] = chat
        logger.info(result)
        return result




