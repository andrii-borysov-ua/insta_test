from selenium.webdriver.common.by import By

class Locator:

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)
        if isinstance(attr, str):
            locator = eval(f'f"""{attr}"""')
            by = By.XPATH
        if isinstance(attr, tuple):
            by, locator = attr
            locator = eval(f'f"""{locator}"""')
        return [by, locator]

