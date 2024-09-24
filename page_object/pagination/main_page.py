from playwright.sync_api import Page, expect, Locator

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self._promua_promo_panel = self.page.locator("//div[@data-qaid='promo_panel']")
        self._promua_main_logo = self.page.locator("//a[@title='prom.ua']/img")
        self._promua_main_logo1 = self.page.locator("//a[@title='prom1.ua']/img")
        self._menu_preview_element = self.page.locator("//div[@data-qaid='menu_preview']")
        self._menu_preview_items = self.page.locator("//div[@data-qaid='menu_preview']//li/a")
        self._actual_banner_image = self.page.locator("//a[@data-qaid='banner_link']/img")
        self._recommended_categories_element = self.page.locator("//div[@data-qaid='recommended_categories']")
        self._personal_feed_element = self.page.locator("//div[@data-qaid='personal_feed_block']")

    def verify_default_main_page(self):
        expect(self._promua_promo_panel).to_be_visible()
        expect(self._promua_main_logo1).not_to_be_visible()
        expect(self._promua_main_logo).to_be_visible()
        expect(self._menu_preview_element).to_be_visible()
        expect(self._actual_banner_image.first).to_be_visible()
        expect(self._recommended_categories_element).to_be_visible()
        expect(self._personal_feed_element).to_be_visible()
        print("Main page elements verified")