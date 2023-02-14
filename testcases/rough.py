import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customlogger import Logger
from pageobjects.B2Bcommonclass import B2Bcommonclass


# C:\Users\KEY\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages

class Test_B2Bcommonclass:
    logger = Logger.logen()

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
    betprice = 202

    @pytest.fixture(scope="function", autouse=False)
    def aura25login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
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
        self.driver.maximize_window()
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
        self.driver.maximize_window()
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
        self.driver.maximize_window()
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
        self.driver.maximize_window()
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
        self.driver.maximize_window()
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
        self.driver.maximize_window()
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
        self.driver.maximize_window()
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
        self.driver.maximize_window()
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
        self.driver.maximize_window()
        self.cc = B2Bcommonclass(self.driver)
        self.driver.get(self.xtra999)
        time.sleep(5)
        self.cc.clicksignin()
        time.sleep(3)
        self.cc.setusername(self.username)
        self.cc.setpassword(self.password)
        self.cc.clicklogin()

    def newfunction(self):
        self.cc = B2Bcommonclass(self.driver)
        self.cc.clickclose()
        alertmessage = ""
        time.sleep(2)
        totalmatches, inplay = self.cc.getinplaymatchcount()
        prewalletamount = self.cc.getwalletamount()
        preexposure = self.cc.getliability()

        if self.cc.inplay:
            for i in range(0, inplay):
                for dp in range(0,2+i):
                    self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
                try:
                    inplaymatch = self.driver.find_elements(By.XPATH, self.cc.inplay_xpath)
                    if inplaymatch:
                        inplaymatch[i].click()  # 0
                        time.sleep(4)
                        try:
                            marketstatus = self.driver.find_element(By.XPATH, self.cc.inactivemarket_xpath)
                            self.driver.back()
                        except:
                            for c in range(0, 5):
                                try:
                                    self.cc.clickbackrate()
                                    self.cc.setbetprice(self.betprice)
                                    self.cc.clickplacebet()
                                except:
                                    break
                                alertmessage = self.cc.getalertmessage()
                                time.sleep(5)
                                if "success" in alertmessage or "0Unknown Error" in alertmessage or "advances Exposure limits" in alertmessage:
                                    break
                                else:
                                    try:
                                        if self.cc.inplay:
                                            self.cc.clickbackrate()
                                        else:
                                            self.driver.find_element(By.XPATH, self.cc.wintossback_xpath).click()
                                    except:
                                        pass
                except:
                    pass
                if "success" in alertmessage or "0Unknown Error" in alertmessage:
                    break
                elif i == inplay-1 and "success" not in alertmessage:
                    self.cc.inplay = False
                    break
                self.cc.clicklogo()
                time.sleep(2)
                for s in range(0, 3):
                    self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)

        if not self.cc.inplay:
            self.cc.clicklogo()
            for q in range(0, 7):
                for dj in range(0, q+4):
                    self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
                try:
                    manualodds = self.driver.find_elements(By.XPATH, self.cc.manualodds_xpath)
                    if manualodds:
                        manualodds[q].click()
                except:
                    continue
                time.sleep(5)
                for sp in range(0, 4):
                    time.sleep(2)
                    if sp < 1:
                        self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
                        self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
                        self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
                    try:
                        self.driver.find_element(By.XPATH, self.cc.wintossback_xpath).click()
                        self.driver.find_element(By.XPATH, self.cc.manualbetprice_xpath).clear()
                        self.driver.find_element(By.XPATH, self.cc.manualbetprice_xpath).send_keys(self.betprice)
                        self.cc.clickplacebet()
                        alertmessage = self.cc.getalertmessage()
                        time.sleep(5)
                        if "success" in alertmessage or "0Unknown Error" in alertmessage or "advances Exposure limits" in alertmessage:
                            break
                        else:
                            if self.cc.inplay:
                                self.cc.clickbackrate()
                            else:
                                self.driver.find_element(By.XPATH, self.cc.wintossback_xpath).click()
                    except:
                        self.cc.clicklogo()
                        break
                if "success" in alertmessage or "0Unknown Error" in alertmessage:
                    break
                else:
                    if q == 6:
                        self.logger.info("No Matches Are Availale To Place Bet %s", alertmessage)
                        assert False

        postexposure = None
        exposure = None
        postwalletamount = None
        actpostwalletamount = None
        dbselection = None
        dbtypeofbet = None
        dbstake = None
        dbpl = None
        rpselection = None
        rptypeofbet = None
        rpstake = None
        rppl = None
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
                        self.driver.refresh()
                        time.sleep(6)
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

        else:
            self.logger.info("Bet Not Place Message After PLace Bet %s", alertmessage)
            assert False

    @pytest.mark.b2bmarker
    @pytest.mark.debug
    def test_aura25(self, aura25login):
        try:
            login = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()

    @pytest.mark.b2bmarker
    def test_abdexch(self, abdlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()

    @pytest.mark.b2bmarker
    def test_badabet(self, badabetlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()

    @pytest.mark.b2bmarker
    def test_infinity(self, infinitylogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()

    @pytest.mark.b2bmarker
    def test_user365(self, user365login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()

    @pytest.mark.b2bmarker
    def test_only333(self, only333login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()

    @pytest.mark.b2bmarker
    def test_pk7(self, pk7login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()

    @pytest.mark.b2bmarker
    def test_gamex(self, gamexlogin):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()

    @pytest.mark.b2bmarker
    def test_aura26(self, aura26login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()

    @pytest.mark.b2bmarker
    def test_xtra999(self, xtra999login):
        try:
            login = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("user not login")
            assert False
        self.newfunction()
