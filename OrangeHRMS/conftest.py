from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager # <-- Add this import at the top
from time import sleep
import base64


BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"
password = "admin123"

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    
    # 1. Correct Service syntax and Capital 'C' in Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_option)
    
    # 2. Assign to class (for your tests) AND to node (for the report screenshot hook)
    request.cls.driver = driver
    request.node.driver = driver
    
    # yield driver
    # sleep(3)
    # driver.quit()

#  Correct spelling
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Enforces self-contained HTML reports
    today = datetime.now()
    date_str = datetime.today().strftime("%Y%m%d")
    report_dir = Path(f"hrmreport_{date_str}")
    report_dir.mkdir(parents=True, exist_ok= True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html 
    config.option.self_contained_html = True


@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    """
    Sets the document title for the generated HTML report.
    """
    report.title = "HRM Test Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    pytest_html = item.config.pluginmanager.getplugin("html")
    extra = getattr(report, "extra", [])

    if report.when == "call":
        if report.failed:
            # 1. Fetch the driver from the item node where browser_setup stored it
            driver = getattr(item, "driver", None)

            # Fallback: check the class if it's not directly on the item node
            if driver is None and item.cls:
                driver = getattr(item.cls, "driver", None)

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
                    # Read the local file and encode it as a Base64 string
                    with open(screenshot_path, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

                    # Embed the string directly. This displays inside your self-contained report!
                    html = f"""
                    <div>
                        <img src="data:image/png;base64,{encoded_string}"
                             width="500"
                             style="border:1px solid #d3d3d3; cursor:pointer;"
                             onclick="window.open(this.src)" />
                    </div>
                    """
                    extra.append(pytest_html.extras.html(html))

    report.extra = extra