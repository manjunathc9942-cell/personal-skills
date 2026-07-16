import warnings
import urllib3
import os
import pytest
from datetime import datetime


def pytest_html_report_title(report):
    report.title = "API Automation Test Report"  # <-- Change your title name here!

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # 1. Mute that annoying NotOpenSSLWarning across the entire pytest session
    warnings.filterwarnings("ignore", category=urllib3.exceptions.NotOpenSSLWarning)

    # 2. Safely handle the report directory creation
    report_dir = "reports"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # 3. Add timestamp to report file name
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSetting up resources...")
    yield
    print("\nTearing down resources...")