from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver

_cached_path = None


def get_driver_path():
    """
    Choose necessary chrome driver
    :return:
    """
    global _cached_path
    if _cached_path is None:
        _cached_path = ChromeDriverManager().install()
    return _cached_path


def get_device_name(driver: WebDriver) -> str:
    """
    Return current device name
    :param driver:
    :return: custom device attribute
    """
    return getattr(driver, "device_name", "unknown-device").replace(" ", "_")
