from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Footer(BasePage):
    PRIVACY_POLICY_BUTTON = (By.CSS_SELECTOR, "a[href='/en/privacy-policy']")
    COOKIES_POLICY_BUTTON = (By.CSS_SELECTOR, "a[href='/en/cookie-policy']")
    TERMS_OF_SERVICE_BUTTON = (By.CSS_SELECTOR, "a[href='/en/terms-of-service']")
    ALLERGENS_BUTTON = (By.CSS_SELECTOR, "a[href='/en/allergens']")
    INGREDIENTS_BUTTON = (By.CSS_SELECTOR, "a[href='/en/ingredients']")
    CONTACT_BUTTON = (By.CSS_SELECTOR, "a[href='/en/contact']")
    REGULATIONS_BUTTON = (By.CSS_SELECTOR, "a[href='/en/regulamente']")
    COOKIES_PREFERENCES_BUTTON = (By.XPATH, "//span[normalize-space(text())='Cookie Preferences']")
    FOOTER_LANGUAGE_BUTTON = (By.CSS_SELECTOR, "footer button[data-testid=language-selector-button]")
    INSTAGRAM_BUTTON = (By.CSS_SELECTOR, "a[href='https://www.instagram.com/burgerkingro/']")
    FACEBOOK_BUTTON = (By.CSS_SELECTOR, "a[href='https://www.facebook.com/BurgerKingRO']")
    YOUTUBE_BUTTON = (By.CSS_SELECTOR, "a[href='https://www.youtube.com/@burgerkingromania']")
    TIKTOK_BUTTON = (By.CSS_SELECTOR, "a[href='https://www.tiktok.com/@burgerkingro']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_privacy_policy_button(self):
        self.click(self.PRIVACY_POLICY_BUTTON)

    def click_cookies_policy_button(self):
        self.click(self.COOKIES_POLICY_BUTTON)

    def click_terms_of_service_button(self):
        self.click(self.TERMS_OF_SERVICE_BUTTON)

    def click_allergens_button(self):
        self.click(self.ALLERGENS_BUTTON)

    def click_ingredients_button(self):
        self.click(self.INGREDIENTS_BUTTON)

    def click_contact_button(self):
        self.click(self.CONTACT_BUTTON)

    def click_regulations_button(self):
        self.click(self.REGULATIONS_BUTTON)

    def click_cookies_preferences_button(self):
        self.click(self.COOKIES_PREFERENCES_BUTTON)

    def click_footer_language_button(self):
        self.click(self.FOOTER_LANGUAGE_BUTTON)

    def click_instagram_button(self):
        self.click(self.INSTAGRAM_BUTTON)

    def click_facebook_button(self):
        self.click(self.FACEBOOK_BUTTON)

    def click_youtube_button(self):
        self.click(self.YOUTUBE_BUTTON)

    def click_tiktok_button(self):
        self.click(self.TIKTOK_BUTTON)