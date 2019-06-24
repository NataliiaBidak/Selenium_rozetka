import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def populate_globals():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10000)  # seconds
    driver.maximize_window()
    driver.get("https://rozetka.com.ua/ua/")
    yield driver
    print("bye")
    driver.close()