import json
import os
import pytest
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load test data from JSON
with open(os.path.join("data", "home_page_expected_results.json"), "r", encoding="utf-8") as f:
    test_data = json.load(f)

expected_hero_header = test_data["hero"]["header"]
expected_hero_subheader = test_data["hero"]["subheader"]
expected_hero_menu_text = test_data["hero"]["menu_button_text"]
expected_hero_picture_src = test_data["hero"]["picture_src"]
expected_hero_menu_button_navigation = test_data["hero"]["menu_navigation"]
expected_urls = test_data["expected_urls"]
expected_banner_titles = [banner["title"] for banner in test_data["banners"]]
expected_banner_subtitles = [banner["subtitle"] for banner in test_data["banners"]]
expected_banner_image_sources = [banner["image_source"] for banner in test_data["banners"]]

@pytest.fixture(scope="function")
def home_page(driver):
    page = HomePage(driver)
    page.navigate("https://burgerking.ro/en/")
    # Accept cookies to avoid interference
    try:
        page.cookies_banner.click(page.cookies_banner.ACCEPT_ALL_COOKIES_BUTTON)
    except Exception:
        pass
    return page

def test_hero_header(home_page):
    # Verify that the hero header has the correct text.
    hero_header_text = home_page.find_element(home_page.HERO_HEADER).text.strip()
    assert hero_header_text == expected_hero_header, f"Hero Header does not have the correct text, got '{hero_header_text}'"

def test_hero_subheader(home_page):
    # Verify that the hero subheader has the correct text.
    hero_subheader_text = home_page.find_element(home_page.HERO_SUBHEADER).text.strip()
    assert hero_subheader_text == expected_hero_subheader, f"Hero Subheader does not have the correct text, got '{hero_subheader_text}'"

def test_hero_picture(home_page):
    # Verify that the hero picture has the correct image src.
    image_source_element = WebDriverWait(home_page.driver, 10).until(EC.presence_of_element_located(home_page.HERO_PICTURE))
    home_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", image_source_element)
    srcset_value = image_source_element.get_attribute("srcset")
    assert expected_hero_picture_src in srcset_value, f"Hero picture srcset does not contain the expected URL"

def test_hero_menu_button_text(home_page):
    # Verify that the hero menu button has the correct text.
    hero_menu_text = home_page.find_element(home_page.MENU_CALL_TO_ACTION_TEXT).text.strip()
    assert hero_menu_text == expected_hero_menu_text, f"Hero Menu Button does not have the correct text, got '{hero_menu_text}'"
    

def test_hero_menu_button_navigation(home_page):
    # Verify that the hero menu button leads to the correct page.
    menu_button = home_page.find_element(home_page.MENU_CALL_TO_ACTION_BUTTON)
    menu_button.click()
    WebDriverWait(home_page.driver, 10).until(
        EC.url_contains(home_page.driver.current_url)
    )
    assert expected_hero_menu_button_navigation in home_page.driver.current_url, \
        f"Clicking menu button did not navigate to '{expected_url}'"

def test_banners_and_buttons(home_page):
    # Verify that all cards have full functionality and meet expected results.
    card_elements = home_page.get_all_banner_button_locators()
    total_cards = home_page.get_number_of_cards()

    for idx, (banner_locator, banner_title_locator, banner_subtitle_locator, banner_image_source_locator, button_locator) in enumerate(card_elements, 0):
        if idx < total_cards:
            expected_url = expected_urls[idx]
            expected_title = expected_banner_titles[idx]
            expected_subtitle = expected_banner_subtitles[idx]

            # Scroll banner title into view
            WebDriverWait(home_page.driver, 10).until(EC.presence_of_element_located(banner_title_locator))
            banner_title_element = home_page.find_element(banner_title_locator)
            home_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", banner_title_element)

            # Verify that the Banner title text meets the expected results.
            banner_title = banner_title_element.text.strip()
            assert banner_title == expected_title, f"Banner {idx+1} does not have the correct title text"

            # Scroll banner subtitle into view
            WebDriverWait(home_page.driver, 10).until(EC.presence_of_element_located(banner_subtitle_locator))
            banner_subtitle_element = home_page.find_element(banner_subtitle_locator)
            home_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", banner_subtitle_element)

            # Verify that the Banner subtitle text meets the expected results.
            banner_subtitle = banner_subtitle_element.text.strip()
            assert banner_subtitle == expected_subtitle, f"Banner {idx+1} does not have the correct subtitle text"

            # Scroll image into view
            image_source_element = WebDriverWait(home_page.driver, 10).until(EC.presence_of_element_located(banner_image_source_locator))
            home_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", image_source_element)

            # Verify that the Banner image source meets the expected results.
            srcset_value = image_source_element.get_attribute("srcset")
            assert expected_banner_image_sources[idx] in srcset_value, f"Banner {idx+1} srcset does not contain the expected URL"

            # Scroll banner into view before clicking
            WebDriverWait(home_page.driver, 10).until(EC.element_to_be_clickable(banner_locator))
            banner_element = home_page.find_element(banner_locator)
            home_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", banner_element)

            # Verify that the Banner, upon clicking, navigates to the expected URL.
            home_page.click_element(banner_locator)
            WebDriverWait(home_page.driver, 10).until(EC.url_contains(expected_url))
            assert expected_url in home_page.driver.current_url, f"Banner {idx+1} did not navigate to expected URL"

            # Go back to home page
            home_page.driver.back()
            WebDriverWait(home_page.driver, 10).until(EC.presence_of_element_located(home_page.HERO_HEADER))

            # Scroll button into view before clicking
            WebDriverWait(home_page.driver, 10).until(EC.element_to_be_clickable(button_locator))
            button_element = home_page.find_element(button_locator)
            home_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_element)

            # Verify that the Button, upon clicking, navigates to the expected URL.
            home_page.click_element(button_locator)
            WebDriverWait(home_page.driver, 10).until(EC.url_contains(expected_url))
            assert expected_url in home_page.driver.current_url, f"Button {idx+1} did not navigate to expected URL"

            # Go back again for next iteration
            home_page.driver.back()
            WebDriverWait(home_page.driver, 10).until(EC.presence_of_element_located(home_page.HERO_HEADER))