from selenium import webdriver
from selenium.webdriver.chrome.options import Options

hub_url = "http://chrome:4444"
options = Options()

def test_main_page():
    driver = webdriver.Remote(command_executor=hub_url, options=options)
    driver.get("http://app_front:5173/")
    driver.save_screenshot("screenshot.png")
    driver.quit()