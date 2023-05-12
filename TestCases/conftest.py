from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pytest_html import html_report
from selenium import webdriver
from pathlib import Path
import pytest
import sys
import os


def get_project_root() -> Path:
    return Path(__file__).parent.parent


# newlist = [
#     {"website_name": "https://aura25.bet/#/login",  # aura25
#      "name": "cf_clearance",
#      "value": "4FQofPYfRcOaDErKc33RjqrMJLYqdaLrDTv5LDm7zRY-1683875838-0-150"
#      },
#     {"website_name": "https://gamex24.com/#/login",  # gamex
#      "name": "cf_clearance",
#      "value": "hr.biwKQL3llsQe0r0zg1M0nq.JqHVUJh_7w2KMPy5U-1683881227-0-150"
#      }]
websitelist = [
    {"website_name": "https://aura24.bet",
     "name": "cf_clearance",
     "value": "cIJrL1OgNqnhg0FkLrbYcseS1e.JhHKrnikqhnuRUdo-1683896194-0-150"},
    {"website_name": "https://park.bet",
     "name": "cf_clearance",
     "value": "E60dRhqHgFZkS96O4LKzS2ivsFeZOHFoDaa_Wek6BwM-1683896434-0-150"},
    {"website_name": "https://greenexch.com",
     "name": "cf_clearance",
     "value": "q9DjSDXuAa9PRkFvxYvgNXmSfANXYcPucq4pcFE9_0M-1683896382-0-150"},
    {"website_name": "https://best365.in",
     "name": "cf_clearance",
     "value": "PryrxXph4RidZugoHWav2q4RP54WjV.ofhWLzkkvE4Y-1683896475-0-150"},
    {"website_name": "https://parkinplay.net",
     "name": "cf_clearance",
     "value": "J5Lql9E4wsfo9MWkeI1V58s8rjTdq8jPZvDQcWYqmaE-1683896703-0-150"},
    {"website_name": "https://butterflyexch.net",
     "name": "cf_clearance",
     "value": "TFG1NX.55ciseU5WPtFNTHCrpHaL2mfwqcsi2PpDt80-1683896739-0-150"},
    {"website_name": "https://probook9.net",
     "name": "cf_clearance",
     "value": "ggkeijDUCbqcGE_mP65soGh9JzDxiG8loGrHsGQwfbk-1683897429-0-150"},
    {"website_name": "https://11wonder.net",
     "name": "cf_clearance",
     "value": "QOUB.ZWczy7JNynIdndgivAEcFHibKGlEGJAyDN4vVs-1683897404-0-150"},
    {"website_name": "https://winexch.net",
     "name": "cf_clearance",
     "value": "QH.R_QoLAoXjzUtv4agKf_LB98UzqinIZsUQDtg8hNQ-1683897379-0-150"},
    {"website_name": "https://runexch.net",
     "name": "cf_clearance",
     "value": "5OkCAsThwyhqNk2e3Y2XsgP5lE9x.1_pBkb3XeZIcuo-1683897504-0-150"},
    {"website_name": "https://cricbuz.net",
     "name": "cf_clearance",
     "value": "rKblRGSbpI2N3gQM_Ef7uTamgF6Nd8Yy6De6hWuQWWk-1683897523-0-150"},
    {"website_name": "https://orange11.net",
     "name": "cf_clearance",
     "value": "XVQ1rpJDpUMemQjPCgkA7h._.56oW.M1tOQjk7zmon8-1683897560-0-150"},
    {"website_name": "https://khelo365.biz",
     "name": "cf_clearance",
     "value": "sEOWo9fJHxArK0gKW8Vn6D8pv2W.j9Tpli9.Au0cS1k-1683897593-0-150"},
    {"website_name": "https://bright99.biz",
     "name": "cf_clearance",
     "value": "MOsBJRFg4lmbDLLTef48nYFKuGQ.XmY1yiGihLDGSIo-1683897635-0-150"},
    {"website_name": "https://powerbets.biz",
     "name": "cf_clearance",
     "value": "gFucNdVSWr2TyuEK6aXSizlTMd3ScbzsqNsn.eTGFvw-1683897720-0-150"},
    {"website_name": "https://9skyexch.com",
     "name": "cf_clearance",
     "value": "s.wlQMFYHx97wMXSX_AifaqozP1RnCffNI.AQKu_yqk-1683897757-0-150"},
    {"website_name": "https://spice11.in",
     "name": "cf_clearance",
     "value": "8alu9rfv1gxAwafHHx9kIRgI.U5YsnLCJk3NwaItheo-1683897790-0-150"},
    {"website_name": "https://gold9.in",
     "name": "cf_clearance",
     "value": "5rco2ZLfIMdiEoYaXXXukH1WRu39g31aEJ93tbIBcck-1683897859-0-150"},
    {"website_name": "https://fancybook.live",
     "name": "cf_clearance",
     "value": "dTmQtpfHeeo1qzYRag7apjUyHgGPvTCZecXTs7dnm9s-1683897882-0-150"},
    {"website_name": "https://skyexch1.net",
     "name": "cf_clearance",
     "value": "yUBtDtMa0GZZnplaln4nbsM2EPcVgC4XOLr.TakLtjM-1683897912-0-150"},
    # {"website_name": "https://probet9.net",
    #  "name": "cf_clearance",
    #  "value": ""},
    {"website_name": "https://Sunexchange.in",
     "name": "cf_clearance",
     "value": "4FQofPYfRcOaDErKc33RjqrMJLYqdaLrDTv5LDm7zRY-1683875838-0-150"},
    {"website_name": "https://7xbet.bet",
     "name": "cf_clearance",
     "value": "HhRjfd0kGINuAdkFi6M3UVjgWHuerbNX8JMWix8v7tA-1683898078-0-150"},
    {"website_name": "https://saiexch24.com",
     "name": "cf_clearance",
     "value": "yPcEklgElcrHC6fXPReGkK.5.kOp0qs3lbgHd_7b6jk-1683898100-0-150"},
    {"website_name": "https://lords99.com",
     "name": "cf_clearance",
     "value": "tctF2vBVUl62by5afKb1HokGDVdnBOoQOfUB_iRXH0k-1683898127-0-150"},
    {"website_name": "https://bengal22.bet",
     "name": "cf_clearance",
     "value": "yRs6DSJp_6x94yXtW7YTguv8GNyvBAdFQ1zO_3f2TN4-1683898152-0-150"},
    {"website_name": "https://all365day.com",
     "name": "cf_clearance",
     "value": "hJukuo.fr0DhDgjSKzPLgjIpegjh.3EMhpdmLhO30e8-1683898181-0-150"},
    {"website_name": "https://Spworld365.com",
     "name": "cf_clearance",
     "value": "4FQofPYfRcOaDErKc33RjqrMJLYqdaLrDTv5LDm7zRY-1683875838-0-150"},
    {"website_name": "https://euro11.net",
     "name": "cf_clearance",
     "value": "t0P4ef0LFHiI9NGQ1hWXQGkJum2OiazNQuLPMJj5tfg-1683898260-0-150"},
    {"website_name": "https://royalbet444.vip",
     "name": "cf_clearance",
     "value": "CMZGCcrB4jzjr9DipJ2u1FZcS2H9wIcLeGHoUWJsw_s-1683898289-0-150"},
    {"website_name": "https://playwin247.bet",
     "name": "cf_clearance",
     "value": "RX817mX3YO1liOqn3kFKydgqmTggFd9XQVPleTAMh5A-1683898328-0-150"},
    {"website_name": "https://jk3434.bet",
     "name": "cf_clearance",
     "value": "icWYK0R5QwY_jiaywzeOdbAtIg5ebuS9vd3lmfXIZIA-1683898363-0-150"},
    {"website_name": "https://bajibet9.com",
     "name": "cf_clearance",
     "value": "b7nEcqDquFjPojJv0gHGm4hKYns3FwdNTo3YGlYiolI-1683898388-0-150"},
    {"website_name": "https://abdexch.com/#/login",
     "name": "cf_clearance",
     "value": ""},
    {"website_name": "https://aura25.bet/#/login",
     "name": "cf_clearance",
     "value": "4FQofPYfRcOaDErKc33RjqrMJLYqdaLrDTv5LDm7zRY-1683875838-0-150"},
    {"website_name": "https://badaabet.com/#/login",
     "name": "cf_clearance",
     "value": ""},
    {"website_name": "https://infinityexch.co/#/login",
     "name": "cf_clearance",
     "value": ""},
    {"website_name": "https://user365day.com/#/login",
     "name": "cf_clearance",
     "value": "bi9FFNeQnXDZQYg_mjfzlkADyeXcsJlNf2u9482a_kc-1683898479-0-150"},
    {"website_name": "https://only333.com/#/login",
     "name": "cf_clearance",
     "value": "RkkikOkqn2qWn5p5_sG4OMXNJwPLs2Np.vjVChGg1tg-1683898515-0-150"},
    {"website_name": "https://pk7exch.com/#/login",
     "name": "cf_clearance",
     "value": "n4N89b2pRrgTo53mnqqXA6t9CwlF02DVlGV1SksFHWs-1683898553-0-150"},
    {"website_name": "https://gamex24.com/#/login",
     "name": "cf_clearance",
     "value": "hr.biwKQL3llsQe0r0zg1M0nq.JqHVUJh_7w2KMPy5U-1683881227-0-150"},
    {"website_name": "https://aura26.com/#/login",
     "name": "cf_clearance",
     "value": "Qk2ItR9C0mxxRWerSoOpr3goAb8ntd4lsJXDa6igRDY-1683898618-0-150"},
    {"website_name": "https://xtra999.com/#/login",
     "name": "cf_clearance",
     "value": "cRLepfh.72CItG7kG6rkXKg9WO.sIHecxODCrssVSCw-1683898648-0-150"}
]


@pytest.fixture(params=websitelist)
def website_list(request):
    name = request.param
    name = name["website_name"]
    setattr(website_list, "__name__", name)
    return request.param


@pytest.fixture()
def web_name(website_list):
    return website_list


@pytest.fixture()
def setup():
    global driver
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    ###
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    ###
    chrome_options.add_argument("--no-incognito")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    capabilities = webdriver.DesiredCapabilities().CHROME.copy()
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options,
                              desired_capabilities=capabilities)

    # driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    # # driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# @pytest.fixture()
# def setup():
#     global driver
#     # filepath = get_project_root()
#     # serv_obj = Service(f'{filepath}/chromedriver.exe')
#     # driver = webdriver.Chrome(service=serv_obj)
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(10)
#     yield driver

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
    return str(newurl)


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
            # file_path = f"http://159.65.148.205:8000/{file_name}"
            file_path = f"{filepath}/{file_name}"
            if file_name:
                html = '<div> <img src="%s"' \
                       ' alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path
                extra.append(pytest_html.extras.html(html))
                extra.append(pytest_html.extras.url(getcurrenturl(), name=getcurrenturl()))
    report.extra = extra
    # driver.quit()


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
