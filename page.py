from selenium.webdriver.common.by import By


class MainPage:
    PAGE_URL = "https://www.icd10data.com"
    IMAGE_LOGO = (By.CLASS_NAME, "img-responsive")
    CODE_BTN = (By.CSS_SELECTOR, "#navMenu > li:nth-child(1) > a")
    DROPDOWN_OPEN = (By.CSS_SELECTOR, "#navMenu > li.dropdown.open")
    DROPDOWN_MENU = (By.CLASS_NAME, "dropdown-menu")
    SEARCH_BAR = (By.CLASS_NAME, "form-group")
    INPUT_FIELD = (By.ID, "searchText")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[id = 'search']")


class SearchPage:
    RESULTS = (By.CLASS_NAME, "searchKeywords")

