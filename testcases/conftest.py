import os
from pathlib import Path
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# ======================================================
# Browser Fixture
# ======================================================

@pytest.fixture(scope="function")
def launch_browser():

    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def browser(launch_browser):
    return launch_browser


# ======================================================
# HTML Report Configuration
# ======================================================

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):

    report_dir = Path("Reports")
    report_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    report_file = report_dir / f"Automation_Report_{timestamp}.html"

    config.option.htmlpath = str(report_file)

    # External screenshots
    config.option.self_contained_html = True


# ======================================================
# Report Title
# ======================================================

def pytest_html_report_title(report):
    report.title = "Automation Execution Report"


# ======================================================
# Screenshot on Failure
# ======================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    pytest_html = item.config.pluginmanager.getplugin("html")

    extra = getattr(report, "extra", [])

    if report.when == "call":

        if report.failed:

            driver = None

            if "launch_browser" in item.funcargs:
                driver = item.funcargs["launch_browser"]

            elif "browser" in item.funcargs:
                driver = item.funcargs["browser"]

            if driver:

                screenshot_dir = Path("Screenshots")
                screenshot_dir.mkdir(exist_ok=True)

                file_name = (
                    report.nodeid
                    .replace("::", "_")
                    .replace("/", "_")
                    .replace("\\", "_")
                    + ".png"
                )

                screenshot_path = screenshot_dir / file_name

                driver.save_screenshot(str(screenshot_path))

                print(f"Screenshot saved : {screenshot_path}")

                if screenshot_path.exists():

                    html = f"""
                    <div>
                        <a href="../Screenshots/{file_name}" target="_blank">
                            <img src="../Screenshots/{file_name}"
                                 width="500"
                                 style="border:1px solid #d3d3d3;"
                                 onclick="window.open(this.src)" />
                        </a>
                    </div>
                    """

                    extra.append(pytest_html.extras.html(html))

    report.extra = extra