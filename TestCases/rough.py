import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customlogger import Logger
from pageobjects.B2Bcommonclass import B2Bcommonclass

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

    def newfunction(self):
        alertmessage = ""
        self.cc = B2Bcommonclass(self.driver)
        self.cc.clickclose()
        time.sleep(2)
        totalmatches, inplay = self.cc.getinplaymatchcount()
        prewalletamount = self.cc.getwalletamount()
        preexposure = self.cc.getliability()

        if self.cc.inplay:
            self.cc.clickinplay()
            time.sleep(2)
            totalinplaymatch = self.driver.find_elements(By.CSS_SELECTOR, self.cc.inplaylist_CSS)
            for i in range(0, len(totalinplaymatch)):
                self.driver.find_element(By.XPATH, self.cc.inplaytext_xpath).click()
                totalinplaymatch[i].click()
                for c in range(0, 4):
                    try:
                        self.cc.clickbackrate()
                        self.cc.setbetprice(self.betprice)
                        self.cc.clickplacebet()
                        alertmessage = self.cc.getalertmessage()
                        time.sleep(7)
                        if "success" in alertmessage or "0Unknown Error" in alertmessage or "Rate Exposure limit" in alertmessage:
                            break
                        else:
                            self.cc.clickbackrate()
                    except:
                        break
                if "success" in alertmessage or "0Unknown Error" in alertmessage:
                    break
                if i == len(totalinplaymatch) - 1:
                    self.cc.inplay = False
                    break
                # self.cc.clicklogo()

        if not self.cc.inplay:
            self.cc.clicklogo()
            self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.PAGE_DOWN)
            countmanualodds = self.driver.find_elements(By.XPATH, self.cc.manualodds_xpath)
            self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.PAGE_UP)
            for q in range(0, len(countmanualodds)):
                for dj in range(0, q + 3):
                    self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
                manualodds = self.driver.find_elements(By.XPATH, self.cc.manualodds_xpath)
                try:
                    manualodds[q].click()
                except:
                    continue
                for sp in range(0, 4):
                    time.sleep(2)
                    self.driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
                try:
                    self.driver.find_element(By.XPATH, self.cc.wintossback_xpath).click()
                    self.driver.find_element(By.XPATH, self.cc.manualbetprice_xpath).clear()
                    self.driver.find_element(By.XPATH, self.cc.manualbetprice_xpath).send_keys(self.betprice)
                    self.cc.clickplacebet()
                    alertmessage = self.cc.getalertmessage()
                    if "success" in alertmessage:
                        break
                    else:
                        self.cc.clicklogo()
                        self.driver.find_element(By.XPATH, self.cc.wintossback_xpath).click()
                except:
                    self.cc.clicklogo()
                if "success" in alertmessage or "0Unknown Error" in alertmessage:
                    break
                elif q == len(countmanualodds) - 1:
                    self.logger.info("No Matches Are Availale To Place Bet %s", alertmessage)
                    assert False

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

    def test_aura25(self, aura25login):
        try:
            login = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()
