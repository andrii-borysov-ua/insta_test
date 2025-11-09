import pytest
from core.base_test import BaseTest
from utils.logger import get_logger


logger = get_logger(__name__)

@pytest.mark.usefixtures("login_to_the_app")
class TestHomePage(BaseTest):

    def test_read_messages(self):
        self.home_page.click_button_with_text("Messages")
        chats = self.home_page.get_chats()
        assert len(chats) > 0

    def test_check_likes_modal_window(self):
        article = self.home_page.search_article_by_likes_number(1000)
        article.find_element(*self.home_page.home_locators.article_likes).click()
        likes_modal = self.home_page.find_element_with_text(self.home_page.home_locators.modal_dialog, "Likes")
        assert likes_modal.is_displayed()

