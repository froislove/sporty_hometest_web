import allure
import pytest
from configuration import MOBILE_DEVICES
from helpers.actions import scroll_down
from services.web.twitch.pages import MainPage


@pytest.mark.parametrize("mobile_driver",
                         list(MOBILE_DEVICES.values()),
                         indirect=True)
@allure.story('Twitch UI testing')
@allure.title(f"Twitch stream search and capture screenshot")
def test_search_stream_and_get_screenshot(mobile_driver):
    """
    Parametrized test that verifies Twitch mobile UI allows searching for a channel and accessing a stream
    on different mobile devices.

    Steps:
    1. Open Twitch mobile site
    2. Accept cookies if present
    3. Click on the search icon
    4. Enter "StarCraft II" in the search input
    5. Select the "Channels" tab
    6. Scroll the results down twice
    7. Click on a random channel
    8. Handle any pop-up modals if present
    9. Wait for the stream to load
    10. Take a screenshot of the stream view

    Success criteria:
    - Streamer page is opened
    - Stream is loaded and rendered (video or canvas)
    - Screenshot is successfully captured

    This test must be executed in mobile emulation mode using a predefined device configuration.
    """

    driver = mobile_driver
    main_page = MainPage(driver)

    main_page.open()
    main_page.accept_cookies_if_needed()
    main_page.click_search_icon()
    main_page.input_search_query(query="StarCraft II")
    main_page.select_channels_tab()
    scroll_down(driver, times=2)

    streamer_page = main_page.select_stream()
    streamer_page.get_screenshot()
