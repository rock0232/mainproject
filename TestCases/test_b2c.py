import time
import pytest
from selenium.webdriver import Keys
from utilities.customlogger import Logger
from pageobjects.B2Ccommonclass import commonclass, hattrick, run567, empire, thalaiva
from selenium.webdriver.common.by import By


class Test_commonlogin:
    logger = Logger.logen()
    uat = "https://uat.cloudd.live/login"
    hattrick = "https://hattrick.games/login"
    empire3rd = "https://3rdempire.in/login"
    run567url = "https://run567.co/login"
    thalaiva365 = "https://thalaiva365.com/login"
    username = "android"
    password = "Android@123"
    # username = "rocktest"
    # password = "Rock@1234"
    betprice = 101

    @pytest.fixture(scope="function", autouse=False)
    def hattricklogin(self, setup):
        self.driver = setup
        self.driver.set_window_size(1366, 768, windowHandle="current")
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

    def commonfunction(self):
        self.cc = commonclass(self.driver)
        self.run = run567(self.driver)
        alertmessage = ""
        prewalletamount = self.cc.getwalletamount()
        self.cc.hoveroverwallet()
        time.sleep(1.5)
        preexposure = self.cc.getexposure()
        self.cc.clickcricket()
        self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.PAGE_DOWN)
        countmanualodds = self.driver.find_elements(By.XPATH, self.cc.manualodds_xpath)
        for i in range(0, len(countmanualodds)):
            for sp in range(0, i + 3):
                self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
            time.sleep(1.5)
            manualodds = self.driver.find_elements(By.XPATH, self.cc.manualodds_xpath)
            try:
                manualodds[i].click()
            except:
                continue
            try:
                time.sleep(2)
                self.cc.clickwintossmarket()
                self.run.clickwintossback()
                self.cc.setbetprice(self.betprice)
                self.cc.clickplacebet()

                alertmessage = self.cc.getalertmessage()

                if "success" in alertmessage:
                    break
                else:
                    self.cc.clickbrandlogo()
                    time.sleep(3)
                    self.cc.clickcricket()
                    self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.PAGE_DOWN)
            except:
                self.cc.clickbrandlogo()
                time.sleep(3)
                self.cc.clickcricket()

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
                self.cc.clickopenbet()
                time.sleep(2)
                self.cc.hoveroverwallet()
                postexposure = self.cc.getexposure()
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
        self.driver.close()

    @pytest.mark.runall
    @pytest.mark.b2cmarker
    @pytest.mark.run567
    def test_run567(self, run567login):
        currenturl = run567login
        if "home" in currenturl:
            self.commonfunction()
        else:
            self.logger.info("User Not login, Please Run This Test Again")
            self.driver.quit()
            assert False

    @pytest.mark.runall
    @pytest.mark.b2cmarker
    @pytest.mark.hattrick
    def test_hattrick(self, hattricklogin):
        self.driver.get("https://hattrick.games/sport/Upcoming")
        time.sleep(10)
        alertmessage = ""
        self.cc = commonclass(self.driver)
        self.ht = hattrick(self.driver)
        self.cc.hoveroverwallet()
        time.sleep(2)
        preexposure = self.cc.getexposure()
        prewalletamount = self.cc.getwalletamount()
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        manualodds = self.driver.find_elements(By.XPATH, self.cc.manualodds_xpath)
        for s in range(0, len(manualodds)):
            for i in range(0, int(s + 3)):
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
            wintoss = self.driver.find_elements(By.XPATH, self.cc.manualodds_xpath)
            try:
                wintoss[s].click()
                time.sleep(3)
                self.cc.clickwintossmarket()
                time.sleep(3)
                for i in range(0, 3):
                    self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
                self.cc.clickwintossback()
                time.sleep(3)
                self.cc.setbetprice(self.betprice)
                self.cc.clickplacebet()
                alertmessage = self.cc.getalertmessage()
                time.sleep(3)
                if "success" in alertmessage:
                    assert True
                    break
                else:
                    self.ht.clickupcoming()
                    self.driver.find_element(By.XPATH, self.cc.allupcoming_xpath).click()
                    self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.PAGE_DOWN)
            except:
                pass

        postexposure = None
        exposure = None
        postwalletamount = None
        actpostwalletamount = None

        if "success" in alertmessage:
            try:
                dbselection = self.cc.getselection()
                dbtypeofbet = self.cc.gettypeofbet()
                dbstake = self.cc.getstake()
                dbpl = self.cc.getpl()
                self.cc.clickuserprofile()
                self.cc.clickopenbet()
                time.sleep(2)
                self.cc.hoveroverwallet()
                postexposure = self.cc.getexposure()
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
        else:
            self.logger.info("Bet Not Place Message After PLace Bet %s", alertmessage)
            assert False
        self.driver.close()

    @pytest.mark.runall
    @pytest.mark.b2cmarker
    @pytest.mark.empire
    def test_empire(self, run567login):
        currenturl = run567login
        if "home" in currenturl:
            self.commonfunction()
        else:
            self.logger.info("User Not login, Please Run This Test Again")
            self.driver.quit()
            assert False

    @pytest.mark.runall
    @pytest.mark.b2cmarker
    @pytest.mark.thalaiva
    def test_thalaiva(self, thalaivalogin):
        currenturl = thalaivalogin
        if "home" in currenturl:
            self.commonfunction()
        else:
            self.logger.info("User Not login, Please Run This Test Again")
            self.driver.quit()
            assert False
