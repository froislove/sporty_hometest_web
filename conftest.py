import os
import allure
import pytest
from configuration import PROJECT_ROOT
from clients.web_clients import create_mobile_driver


def pytest_configure(config):
    allure_dir = os.path.join(PROJECT_ROOT, "allure-results")
    config.option.allure_report_dir = allure_dir


@pytest.fixture
def mobile_driver(request):
    """
    Creating driver with target driver name
    """
    device_name = getattr(request, "param", "default")
    driver = create_mobile_driver(device_name)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("create_driver")
        if driver:
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(driver.current_url,
                          name="URL at failure",
                          attachment_type=allure.attachment_type.TEXT)
