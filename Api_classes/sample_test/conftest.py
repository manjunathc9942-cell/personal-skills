import os
import warnings
from datetime import datetime

import pytest
import urllib3


# ==========================================================
# HTML Report Title
# ==========================================================

def pytest_html_report_title(report):
    """
    Custom title for the HTML report.
    """
    report.title = "API Automation Test Report"


# ==========================================================
# PyTest Configuration
# ==========================================================

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Executes before the test session starts.
    - Suppresses SSL warnings
    - Creates Reports directory
    - Generates timestamped HTML report
    """

    # Suppress urllib3 SSL warning (macOS LibreSSL)
    warnings.filterwarnings(
        "ignore",
        category=urllib3.exceptions.NotOpenSSLWarning
    )

    # Create Reports directory if it doesn't exist
    report_dir = "Reports"
    os.makedirs(report_dir, exist_ok=True)

    # Timestamp for report
    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    # HTML Report
    config.option.htmlpath = os.path.join(
        report_dir,
        f"API_Automation_Report_{timestamp}.html"
    )

    # Embed CSS & JavaScript inside HTML
    config.option.self_contained_html = True


# ==========================================================
# Test Session Setup & Teardown
# ==========================================================

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    """
    Executes once before and after the entire test suite.
    """

    print("\n" + "=" * 60)
    print("Starting API Automation Test Execution")
    print("=" * 60)

    yield

    print("\n" + "=" * 60)
    print("API Automation Test Execution Completed")
    print("=" * 60)