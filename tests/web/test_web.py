from ..api.config import WEB_URL
from selenium.webdriver.common.by import By

def test_main_page(driver):
    driver.get(WEB_URL)
    element = driver.find_element(by=By.XPATH, value="*//div/div/h1")
    assert element.text.casefold() == "импортзамещенная тестовая система"

