from selenium.webdriver.common.by import By


# Elements locator constants for english localization


TWITCH_MAIN_FOLLOWING = (By.XPATH, "//p[contains(text(), 'Following')]")
TWITCH_MAIN_SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
TWITCH_MAIN_ACCEPT_COOKIES = (By.XPATH, "//div[contains(text(), 'Accept')]")
TWITCH_MAIN_BROWSE = (By.XPATH, "//div[contains(text(), 'Browse')]")
TWITCH_MAIN_CHANNELS = (By.XPATH, "//div[contains(text(), 'Channels')]")
TWITCH_STREAM_ELEMENT = (By.XPATH, "//button[contains(@class, 'tw-link')]")

STREAM_VIDEO_ELEMENT = (By.XPATH, "//div[contains(@data-test-selector, 'video-player__video-container')]")
STREAM_LOADING_SPINNER = (By.XPATH, '//div[contains(@class, "tw-loading-spinner")]')
