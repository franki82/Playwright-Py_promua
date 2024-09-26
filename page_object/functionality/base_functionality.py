from playwright.sync_api import Page
from datetime import datetime
from pathlib import Path

class BaseFunctionality:

    def __init__(self, page: Page):
        self.page = page
        self.counter_errors_in_class = 0

    def open_url(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state()

    def pause(self, timeout_in_sec: int):
        self.page.wait_for_timeout(timeout_in_sec * 1000)

    def _create_screenshot(self):
        project_path = Path(__file__).parent.parent.parent
        path_to_log = str(project_path) + '/log/'
        screenshot_file_name = "screenshot" + str(datetime.now()) + ".png"
        self.page.screenshot(path=path_to_log + screenshot_file_name)
        print("screenshot: " + screenshot_file_name)

    def verify_count_of_errors_and_create_screenshot(self, current_counter_of_error):
        if current_counter_of_error > self.counter_errors_in_class:
            self.counter_errors_in_class = current_counter_of_error
            self._create_screenshot()

    def verify_true(self, condition, error_message):
        assert condition, error_message
