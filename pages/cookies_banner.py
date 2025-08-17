from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CookiesBanner(BasePage):
    # Main Cookies Banner Locators
    ACCEPT_ALL_COOKIES_BUTTON = (By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
    REJECT_ALL_COOKIES_BUTTON = (By.CSS_SELECTOR, "#onetrust-reject-all-handler")
    COOKIES_SETTINGS_BUTTON = (By.CSS_SELECTOR, "#onetrust-pc-btn-handler")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.onetrust-close-btn-handler.onetrust-close-btn-ui.banner-close-button.ot-close-icon")

    # Cookies Settings Locators
    COOKIES_SETTINGS_ALLOW_ALL_BUTTON = (By.CSS_SELECTOR, "button#accept-recommended-btn-handler")
    COOKIES_SETTINGS_STRICTLY_NECESSARY_COOKIES_EXPAND_BUTTON = (By.CSS_SELECTOR, 'button[ot-accordion="true"][aria-controls="ot-desc-id-C0001"]')
    COOKIES_SETTINGS_FUNCTIONAL_COOKIES_EXPAND_BUTTON = (By.CSS_SELECTOR, 'button[ot-accordion="true"][aria-controls="ot-desc-id-C0003"]')
    COOKIES_SETTINGS_PERFORMANCE_COOKIES_EXPAND_BUTTON = (By.CSS_SELECTOR, 'button[ot-accordion="true"][aria-controls="ot-desc-id-C0002"]')
    COOKIES_SETTINGS_FUNCTIONAL_COOKIES_SWITCH_NOB = (By.CSS_SELECTOR, 'span.ot-switch-nob[aria-label="Functional Cookies"]')
    COOKIES_SETTINGS_PERFORMANCE_COOKIES_SWITCH_NOB = (By.CSS_SELECTOR, 'span.ot-switch-nob[aria-label="Performance Cookies"]')
    COOKIES_SETTINGS_REJECT_ALL_BUTTON = (By.CSS_SELECTOR, "button.ot-pc-refuse-all-handler")
    COOKIES_SETTINGS_CONFIRM_MY_CHOICES_BUTTON = (By.CSS_SELECTOR, "button.save-preference-btn-handler.onetrust-close-btn-handler")
    COOKIES_SETTINGS_CLOSE_BUTTON = (By.CSS_SELECTOR, "#close-pc-btn-handler")

    def __init__(self, driver):
        super().__init__(driver)

    # Main Cookies Banner Methods
    def click_accept_all_cookies_button(self):
        self.click(self.ACCEPT_ALL_COOKIES_BUTTON)

    def click_reject_all_cookies_button(self):
        self.click(self.REJECT_ALL_COOKIES_BUTTON)

    def click_cookies_settings_button(self):
        self.click(self.COOKIES_SETTINGS_BUTTON)

    def click_close_button(self):
        self.click(self.CLOSE_BUTTON)

    # Cookies Settings Methods
    def click_cookies_settings_allow_all_button(self):
        self.click(self.COOKIES_SETTINGS_ALLOW_ALL_BUTTON)

    def click_cookies_settings_strictly_necessary_cookies_expand_button(self):
        self.click(self.COOKIES_SETTINGS_STRICTLY_NECESSARY_COOKIES_EXPAND_BUTTON)

    def click_cookies_settings_functional_cookies_expand_button(self):
        self.click(self.COOKIES_SETTINGS_FUNCTIONAL_COOKIES_EXPAND_BUTTON)

    def click_cookies_settings_performance_cookies_expand_button(self):
        self.click(self.COOKIES_SETTINGS_PERFORMANCE_COOKIES_EXPAND_BUTTON)

    def click_cookies_settings_functional_cookies_switch_nob(self):
        self.click(self.COOKIES_SETTINGS_FUNCTIONAL_COOKIES_SWITCH_NOB)

    def click_cookies_settings_performance_cookies_switch_nob(self):
        self.click(self.COOKIES_SETTINGS_PERFORMANCE_COOKIES_SWITCH_NOB)

    def click_cookies_settings_reject_all_button(self):
        self.click(self.COOKIES_SETTINGS_REJECT_ALL_BUTTON)

    def click_cookies_settings_confirm_my_choices_button(self):
        self.click(self.COOKIES_SETTINGS_CONFIRM_MY_CHOICES_BUTTON)

    def click_cookies_settings_close_button(self):
        self.click(self.COOKIES_SETTINGS_CLOSE_BUTTON)