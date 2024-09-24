from playwright.sync_api import Browser, expect
from page_object.functionality.general_search import GeneralSearch
from page_object.pagination.main_page import MainPage
from page_object.functionality.base_functionality import BaseFunctionality


class Initiations:
    def __init__(self, browser: Browser, base_url: str):
        self.browser = browser
        self.context = self.browser.new_context(no_viewport=True)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.general_search = GeneralSearch(self.page)
        self.main_page = MainPage(self.page)
        self.base_functionality = BaseFunctionality(self.page)
        print("Class Initiated")

    def close(self):
        self.page.close()
        self.context.close()
        print("All Connections Closed")