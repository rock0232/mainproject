import time
import pytest
from utilities.customlogger import Logger
from pageobjects.B2Ccommonclass import commonclass, hattrick, run567, empire, thalaiva

class Test_commonlogin:
    logger = Logger.logen()
    uat = "https://uat.cloudd.live/login"
    hattrick = "https://hattrick.games/login"
    empire3rd = "https://3rdempire.in/login"
    run567url = "https://run567.com/login"
    thalaiva365 = "https://thalaiva365.com/login"
    # username = "android"
    # password = "Android@123"
    username = "rocktest"
    password = "Rock@1234"
    hattrickusername = "sp25"
    hattrickpassword = "Test@1234"
    betprice = 100

    @pytest.fixture(scope="function", autouse=False)
    def hattricklogin(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.lp = commonclass(self.driver)
        self.driver.get(self.hattrick)
        time.sleep(5)
        self.lp.clicksignin()
        time.sleep(3)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        time.sleep(15)
        currenturl = self.driver.current_url
        return currenturl

    @pytest.fixture(scope="function", autouse=False)
    def run567login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.lp = commonclass(self.driver)
        self.driver.get(self.run567url)
        time.sleep(5)
        self.lp.clicksignin()
        time.sleep(3)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        time.sleep(15)
        currenturl = self.driver.current_url
        return currenturl

    @pytest.fixture(scope="function", autouse=False)
    def empirelogin(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.lp = commonclass(self.driver)
        self.driver.get(self.empire3rd)
        time.sleep(5)
        self.lp.clicksignin()
        time.sleep(3)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        time.sleep(5)
        self.lp.clicklogin()
        time.sleep(15)
        currenturl = self.driver.current_url
        return currenturl

    @pytest.fixture(scope='function', autouse=False)
    def thalaivalogin(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.lp = commonclass(self.driver)
        self.driver.get(self.thalaiva365)
        time.sleep(5)
        self.lp.clicksignin()
        time.sleep(3)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        time.sleep(5)
        self.lp.clicklogin()
        time.sleep(15)
        currenturl = self.driver.current_url
        return currenturl

    @pytest.mark.debugmarker1
    def test_hattrick(self, hattricklogin):
        currenturl = hattricklogin
        if currenturl == "https://hattrick.games/home":
            self.logger.info("User Login With %s", self.username)
            self.driver.get("https://hattrick.games/sport/Upcoming")
            time.sleep(15)
            self.ht = hattrick(self.driver)
            self.cc = commonclass(self.driver)
            self.cc.scrollmarket()
            time.sleep(5)
            self.cc.scrollmarket()
            self.logger.info("Event Name is %s", self.cc.eventname())
            self.cc.clickmarket()
            time.sleep(5)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("wallet amount Before Place Bet is %s", prewalletamount)
            time.sleep(4)
            self.cc.hoveroverwallet()
            totalexposure = self.cc.getexposure()
            self.logger.info("Exposure Before Bet Place is %s", totalexposure)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            self.cc.scrollmarketdata()
            time.sleep(2)
            self.cc.setbetprice(self.betprice)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)
            actpostwalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)
            if "success" in alertmessage:
                try:

                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s",self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickopenbet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)

                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    self.cc.hoveroverwallet()
                    postexposure = self.cc.getexposure()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = self.betprice + totalexposure
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred",e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")

    @pytest.mark.debugmarker
    def test_run567(self, run567login):
        currenturl = run567login
        if currenturl == "https://run567.com/home":
            self.logger.info("User Login With %s", self.username)
            self.run = run567(self.driver)
            self.cc = commonclass(self.driver)
            self.cc.clickcricket()
            self.cc.scrollmarket()
            time.sleep(5)
            self.cc.scrollmarket()
            self.logger.info("Event Name is %s", self.cc.eventname())
            self.cc.clickmarket()
            time.sleep(5)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("wallet amount Before Place Bet is %s", prewalletamount)
            time.sleep(4)
            self.cc.hoveroverwallet()
            totalexposure = self.cc.getexposure()
            self.logger.info("Exposure Before Bet Place is %s", totalexposure)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            self.cc.scrollmarketdata()
            time.sleep(2)
            self.cc.setbetprice(2)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)
            actpostwalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)
            if "success" in alertmessage:
                try:

                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickopenbet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)

                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    self.cc.hoveroverwallet()
                    postexposure = self.cc.getexposure()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = self.betprice + totalexposure
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")

    @pytest.mark.debugmarker
    def test_empire3rd(self, empirelogin):
        currenturl = empirelogin
        if currenturl == "https://3rdempire.in/home":
            self.logger.info("User Login With %s", self.username)
            self.emp = empire(self.driver)
            self.cc = commonclass(self.driver)
            self.cc.clickcricket()
            self.cc.scrollmarket()
            time.sleep(5)
            self.cc.scrollmarket()
            self.logger.info("Event Name is %s", self.cc.eventname())
            self.cc.clickmarket()
            time.sleep(5)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("wallet amount Before Place Bet is %s", prewalletamount)
            time.sleep(4)
            self.cc.hoveroverwallet()
            totalexposure = self.cc.getexposure()
            self.logger.info("Exposure Before Bet Place is %s", totalexposure)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            self.cc.scrollmarketdata()
            time.sleep(2)
            self.cc.setbetprice(2)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)
            actpostwalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)
            if "success" in alertmessage:
                try:

                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickopenbet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)

                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    self.cc.hoveroverwallet()
                    postexposure = self.cc.getexposure()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = self.betprice + totalexposure
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")

    @pytest.mark.debugmarker2
    def test_thalaiva(self, thalaivalogin):
        currenturl = thalaivalogin
        if currenturl == "https://thalaiva365.com/home":
            self.logger.info("User Login With %s", self.username)
            self.th = thalaiva(self.driver)
            self.cc = commonclass(self.driver)
            self.cc.clickcricket()
            self.cc.scrollmarket()
            time.sleep(5)
            self.cc.scrollmarket()
            self.logger.info("Event Name is %s", self.cc.eventname())
            self.cc.clickmarket()
            time.sleep(5)
            prewalletamount = self.cc.getwalletamount()
            self.logger.info("wallet amount Before Place Bet is %s", prewalletamount)
            time.sleep(4)
            self.cc.hoveroverwallet()
            totalexposure = self.cc.getexposure()
            self.logger.info("Exposure Before Bet Place is %s", totalexposure)
            time.sleep(2)
            self.cc.clickbackrate()
            self.logger.info("Click on Back Rate, Back Team Name is %s", self.cc.getmainteamname())
            self.cc.scrollmarketdata()
            time.sleep(2)
            self.cc.setbetprice(2)
            self.logger.info("Set Bet Price, Bet Price = %s", self.betprice)
            time.sleep(2)
            self.cc.clickplacebet()
            self.logger.info("Click On Place Bet Button")
            alertmessage = self.cc.getalertmessage()
            self.logger.info("Message After Click on Place Bet Button %s", alertmessage)
            actpostwalletamount = self.cc.getwalletamount()
            self.logger.info("Wallet Balance After Place Bet is %s", actpostwalletamount)
            if "success" in alertmessage:
                try:

                    self.logger.info("************* Data From Dashboard Bet list *************")
                    self.logger.info("Bet Place Team Name is %s", self.cc.getselection())
                    self.logger.info("Bet Place On %s", self.cc.gettypeofbet())
                    self.logger.info("Bet Stake Amount is %s", self.cc.getstake())
                    self.logger.info("P/L on Bet Place is %s", self.cc.getpl())

                    self.cc.clickuserprofile()
                    self.logger.info("Click on User Profile Button")
                    self.cc.clickopenbet()
                    self.logger.info("Click on Open Bet Button In User Profile Button")
                    time.sleep(10)

                    self.logger.info("************* Data From Open Bet Report *************")
                    self.logger.info("Bet Place Team Name In Open Bet Report is %s", self.cc.getreportselection())
                    self.logger.info("Bet Place Type In Open Bet Report is %s", self.cc.getreporttype())
                    self.logger.info("Bet Stake Amount In Open Bet Report Is is %s", self.cc.getreportstake())
                    self.logger.info("P/L On Bet Place In Open Bet Report is %s", self.cc.getreportpl())

                    self.cc.hoveroverwallet()
                    postexposure = self.cc.getexposure()
                    postwalletamount = prewalletamount - self.betprice
                    exposure = self.betprice + totalexposure
                    self.logger.info("Exposure After Place Bet Is %s", postexposure)

                    assert postexposure == exposure and postwalletamount == actpostwalletamount

                except Exception as e:
                    self.logger.info("Exception Occurred", e)
            else:
                self.logger.info("Bet Not Place Message After Place %s", alertmessage)
            self.driver.quit()
        else:
            self.logger.warning("User Not Login Please Try Again")
