import time
import allure
from abc import abstractmethod, ABC
from selenium.webdriver.common.keys import Keys
from helpers.common_helpers import ensure_dir_exists
from helpers.webdriver_helpers import get_device_name
from configuration import TWITCH_MOBILE_URL, SCREENSHOTS_DIR
from helpers.actions import wait_for_element, wait_and_click_for_element, wait_and_click_random_element, \
    close_modal_if_present, wait_until_element_disappear, get_screenshot
from services.web.twitch.en_elements import TWITCH_MAIN_SEARCH_INPUT, \
    TWITCH_MAIN_ACCEPT_COOKIES, TWITCH_MAIN_FOLLOWING, TWITCH_MAIN_BROWSE, TWITCH_MAIN_CHANNELS, \
    TWITCH_STREAM_ELEMENT, STREAM_LOADING_SPINNER


class BasePage(ABC):
    """
    Base Page Object
    """

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def wait_until_loaded(self, timeout=15):
        pass


class MainPage(BasePage):
    """
    Object represents Twitch main page
    """

    def wait_until_loaded(self, timeout: int = 10) -> None:
        with allure.step(f"Waiting until {self.driver.current_url} will be loaded"):
            wait_for_element(self.driver, TWITCH_MAIN_FOLLOWING, timeout)

    @allure.step(f'Open main page {TWITCH_MOBILE_URL}')
    def open(self) -> None:
        self.driver.get(TWITCH_MOBILE_URL)
        self.wait_until_loaded()

    @allure.step("Accept cookies")
    def accept_cookies_if_needed(self) -> None:
        wait_and_click_for_element(self.driver, TWITCH_MAIN_ACCEPT_COOKIES, 3)

    @allure.step("Click the browse icon")
    def click_search_icon(self) -> None:
        wait_and_click_for_element(self.driver, TWITCH_MAIN_BROWSE, 3)

    @allure.step("Input search query")
    def input_search_query(self, query: str) -> None:
        input = wait_for_element(self.driver, TWITCH_MAIN_SEARCH_INPUT)
        input.send_keys(query)
        input.send_keys(Keys.RETURN)

    @allure.step("Select channels in main menu")
    def select_channels_tab(self) -> None:
        wait_and_click_for_element(self.driver, TWITCH_MAIN_CHANNELS)

    @allure.step("Select random stream and return Stream page")
    def select_stream(self):
        wait_and_click_random_element(self.driver, TWITCH_STREAM_ELEMENT)
        stream_page = StreamPage(self.driver)
        stream_page.wait_until_loaded()
        return stream_page


class StreamPage(BasePage):
    """
    Object represents page with stream
    """

    def wait_until_loaded(self, timeout: int = 200) -> None:
        with allure.step(f"Waiting until {self.driver.current_url} will be loaded"):
            close_modal_if_present(self.driver)
            wait_until_element_disappear(self.driver, STREAM_LOADING_SPINNER, timeout=timeout)

    def get_screenshot(self) -> None:
        with allure.step(f"Get screenshot of page {self.driver.current_url}"):
            device = get_device_name(self.driver)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            ensure_dir_exists(SCREENSHOTS_DIR)
            filename = f"{SCREENSHOTS_DIR}/screenshot_{device}_{timestamp}.png"
            screenshot = get_screenshot(self.driver)
            with open(filename, "ab") as f:
                f.write(screenshot)

            allure.attach(
                screenshot,
                name="twitch_stream_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
