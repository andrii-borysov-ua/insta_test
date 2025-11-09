from locators import Locator


class HomePageLocators(Locator):
    save_login_info_not_now_link = '//*[text()="Not now"]'

    modal_dialog = '//div[@role="dialog" and .//*[text()="%s"]]'
    element_button = './/*[@role="button" and text()="%s"]'

    menu_item = '//a[@role="link" and .//span[text()="%s"] or .//*[@aria-label="%s"]]'

    story_tray = '//div[@data-pagelet="story_tray"]'
    story_next_button = story_tray + '//button[@aria-label="Next"]/div'
    story_back_button = story_tray + '//button[@aria-label="Go back"]/div'
    story_item = story_tray + '//li/div[contains(@aria-label,"Story by")]'
    story_live_item = story_item + '//span[text()="LIVE"]'

    chat_item = '//div[@aria-label="Chats"]//*[@role="button"]'
    chat_unread = '//div[@aria-label="Chats"]//*[@role="button" and .//*[text()="Unread"]]'


    article_item = '//article'
    next_article_item = './following-sibling::*[1]'
    article_header = './div/div[1]'
    article_body = './div/div[2]'
    article_next_button = article_body + '//button[@aria-label="Next"]'
    article_back_button = article_body + '//button[@aria-label="Go back"]'
    article_futter = './div/div[3]'
    article_owner = article_header + '//span[@style and @dir="auto"]//a[@role="link"]'
    article_more_options = article_header + '//*[@aria-label="More options"]'
    article_like_button = article_futter + '//*[@aria-label="Like"]'
    article_comment_button = article_futter + '//*[@aria-label="Comment"]'
    article_share_button = article_futter + '//*[@aria-label="Share"]'
    article_save_button = article_futter + '//*[@aria-label="Save"]'
    article_likes = article_futter + '//span[a[contains(@href,"liked_by")]]'


