import time
import pytest
import allure
import random
from typing import Union, Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException


def wait_and_click_for_element(driver: WebDriver,
                               locator: Union[WebElement, Tuple[str, str]],
                               timeout: int = 10) -> None:
    with allure.step(f"Wait and click to element {locator[1]}"):
        try:
            WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except (NoSuchElementException, TimeoutException):
            pytest.fail(f"No element {locator[1]} was discovered during {timeout} sec")


def wait_for_element(driver: WebDriver,
                     locator: Union[WebElement, Tuple[str, str]],
                     timeout: int = 10) -> WebElement:
    with allure.step(f"Wait for element {locator[1]}"):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except (NoSuchElementException, TimeoutException):
            pytest.fail(f"No element {locator[1]} was discovered during {timeout} sec")


def scroll_down(driver: WebDriver, times: int = 2, pause: int = 1):
    """
    Scroll down a given number of times with a pause
    :param driver: WebDriver
    :param times: number of scroll down actions
    :param pause: sec to sleep
    :return:
    """
    with allure.step(f"Scroll down {times} times"):
        viewport_height = driver.execute_script("return window.innerHeight")

        for _ in range(times):
            driver.execute_script("window.scrollBy(0, arguments[0]);", viewport_height)
            time.sleep(pause)


def wait_and_click_random_element(driver: WebDriver,
                                  locator: Union[WebElement, Tuple[str, str]],
                                  timeout: int = 10) -> None:
    with allure.step(f"Wait and click for random element {locator[1]}"):
        try:
            elements = WebDriverWait(driver, timeout).until(
                EC.visibility_of_any_elements_located(locator)
            )
            element = random.choice(elements)
            element.click()

        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", element)

        except (NoSuchElementException, TimeoutException):
            pytest.fail(f"No elements of {locator[1]} locator was discovered during {timeout} sec")


def close_modal_if_present(driver: WebDriver, timeout: int = 5) -> None:
    with allure.step(f"Wait and close modals"):
        text_options = ["Start Watching", "I understand", "Accept"]
        try:

            for option in text_options:
                locator = (By.XPATH, f"//*[contains(text(), '{option}')]")
                WebDriverWait(driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                ).click()
        except TimeoutException:
            pass


def wait_until_element_disappear(driver: WebDriver,
                                 locator: Union[WebElement, Tuple[str, str]],
                                 timeout: int = 10) -> None:
    with allure.step(f"Wait until element {locator[1]} will disappear"):
        try:
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )

        except TimeoutException:
            pytest.fail(f"Element {locator[1]} didn't disappear in {timeout} sec")


def get_screenshot(driver: WebDriver) -> bytes:
    screenshot = driver.get_screenshot_as_png()
    return screenshot
