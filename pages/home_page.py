from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.header import Header
from pages.footer import Footer
from pages.cookies_banner import CookiesBanner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    # Hero area locators
    HERO_HEADER = (By.CSS_SELECTOR, "#hero-header-wrapper")
    HERO_SUBHEADER = (By.CSS_SELECTOR, "#hero-subheader-wrapper")
    MENU_CALL_TO_ACTION_BUTTON = (By.CSS_SELECTOR, 'a[href^="/menu/section-"]')
    MENU_CALL_TO_ACTION_TEXT = (By.CSS_SELECTOR, 'a[href^="/menu/section-"] > span')
    HERO_PICTURE = (By.CSS_SELECTOR,'div[id="hero-image-wrapper"] > div[data-testid="picture-boundary"] picture > source')

    
    def get_number_of_cards(self):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="marketing-tile-group-grid"]'))
        )      
        cards = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="marketing-tile-group-grid"] > div')
        return len(cards)

    def get_banner_locator(self, index):
        locator_str = f'div[data-testid="marketing-tile-group-grid"] > div:nth-child({index}) > div > a'
        return (By.CSS_SELECTOR, locator_str)

    def get_banner_title_locator(self, index):
        locator_str = f'div[data-testid="marketing-tile-group-grid"] > div:nth-child({index}) > div > div > div > div:nth-child(1)'
        return (By.CSS_SELECTOR, locator_str)

    def get_banner_subtitle_locator(self, index):
        locator_str = f'div[data-testid="marketing-tile-group-grid"] > div:nth-child({index}) > div > div > div > div:nth-child(2)'
        return (By.CSS_SELECTOR, locator_str)

    def get_banner_image_source_locator(self, index):
        locator_str = f'div[data-testid="marketing-tile-group-grid"] > div:nth-child({index}) picture > source'
        return (By.CSS_SELECTOR, locator_str)

    def get_button_locator(self, index):
        locator_str = f'div[data-testid="marketing-tile-group-grid"] > div:nth-child({index}) > div > div > div > a'
        return (By.CSS_SELECTOR, locator_str)

    def get_all_banner_button_locators(self):
        count = self.get_number_of_cards()
        return [(self.get_banner_locator(i), self.get_banner_title_locator(i), self.get_banner_subtitle_locator(i), self.get_banner_image_source_locator(i), self.get_button_locator(i)) for i in range(1, count+1)]

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
        self.footer = Footer(driver)
        self.cookies_banner = CookiesBanner(driver)

    def click_element(self, locator):
        self.click(locator)