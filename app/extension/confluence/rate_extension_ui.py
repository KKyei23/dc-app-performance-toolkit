import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS

def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_pages']:
        app_specific_page_id = datasets['custom_page_id']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out
    @print_timing("selenium_app_specific_user_login")
    def measure():
         def app_specific_user_login(username='admin', password='admin'):
             login_page = Login(webdriver)
             login_page.delete_all_cookies()
             login_page.go_to()
             login_page.wait_for_page_loaded()
             login_page.set_credentials(username=username, password=password)
             login_page.click_login_button()
             if login_page.is_first_login():
                 login_page.first_user_setup()
             all_updates_page = AllUpdates(webdriver)
             all_updates_page.wait_for_page_loaded()
         app_specific_user_login(username='admin', password='admin')
     measure()

    #Log to page with rate macro, wait till visible then log out
    #log into page with rate search macro wait till visible then log out
    # Same two with blog pages


    # @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_rate_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={CONFLUENCE_SETTINGS.get_rate_page}")
            page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
            page.wait_until_visible((By.XPATH, "//table"))  # Wait for you app-specific UI element by ID selector
        sub_measure()
    measure()

    # @print_timing("selenium_app_rate_page")
    def measure():

        @print_timing("selenium_app_custom_action:rate_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={CONFLUENCE_SETTINGS.get_rate_page}")
            page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
            page.wait_until_visible((By.XPATH, "//table"))  # Wait for you app-specific UI element by ID selector
            rate = page.wait_until_visible((By.XPATH, "//a[@title='4 Star']"))
            rate.click()
        sub_measure()
    measure()

    @print_timing("selenium_app_rate_search")
    def measure():

        @print_timing("selenium_app_custom_action:view_rated_search_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={CONFLUENCE_SETTINGS.get_rate_search_page}")
            page.wait_until_visible((By.ID, "title-text"))
            page.wait_until_visible((By.XPATH, "//div[@data-macro-name='rate-search']"))
        sub_measure()
    measure()

    @print_timing("selenium_app_blog_rate")
    def measure():

        @print_timing("selenium_app_custom_action:rate_blog_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={CONFLUENCE_SETTINGS.get_rate_blog_page}")
            page.wait_until_visible((By.ID, "title-text"))
            page.wait_until_visible((By.CLASS_NAME, "rater"))
        sub_measure()
    measure()

    @print_timing("selenium_app_blog_rate_search")
    def measure():

        @print_timing("selenium_app_custom_action:view_rated_search_blogpage")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={CONFLUENCE_SETTINGS.get_rate_search_blog_page}")
            page.wait_until_visible((By.ID, "title-text"))
            page.wait_until_visible((By.XPATH, "//div[@data-macro-name='rate-search']"))
        sub_measure()
    measure()

