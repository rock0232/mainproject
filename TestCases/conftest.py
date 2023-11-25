import datetime
import re
import time
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from undetected_chromedriver.options import ChromeOptions
from pytest_html import html_report
from selenium import webdriver
from pathlib import Path
import pytest
import sys
import os
from utilities import xlutils
import allure


# read data from Excel file
def getwebsiteurl():
    websiteurl = []
    filepath = get_project_root()
    filepath = f"{filepath}/testdata/website_url.xlsx"
    rowcount = xlutils.getRowCount(filepath, sheetName="Sheet1")

    for i in range((rowcount + 1)):
        if i > 1:
            url = xlutils.readData(filepath, sheetName="Sheet1", rownum=i, columnno=2)
            name = xlutils.readData(filepath, sheetName="Sheet1", rownum=i, columnno=1)
            websiteurl.append(url)
            break
    return websiteurl


def get_project_root() -> Path:
    return Path(__file__).parent.parent


@pytest.fixture(params=xlutils.read_sheet())
def website_list(request):
    return request.param


@pytest.fixture()
def setup():
    global driver
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--start-fullscreen')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--disable-blink-features")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--single-process')

    # chrome_options.add_argument("--no-incognito")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    capabilities = webdriver.DesiredCapabilities().CHROME.copy()
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True

    # driver = uc.Chrome(chrome_options=chrome_options)
    driver = uc.Chrome()
    stealth(driver,

            languages=["en-US", "en"],

            vendor="Google Inc.",

            platform="Win32",

            webgl_vendor="Intel Inc.",

            renderer="Intel Iris OpenGL Engine",

            fix_hairline=True,

            )
    driver.execute_cdp_cmd('Emulation.setUserAgentOverride', {

        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",

        "platform": "Win64",

        "acceptLanguage": "ro-RO"

    })

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_example(setup):
    driver = setup
    driver.get("https://aura25.bet")
    time.sleep(1000)
    # print(f"WebDriver binary location: {setup.binary_location}")
    zip_name = "chromedriver_%s.zip"
    exe_name = "chromedriver%s"

    platform = sys.platform
    if platform.endswith("win32"):
        zip_name %= "win32"
        exe_name %= ".exe"
    if platform.endswith(("linux", "linux2")):
        zip_name %= "linux64"
        exe_name %= ""
    if platform.endswith("darwin"):
        zip_name %= "mac64"
        exe_name %= ""

    if platform.endswith("win32"):
        d = "~/appdata/roaming/undetected_chromedriver"
    elif "LAMBDA_TASK_ROOT" in os.environ:
        d = "/tmp/undetected_chromedriver"
    elif platform.startswith(("linux", "linux2")):
        d = "~/.local/share/undetected_chromedriver"
    elif platform.endswith("darwin"):
        d = "~/Library/Application Support/undetected_chromedriver"
    else:
        d = "~/.undetected_chromedriver"
    data_path = os.path.abspath(os.path.expanduser(d))
    print(data_path)


# os.path.abspath(os.path.expanduser(d))

def pytest_html_report_title(report):
    report.title = "Test Result Report"


def getcurrenturl():
    url = driver.current_url
    urllst = []
    for i in url:
        if i == "#":
            break
        else:
            urllst.append(i)
    newurl = "".join(urllst)
    return str(newurl + "#/login")

#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#
#     if report.when == 'call':
#         xfail = hasattr(report, 'wasxfail')
#         filepath = os.getcwd()
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             pattern = r"[^\w]"
#             date = str(datetime.datetime.now())
#             test_node = report.nodeid.replace("::", "_") + date
#             file_name = re.sub(pattern, "", test_node) + ".png"
#             _capture_screenshot(f'Screenshots/{file_name}')
#
#             # file_path = f"http://159.65.148.205:8000/{file_name}"
#             file_path = f"{filepath}/Screenshots/{file_name}"
#             if file_name:
#                 html = '<div> <img src="%s"' \
#                        ' alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_path
#                 extra.append(pytest_html.extras.html(html))
#                 extra.append(pytest_html.extras.url(getcurrenturl(), name=getcurrenturl()))
#     report.extra = extra
#     # driver.quit()


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


# @allure.step("Taking screenshot on failure")
def take_screenshot(driver, name):
    allure.attach(driver.get_screenshot_as_png(), name, allure.attachment_type.PNG)

def pytest_exception_interact(node, call, report):
    if report.failed:
        pattern = r"[^\w]"
        date = str(datetime.datetime.now())
        test_node = report.nodeid.replace("::", "_") + date
        file_name = re.sub(pattern, "", test_node) + ".png"
        take_screenshot(driver, file_name)

def pytest_configure(config):
    config._metadata["Project Name"] = "Mainproject"
    config._metadata['Module Name'] = "Test Place Bet"
    config._metadata['Tester'] = "Rock"
    config._metadata['Browser'] = "Chrome"

    """# It is hook for delete/Modify Environment info to HTML Report"""


@pytest.mark.optionalhook(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", "pytest, pytest-html, selenium")

# def exception_handler(exception_type, exception, traceback, debug_hook=sys.excepthook):
#     debug_hook(exception_type, exception, traceback)

# --show-capture={no,stdout,stderr,log,all}
# python -m pytest -m regression -s -v --show-capture={no,stdout,stderr,log,all} --html=Reports\reportsnew2.html testCases/test_placebet.py
# python -m pytest --capture=tee-sys -v -s --html=Reports\reports.html testCases\test_placebet.py --workers auto
# pytest -v -s test_file.py --workers auto
# python -m pytest --capture=tee-sys -s -v -n=5 --html=Reports\reports.html testCases\test_placebet.py
# python -m pytest -s -v -n=2 --html=Reports\reports.html testCases\test_placebet.py
# python -m pytest -n=3 TestCases/test_login.py
# python -m pytest -s -v --capture=tee-sys --html=Reports\reports.html testCases/login_test.py
# python -m pytest -m regression -s -v --capture=sys --log-cli-level=INFO --html=Reports\finalreport.html --self-contained-html testCases/test_placebet.py
# python -m pytest -m regression --capture= --html=Reports\finalreport.html --self-contained-html testCases/test_placebet.py
# python -m pytest -m regression -s -v --capture=sys -rF --html=Reports\finalreport.html --self-contained-html testCases/test_placebet.py
# python -m pytest --markers -m newmarker -s -v --capture=sys --html=Reports\finalreport.html --self-contained-html testCase
# s/test_placebet.py
# python -m pytest -m testmarker -s -v --capture=sys --html=Reports\finalreport.html --self-contained-html testCases/test_placebet.py
# allure serve "E:\Rock_Selenium\Automation Project\mainproject\Reports"
# pytest -v -s --alluredir="E:\Rock_Selenium\Automation Project\mainproject\Reports" --tb=no -p no:warnings TestCases\rough.py
