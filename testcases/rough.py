import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

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
        time.sleep(10)
        currenturl = self.driver.current_url
        return currenturl

    def newfunction(self):
        self.cc = B2Bcommonclass(self.driver)
        self.cc.clickclose()
        time.sleep(2)
        totalmatches, inplay = self.cc.getinplaymatchcount()
        if self.cc.inplay:
            action = None
            for j in range(0, inplay):
                relcount = int(totalmatches / 4)
                for i in range(0, relcount):
                    try:
                        elememt = self.driver.find_element(By.XPATH, self.cc.inplay_xpath)
                        if elememt:
                            elememt.click()
                            time.sleep(4)
                    except:
                        pass
                    try:
                        marketstatus = self.driver.find_element(By.XPATH, self.cc.inactivemarket_xpath).is_displayed()
                        if marketstatus:
                            self.driver.back()
                    except:
                        action = "break"
                        break
                    self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
                    time.sleep(2)
                    self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_UP)
                    time.sleep(2)
                if action == "break":
                    break

        elif not self.cc.inplay:
            relcount = int(totalmatches / 4)
            for i in range(0, relcount):
                try:
                    manualodds = self.driver.find_element(By.XPATH, self.cc.manualodds_xpath)
                    if manualodds:
                        manualodds.click()
                        break
                except:
                    pass
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
                time.sleep(2)
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_UP)
                time.sleep(2)

        prewalletamount = self.cc.getwalletamount()
        preexposure = self.cc.getliability()
        time.sleep(5)
        for i in range(0,5):
            if self.cc.inplay:
                self.cc.clickbackrate()
                self.cc.setbetprice(self.betprice)
            else:
                self.driver.find_element(By.XPATH, self.cc.wintossback_xpath).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.cc.manualbetprice_xpath).clear()
                self.driver.find_element(By.XPATH, self.cc.manualbetprice_xpath).send_keys(self.betprice)
            self.cc.clickplacebet()
            alertmessage = self.cc.getalertmessage()
            time.sleep(5)
            print(alertmessage)
            if "success" in alertmessage:
                break
            else:
                if self.cc.inplay:
                    self.cc.clickbackrate()
                else:
                    self.driver.find_element(By.XPATH, self.cc.wintossback_xpath).click()

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
            betplace = True
            try:
                self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

                dbselection = self.cc.getselection()
                dbtypeofbet = self.cc.gettypeofbet()
                dbstake = self.cc.getstake()
                dbpl = self.cc.getpl()
                self.cc.clickuserprofile()
                self.cc.clickmybet()
                postexposure = self.cc.getliability()
                postwalletamount = prewalletamount - self.betprice
                exposure = dbstake + preexposure
                actpostwalletamount = self.cc.getwalletamount()
                rpselection = self.cc.getreportselection()
                rptypeofbet = self.cc.getreporttype()
                rpstake = self.cc.getreportstake()
                rppl = self.cc.getreportpl()

            except Exception as e:
                self.logger.info("exception %s", e)
            if postexposure == exposure and postwalletamount == actpostwalletamount:
                self.logger.info("Test Passed")
                self.logger.info("Wallet Amount And Exposure are Updated After Place Bet")
                assert postexposure == exposure and postwalletamount == actpostwalletamount
            else:
                self.logger.error("Test Failed")
                self.logger.info("User Login With %s", self.username)
                self.logger.info("is bet place = %s", betplace)
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
                self.logger.info("")
                self.logger.info("******************** Data From Open Bet Report ********************")
                self.logger.info("Bet Place Team Name In Open Bet Report is %s", rpselection)
                self.logger.info("Bet Place Type In Open Bet Report is %s", rptypeofbet)
                self.logger.info("Bet Stake Amount In Open Bet Report is %s", rpstake)
                self.logger.info("P/L On Bet Place In Open Bet Report is %s", rppl)
        else:
            self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            assert False
        self.driver.quit()

    @pytest.mark.b2bmarker
    @pytest.mark.debug
    def test_aura25(self, aura25login):
        currenturl = aura25login
        if currenturl == "https://aura25.bet/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")

    @pytest.mark.b2bmarker
    def test_abdexch(self, abdlogin):
        currenturl = abdlogin
        if currenturl == "https://abdexch.com/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")

    @pytest.mark.b2bmarker
    def test_badabet(self, badabetlogin):
        currenturl = badabetlogin
        if currenturl == "https://badaabet.com/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")

    @pytest.mark.b2bmarker
    def test_infinity(self, infinitylogin):
        currenturl = infinitylogin
        if currenturl == "https://infinityexch.co/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")

    @pytest.mark.b2bmarker
    def test_user365(self, user365login):
        currenturl = user365login
        if currenturl == "https://user365day.com/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")

    @pytest.mark.b2bmarker
    def test_only333(self, only333login):
        currenturl = only333login
        if currenturl == "https://only333.com/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")

    @pytest.mark.b2bmarker
    def test_pk7(self, pk7login):
        currenturl = pk7login
        if currenturl == "https://pk7exch.com/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")

    @pytest.mark.b2bmarker
    def test_gamex(self, gamexlogin):
        currenturl = gamexlogin
        if currenturl == "https://gamex24.com/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")

    @pytest.mark.b2bmarker
    def test_aura26(self, aura26login):
        currenturl = aura26login
        if currenturl == "https://aura26.com/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")

    @pytest.mark.b2bmarker
    def test_xtra999(self, xtra999login):
        currenturl = xtra999login
        if currenturl == "https://xtra999.com/#/home":
            self.newfunction()
        else:
            self.logger.info("user not login")
