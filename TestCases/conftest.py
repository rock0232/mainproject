import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from pathlib import Path
from pytest_html import html_report


def get_project_root() -> Path:
    return Path(__file__).parent.parent


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    global driver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # optional
    chrome_options.add_argument('--no-sandbox')
    # optional
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)


# @pytest.fixture()
# def setup():
#     global driver
#     filepath = get_project_root()
#     # serv_obj = Service(f'{filepath}/chromedriver.exe')
#     # serv_obj = Service("/var/lib/jenkins/workspace/demo/chromedriver.exe")
#     # serv_obj = Service("/var/lib/jenkins/workspace/demo/chromedriver.exe")
#
#     # live server
#
#     serv_obj = Service("/usr/local/bin/chromedriver.deb")
#
#     # driver = webdriver.Chrome(executable_path="f{filepath}/chromedriver.exe")
# #     driver = webdriver.Chrome()
#     driver = webdriver.Chrome(service=serv_obj)
#     driver.implicitly_wait(10)
#     return driver

# @pytest.fixture()
# def setup():
#     # Initialize Chrome Driver
#     global driver
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     driver = webdriver.Chrome(options=chrome_options)
#
#     # Return Chrome Driver instance
#     yield driver
#
#     # Teardown Chrome Driver instance
#     driver.quit()


def pytest_html_report_title(report):
    report.title = "Test Result Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        filepath = os.getcwd()
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            file_path = f"{filepath}//{file_name}"
            if file_name:
                html = '<div> <img src="%s"' \
                       ' alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path
                extra.append(pytest_html.extras.html(html))
                driver.quit()
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


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
