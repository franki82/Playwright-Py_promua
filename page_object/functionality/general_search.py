from playwright.sync_api import Page, expect, Locator

class GeneralSearch:
    def __init__(self, page: Page):
        self.page = page
        self._search_input = self.page.locator("//input[@name='search_term']")
        self._start_search_button = self.page.locator("//button[@data-qaid='search_btn']")
        self._search_results_element = self.page.locator("//div[@data-qaid='product_gallery']")
        self._search_results_items = self.page.locator("//div[@data-qaid='product_gallery']//div[@data-product-id]")
        self._search_count_of_items = self.page.locator("//div[@data-qaid='pagination']/div/span")
        self._product_description_xpath = "div//span[@data-qaid='product_name']"

    def simple_search(self, search_value):
        expect(self._search_input).to_be_visible()
        expect(self._start_search_button).to_be_visible()
        expect(self._start_search_button).to_have_attribute("disabled", "")
        self._search_input.fill(search_value)
        expect(self._start_search_button).not_to_have_attribute("disabled", "")
        expect(self._search_input).to_have_value(search_value)
        self._start_search_button.click()
        self.page.wait_for_load_state()

    def get_product_plates(self):
        expect(self._search_results_element).to_be_visible()
        self._search_count_of_items.scroll_into_view_if_needed()
        self.page.wait_for_load_state(state='networkidle')
        return self._search_results_items.all()

    def get_product_description(self, plate_element:Locator):
        return plate_element.locator('xpath='+self._product_description_xpath).text_content()