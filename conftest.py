import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger


load_dotenv()
logger = get_logger(__name__)



def get_chrome_options():
    options = ChromeOptions()
    headless = eval(os.environ.get('HEADLESS'))
    if headless:
        options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    return options


@pytest.fixture(scope="class")
def driver():
    logger.info('starting browser')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=get_chrome_options())
    driver.implicitly_wait(os.getenv('IMPLICIT_WAIT', 5))
    yield driver
    logger.info('bye bye browser')
    driver.quit()

