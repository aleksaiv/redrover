import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import getenv
from dotenv import load_dotenv
load_dotenv(".env")

HUB_URL = getenv("HUB_URL", None)
options = Options()


@pytest.fixture()
def driver():
    if HUB_URL:
        drv = webdriver.Remote(command_executor=HUB_URL, options=options)
    else:
        drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()