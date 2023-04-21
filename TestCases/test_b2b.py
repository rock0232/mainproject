import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customlogger import Logger
from TestCases.conftest import setup
from pageobjects.B2Bcommonclass import B2Bcommonclass


# C:\Users\KEY\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages

class Test_B2Bcommonclass:
    logger = Logger.logen()

    aura24 = "https://aura24.bet"
    park = "https://park.bet"
    greenexch = "https://greenexch.com"
    best365 = "https://best365.in"
    parkinplay = "https://parkinplay.net"
    butterflyexch = "https://butterflyexch.net"
    probook9 = "https://probook9.net"
    elevenwonder = "https://11wonder.net"
    winexch = "https://winexch.net"
    runexch = "https://runexch.net"
    cricbuz = "https://cricbuz.net"
    orange11 = "https://orange11.net"
    khelo365 = "https://khelo365.biz"
    bright99 = "https://bright99.biz"
    powerbets = "https://powerbets.biz"
    nineskyexch = "https://9skyexch.com"
    spice11 = "https://spice11.in"
    gold9 = "https://gold9.in"
    fancybook = "https://fancybook.live"
    skyexch1 = "https://skyexch1.net"
    # probet9 = "https://probet9.net"
    Sunexchange = "https://Sunexchange.in"
    sevenxbet = "https://7xbet.bet"
    saiexch24 = "https://saiexch24.com"
    lords99 = "https://lords99.com"
    bengal22 = "https://bengal22.bet"
    all365day = "https://all365day.com"
    Spworld365 = "https://Spworld365.com"
    euro11 = "https://euro11.net"
    royalbet444 = "https://royalbet444.vip"
    playwin247 = "https://playwin247.bet"
    jk3434 = "https://jk3434.bet"
    bajibet9 = "https://bajibet9.com"
    abdexch = "https://abdexch.com/#/login"
    aura25 = "https://aura25.bet/#/login"
    badabet = "https://badaabet.com/#/login"
    infinity = "https://infinityexch.co/#/login"
    user365 = "https://user365day.com/#/login"
    only333 = "https://only333.com/#/login"
    pk7 = "https://pk7exch.com/#/login"
    gamex = "https://gamex24.com/#/login"
    aura26 = "https://aura26.com/#/login"
    xtra999 = "https://xtra999.com/#/login"
    username = "rocktest"
    password = "Rock@1234"
    newusername = "kt11"
    newpassword = "First@666"
    betprice = 202

    @pytest.fixture(scope="function", autouse=False)
    def bajibet9login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.bajibet9)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()


    @pytest.fixture(scope="function", autouse=False)
    def jk3434login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.jk3434)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def playwin247login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.playwin247)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def royalbet444login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.royalbet444)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def euro11login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.euro11)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def Spworld365login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.Spworld365)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def all365daylogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.all365day)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def bengal22login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.bengal22)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def lords99login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.lords99)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def saiexch24login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.saiexch24)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def sevenxbetlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.sevenxbet)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def Sunexchangelogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.Sunexchange)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    # @pytest.fixture(scope="function", autouse=False)
    # def probet9login(self, setup):
    #     self.driver = setup
    #     self.driver.set_window_size(1366,768)
    #     self.cc = B2Bcommonclass(self.driver)
    #     self.driver.get(self.probet9)
    #     time.sleep(5)
    #     self.cc.clicksignin()
    #     time.sleep(3)
    #     self.cc.setusername(self.newusername)
    #     self.cc.setpassword(self.newpassword)
    #     self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def skyexch1login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.skyexch1)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def fancybooklogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.fancybook)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def gold9login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.gold9)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def spice11login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.spice11)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def nineskyexchlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.nineskyexch)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def powerbetslogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.powerbets)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def bright99login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.bright99)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def khelo365login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.khelo365)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def orange11login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.orange11)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def cricbuzlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.cricbuz)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def runexchlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.runexch)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def winexchlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.winexch)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def elevenwonderlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.elevenwonder)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def probook9login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.butterflyexch)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def butterflyexchlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.butterflyexch)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def parkinplaylogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.parkinplay)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def best365login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.best365)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def greenexchlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.greenexch)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def parklogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.park)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def aura24login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.aura24)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.newusername)
        self.cc.setpassword(self.newpassword)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def aura25login(self,setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.aura25)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def abdlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.abdexch)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def badabetlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.badabet)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def infinitylogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.infinity)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def user365login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.user365)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def only333login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.only333)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def pk7login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.pk7)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def gamexlogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.gamex)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def aura26login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.aura26)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    @pytest.fixture(scope="function", autouse=False)
    def xtra999login(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366,768)
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.xtra999)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    def newfunction(self):
        alertmessage = ""
        self.cc = B2Bcommonclass(self.driver)
        self.cc.clickclose()
        time.sleep(2)
        prewalletamount = self.cc.getwalletamount()
        preexposure = self.cc.getliability()
        element = self.driver.find_elements(By.XPATH, self.cc.manualodds_xpath)
        for sc in range(0,len(element)):
            element1 = self.driver.find_elements(By.XPATH, self.cc.manualodds_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", element1[sc])
            time.sleep(2)
            element1[sc].click()
            time.sleep(5)
            backelement = self.driver.find_element(By.XPATH, self.cc.wintossback_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", backelement)
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.cc.wintossback_xpath).click()
            self.driver.find_element(By.CSS_SELECTOR, self.cc.manualbetprice_css).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.cc.manualbetprice_css).send_keys(self.betprice)
            self.cc.clickplacebet()
            alertmessage = self.cc.getalertmessage()
            if "success" in alertmessage:
                self.cc.inplay = False
                break
            else:
                self.cc.clicklogo()

        if self.cc.inplay:
            self.cc.clickinplay()
            totalinplaymatches = self.driver.find_elements(By.CSS_SELECTOR, self.cc.inplaylist_CSS)
            for s in range(0, len(totalinplaymatches)):
                time.sleep(5)
                matches = self.driver.find_elements(By.CSS_SELECTOR, self.cc.inplaylist_CSS)
                self.driver.execute_script("arguments[0].scrollIntoView();",matches[s])
                time.sleep(2)
                matches[s].click()
                time.sleep(5)
                try:
                    for c in range(0, 4):
                        self.cc.clickbackrate()
                        self.cc.setbetprice(self.betprice)
                        self.cc.clickplacebet()
                        alertmessage = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.cc.alertmessage_class))).text
                        # time.sleep(7)
                        if "success" in alertmessage or "0Unknown Error" in alertmessage or "Rate Exposure limit" in alertmessage:
                            break
                        else:
                            self.cc.clickbackrate()
                except:
                    self.cc.clicklogo()
                if "success" in alertmessage:
                    assert "success" in alertmessage
                    break
            else:
                self.logger.info("No Matches Are Availale To Place Bet %s", alertmessage)

        postexposure = None
        exposure = None
        postwalletamount = None
        actpostwalletamount = None
        dbselection = None
        dbtypeofbet = None
        dbstake = None
        dbpl = None

        if "success" in alertmessage:
            try:
                dbselection = self.cc.getselection()
                dbtypeofbet = self.cc.gettypeofbet()
                dbstake = self.cc.getstake()
                dbpl = self.cc.getpl()
                self.cc.clickuserprofile()
                self.cc.clickmybet()
                time.sleep(2)
                postexposure = self.cc.getliability()
                postwalletamount = prewalletamount - float(dbstake)
                exposure = float(dbstake) + preexposure
                actpostwalletamount = self.cc.getwalletamount()

                if postexposure == exposure and postwalletamount == actpostwalletamount:
                    self.logger.info("Test Passed")
                    self.logger.info("Message After Click on Place Bet Button %s", alertmessage)
                    self.logger.info("Wallet Amount And Exposure are Updated After Place Bet")
                else:
                    try:
                        self.logger.error("Test Failed")
                        self.logger.info("Wallet balance and Exposure Balance is not Updated After Bet place")
                        self.logger.info("Message After Place Bet %s", alertmessage)
                        self.logger.info("User Login With %s", self.username)
                        self.logger.info("Wallet Amount Before Place Bet %s", prewalletamount)
                        self.logger.info("Wallet Amount After Place Bet %s", actpostwalletamount)
                        self.logger.info("Bet Price %s", self.betprice)
                        self.logger.info("Exposure Before Place Bet %s", preexposure)
                        self.logger.info("Exposure After Place Bet %s", postexposure)
                        self.logger.info("")
                        self.logger.info("******************** Data From Dashboard Bet list ********************")
                        self.logger.info("Bet Place Team Name is %s", dbselection)
                        self.logger.info("Bet Place On %s", dbtypeofbet)
                        self.logger.info("Bet Stake Amount is %s", dbstake)
                        self.logger.info("P/L on Bet Place is %s", dbpl)
                        time.sleep(0.5)
                        # self.driver.refresh()
                        time.sleep(5)
                        rpselection = self.cc.getreportselection()
                        rptypeofbet = self.cc.getreporttype()
                        rpstake = self.cc.getreportstake()
                        rppl = self.cc.getreportpl()
                        self.logger.info("")
                        self.logger.info("******************** Data From Open Bet Report ********************")
                        self.logger.info("Bet Place Team Name In Open Bet Report is %s", rpselection)
                        self.logger.info("Bet Place Type In Open Bet Report is %s", rptypeofbet)
                        self.logger.info("Bet Stake Amount In Open Bet Report is %s", rpstake)
                        self.logger.info("P/L On Bet Place In Open Bet Report is %s", rppl)

                        assert rpselection == dbselection and rptypeofbet == dbtypeofbet and rpstake == dbstake and rppl == dbpl
                    except:
                        self.logger.info(" ")
                        self.logger.info("Data Not Display In Report or Report Is not Update")
                assert postexposure == exposure and postwalletamount == actpostwalletamount
            except:
                assert postexposure == exposure and postwalletamount == actpostwalletamount
        elif "0Unknown Error" in alertmessage:
            self.logger.info("Bet Not Place Error Message = %s", alertmessage)
            assert False

        else:
            self.logger.info("Bet Not Place Message After PLace Bet %s", alertmessage)
            assert False
        self.driver.close()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.aura25
    def test_aura25(self, aura25login):
        try:
            login = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.abdexch
    def test_abdexch(self, abdlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.badabet
    def test_badabet(self, badabetlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.infinity
    def test_infinity(self, infinitylogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.user365
    def test_user365(self, user365login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.only333
    def test_only333(self, only333login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.pk7
    def test_pk7(self, pk7login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.gamex
    def test_gamex(self, gamexlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.aura26
    def test_aura26(self, aura26login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    @pytest.mark.xtra999
    def test_xtra999(self, xtra999login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_aura24(self, aura24login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_park(self, parklogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_greenexch(self, greenexchlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_best365(self, best365login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_parkinplay(self, parkinplaylogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_butterflyexch(self, butterflyexchlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_probook9(self, probook9login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_elevenwonder(self, elevenwonderlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_winexch(self, winexchlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_runexch(self, runexchlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_cricbuz(self, cricbuzlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_orange11(self, orange11login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_khelo365(self, khelo365login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_bright99(self, bright99login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_powerbets(self, powerbetslogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_nineskyexch(self, nineskyexchlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_spice11(self, spice11login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_gold9login(self, gold9login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_fancybook(self, fancybooklogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_skyexch1(self, skyexch1login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()
    #
    # @pytest.mark.runall
    # @pytest.mark.b2bmarker
    # def test_probet9login(self, probet9login):
    #     try:
    #         login = WebDriverWait(self.driver, 15).until(
    #             EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
    #     except:
    #         self.logger.info("User Not login, Please Run This Test Again")
    #         assert False
    #     self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_Sunexchange(self, Sunexchangelogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_sevenxbet(self, sevenxbetlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()


    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_saiexch24(self, saiexch24login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_lords99(self, lords99login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_bengal22(self, bengal22login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_all365day(self, all365daylogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_Spworld365(self, Spworld365login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_euro11(self, euro11login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_royalbet444(self, royalbet444login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_playwin247(self, playwin247login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_jk3434(self, jk3434login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()

    @pytest.mark.runall
    @pytest.mark.b2bmarker
    def test_bajibet9(self, bajibet9login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()



