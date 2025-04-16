from selenium import webdriver
from configuration import LANGUAGE
from helpers.webdriver_helpers import get_driver_path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def create_mobile_driver(device_name: str) -> WebDriver:
    """
    Initialize driver using the Mobile emulator from Google Chrome
    :param device_name: device name for mobile emulation
    :return:
    """
    mobile_emulation = {
        "deviceName": device_name
    }

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    prefs = {
        "intl.accept_languages": LANGUAGE
    }
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(get_driver_path())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.device_name = device_name

    return driver
