from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Header(BasePage):
    MENU_BUTTON = (By.CSS_SELECTOR, "a[data-testid=Menu]")
    RESTAURANTS_BUTTON = (By.CSS_SELECTOR, "a[data-testid=Restaurants]")
    COUPONS_BUTTON = (By.CSS_SELECTOR, "a[data-testid=Coupons]")
    LOGO_BUTTON = (By.CSS_SELECTOR, "div[data-testid=desktop-header-logo]")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button[data-testid=desktop-signup-link]")
    HEADER_LANGUAGE_BUTTON = (By.CSS_SELECTOR, "header button[data-testid=language-selector-button]")
    HAMBURGER_BUTTON = (By.CSS_SELECTOR, "button[data-testid=side-nav-action-btn]")
    HAMBURGER_ABOUT_US_BUTTON = (By.CSS_SELECTOR, "a[href='/en/about-us']")
    HAMBURGER_ALLERGENS_BUTTON = (By.CSS_SELECTOR, "a[href='/en/allergens']")
    HAMBURGER_COOKIES_PREFERENCES_BUTTON = (By.XPATH, "//a[normalize-space(text())='Cookie Preferences']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_menu_button(self):
        self.click(self.MENU_BUTTON)

    def click_restaurants_button(self):
        self.click(self.RESTAURANTS_BUTTON)

    def click_coupons_button(self):
        self.click(self.COUPONS_BUTTON)

    def click_logo_button(self):
        self.click(self.LOGO_BUTTON)

    def click_sign_up_button(self):
        self.click(self.SIGN_UP_BUTTON)

    def click_header_language_button(self):
        self.click(self.HEADER_LANGUAGE_BUTTON)

    def click_hamburger_button(self):
        self.click(self.HAMBURGER_BUTTON)

    def click_hamburger_about_us_button(self):
        self.click(self.HAMBURGER_ABOUT_US_BUTTON)

    def click_hamburger_allergens_button(self):
        self.click(self.HAMBURGER_ALLERGENS_BUTTON)

    def click_hamburger_cookies_preferences_button(self):
        self.click(self.HAMBURGER_COOKIES_PREFERENCES_BUTTON)