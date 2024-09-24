from pytest import fixture
from playwright.sync_api import sync_playwright
import settings

from page_object import initiations

@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture(scope='session')
def get_browser(get_playwright, request):
    user_browser = request.config.getoption('--browser')
    if not user_browser:
        user_browser = 'chromium'
    else:
        user_browser = user_browser[0]
    headless = request.config.getoption('--headless')
    if headless == 'True':
        headless = True
    else:
        headless = False
    if user_browser == 'chromium':
        browser = get_playwright.chromium.launch(headless=headless, args=['--start-maximized'])
    elif user_browser == 'firefox':
        browser = get_playwright.firefox.launch(headless=headless, args=['--start-maximized'])
    elif user_browser == 'webkit':
        browser = get_playwright.webkit.launch(headless=headless, args=['--start-maximized'])
    else:
        browser = get_playwright.chromium.launch(headless=headless, args=['--start-maximized'])
    yield browser
    browser.close()

@fixture(scope='session')
def get_objects(get_browser, request):
    base_url = request.config.getoption('--base_url')
    if base_url == "":
        base_url = settings.DEFAULT_URL
    print("URL: " + base_url)
    initiation_objects = initiations.Initiations(get_browser, base_url)
    yield initiation_objects
    initiation_objects.close()

@fixture(scope='function', autouse=True)
def setup_method(get_objects, request):
    get_objects.base_functionality.open_url(get_objects.base_url)
    yield
    get_objects.base_functionality.verify_count_of_errors_and_create_screenshot(request.session.testsfailed)

def pytest_addoption(parser):
    parser.addoption('--base_url', action='store', default='https://prom.ua/')
    parser.addoption('--headless', action='store', default='False')