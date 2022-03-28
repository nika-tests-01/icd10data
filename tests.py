import pytest

from page import MainPage
from page import SearchPage


def test_medical_codes(browser):
    browser.get(MainPage.PAGE_URL)

    # Step A
    current_url = browser.current_url
    url = browser.find_element(*MainPage.IMAGE_LOGO).get_property("src")
    assert current_url in url

    # Step B
    btn = browser.find_element(*MainPage.CODE_BTN).text
    assert btn == "Codes"

    # Step C
    browser.find_element(*MainPage.CODE_BTN).click()
    menu = browser.find_element(*MainPage.DROPDOWN_OPEN).find_element(*MainPage.DROPDOWN_MENU).get_attribute("class")
    assert menu == "dropdown-menu"

    # Step D
    search_bar_y = browser.find_element(*MainPage.SEARCH_BAR).location['y']
    assert search_bar_y < 20

    # Step E
    browser.find_element(*MainPage.INPUT_FIELD).click()
    browser.find_element(*MainPage.INPUT_FIELD).send_keys("Coronavirus")
    browser.find_element(*MainPage.SUBMIT_BTN).click()

    # Step F
    search_result = browser.find_element(*SearchPage.RESULTS).text
    assert "U07.1" in search_result

