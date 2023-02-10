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

    @pytest.mark.b2bmarker
    def test_abdexch(self, abdlogin):
        currenturl = abdlogin
        if currenturl == "https://abdexch.com/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            eventname = self.cc.clickinplaymarket()
            self.logger.info("Event Name is %s", eventname)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            preliability = self.cc.getliability()
            self.logger.info("Exposure Before Bet Place is %s", preliability)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

            if "success" in alertmessage:
                try:
                    stackprice = self.cc.getstake()
                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)
                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred %s", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            self.driver.quit()

    @pytest.mark.b2bmarker
    @pytest.mark.debug
    def test_aura25(self, aura25login):
        currenturl = aura25login
        if currenturl == "https://aura25.bet/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            count = self.cc.getinplaymatchcount()
            if self.cc.inplay:
                relcount = int(count * 1.5)
                for i in range(0, relcount):
                    self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
                    try:
                        elememt = self.driver.find_element(By.XPATH, self.cc.inplay_xpath)
                        if elememt:
                            elememt.click()
                            break
                    except:
                        pass
            elif not self.cc.inplay:
                relcount = int(count * 1.5)
                for i in range(0, relcount):
                    self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
                    try:
                        manualodds = self.driver.find_element(By.XPATH, self.cc.manualodds_xpath)
                        if manualodds:
                            manualodds.click()
                            break
                    except:
                        pass
            prewalletamount = self.cc.getwalletamount()
            preliability = self.cc.getliability()

            if self.cc.inplay:
                self.cc.clickbackrate()
                self.cc.setbetprice(self.betprice)
            else:
                for i in range(0, 5):
                    self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
                self.driver.find_element(By.XPATH, self.cc.wintossback_xpath).clear()
                self.driver.find_element(By.XPATH, self.cc.manualbetprice_xpath).send_keys(self.betprice)
            # self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            # self.logger.info("Exposure Before Bet Place is %s", preliability)
            # time.sleep(2)

            # self.cc.clickbackrate()
            # self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)

            # self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            postexposure = None
            exposure = None
            postwalletamount = None
            actpostwalletamount = None

            if "success" in alertmessage:
                try:
                    self.logger.info("Message After Click on Place Bet Button %s", alertmessage)
                    stackprice = self.cc.getstake()
                    # self.logger.info("************* Data From Dashboard Bet list *************")
                    # self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    # self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    # self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    # self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    # self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    # self.logger.info("Click on Open Bet Button In User Profile Button")
                    # time.sleep(10)
                    # self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    # self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    # self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)
                # except Exception as e:
                #     self.logger.info("Exception Occurred %s", e)
                except:
                    pass
                assert postexposure == exposure and postwalletamount == actpostwalletamount
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
                assert False
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            assert False

    @pytest.mark.b2bmarker
    def test_badabet(self, badabetlogin):
        currenturl = badabetlogin
        if currenturl == "https://badaabet.com/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            eventname = self.cc.clickinplaymarket()
            self.logger.info("Event Name is %s", eventname)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            preliability = self.cc.getliability()
            self.logger.info("Exposure Before Bet Place is %s", preliability)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

            if "success" in alertmessage:
                try:
                    stackprice = self.cc.getstake()
                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)
                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred %s", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            self.driver.quit()

    @pytest.mark.b2bmarker
    def test_infinity(self, infinitylogin):
        currenturl = infinitylogin
        if currenturl == "https://infinityexch.co/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            eventname = self.cc.clickinplaymarket()
            self.logger.info("Event Name is %s", eventname)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            preliability = self.cc.getliability()
            self.logger.info("Exposure Before Bet Place is %s", preliability)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

            if "success" in alertmessage:
                try:
                    stackprice = self.cc.getstake()
                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)
                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred %s", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            self.driver.quit()

    @pytest.mark.b2bmarker
    def test_user365(self, user365login):
        currenturl = user365login
        if currenturl == "https://user365day.com/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            eventname = self.cc.clickinplaymarket()
            self.logger.info("Event Name is %s", eventname)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            preliability = self.cc.getliability()
            self.logger.info("Exposure Before Bet Place is %s", preliability)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

            if "success" in alertmessage:
                try:
                    stackprice = self.cc.getstake()
                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)
                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred %s", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            self.driver.quit()

    @pytest.mark.b2bmarker
    def test_only333(self, only333login):
        currenturl = only333login
        if currenturl == "https://only333.com/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            eventname = self.cc.clickinplaymarket()
            self.logger.info("Event Name is %s", eventname)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            preliability = self.cc.getliability()
            self.logger.info("Exposure Before Bet Place is %s", preliability)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

            if "success" in alertmessage:
                try:
                    stackprice = self.cc.getstake()
                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)
                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred %s", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            self.driver.quit()

    @pytest.mark.b2bmarker
    def test_pk7(self, pk7login):
        currenturl = pk7login
        if currenturl == "https://pk7exch.com/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            eventname = self.cc.clickinplaymarket()
            self.logger.info("Event Name is %s", eventname)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            preliability = self.cc.getliability()
            self.logger.info("Exposure Before Bet Place is %s", preliability)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

            if "success" in alertmessage:
                try:
                    stackprice = self.cc.getstake()
                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)
                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred %s", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            self.driver.quit()

    @pytest.mark.b2bmarker
    def test_gamex(self, gamexlogin):
        currenturl = gamexlogin
        if currenturl == "https://gamex24.com/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            eventname = self.cc.clickinplaymarket()
            self.logger.info("Event Name is %s", eventname)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            preliability = self.cc.getliability()
            self.logger.info("Exposure Before Bet Place is %s", preliability)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

            if "success" in alertmessage:
                try:
                    stackprice = self.cc.getstake()
                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)
                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred %s", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            self.driver.quit()

    @pytest.mark.b2bmarker
    def test_aura26(self, aura26login):
        currenturl = aura26login
        if currenturl == "https://aura26.com/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            eventname = self.cc.clickinplaymarket()
            self.logger.info("Event Name is %s", eventname)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            preliability = self.cc.getliability()
            self.logger.info("Exposure Before Bet Place is %s", preliability)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

            if "success" in alertmessage:
                try:
                    stackprice = self.cc.getstake()
                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)
                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred %s", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            self.driver.quit()

    @pytest.mark.b2bmarker
    def test_xtra999(self, xtra999login):
        currenturl = xtra999login
        if currenturl == "https://xtra999.com/#/home":
            self.cc = B2Bcommonclass(self.driver)
            self.cc.clickclose()
            time.sleep(2)
            eventname = self.cc.clickinplaymarket()
            self.logger.info("Event Name is %s", eventname)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance Before Place Bet is %s", prewalletamount)
            preliability = self.cc.getliability()
            self.logger.info("Exposure Before Bet Place is %s", preliability)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)

            if "success" in alertmessage:
                try:
                    stackprice = self.cc.getstake()
                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickmybet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)
                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    postexposure = self.cc.getliability()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = stackprice + preliability
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)
                    actpostwalletamount = self.cc.getwalletamount()
                    self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred %s", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
            self.driver.quit()
