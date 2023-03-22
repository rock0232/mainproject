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
    websitelist = ["https://abdexch.com/#/login", "https://aura25.bet/#/login"]

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

    # def test_common(self, setup, websitelist):
    #     driver = setup
    #     driver.maximize_window()
    #     cc = B2Bcommonclass(driver)
    #     driver.get(websitelist)
    #     time.sleep(5)
    #     cc.clicksignin()
    #     time.sleep(3)
    #     cc.setusername(self.username)
    #     cc.setpassword(self.password)
    #     cc.clicklogin()
    #
    #     time.sleep(15)
    #     alertmessage = ""
    #     cc.clickclose()
    #     time.sleep(2)
    #     totalmatches, inplay = cc.getinplaymatchcount()
    #     prewalletamount = cc.getwalletamount()
    #     preexposure = cc.getliability()
    #
    #     if cc.inplay:
    #         cc.clickinplay()
    #         time.sleep(2)
    #         totalinplaymatch = driver.find_elements(By.CSS_SELECTOR, cc.inplaylist_CSS)
    #         for i in range(0, len(totalinplaymatch)):
    #             driver.find_element(By.XPATH, cc.inplaytext_xpath).click()
    #             totalinplaymatch[i].click()
    #             for c in range(0, 4):
    #                 try:
    #                     cc.clickbackrate()
    #                     cc.setbetprice(self.betprice)
    #                     cc.clickplacebet()
    #                     alertmessage = cc.getalertmessage()
    #                     time.sleep(7)
    #                     if "success" in alertmessage or "0Unknown Error" in alertmessage or "Rate Exposure limit" in alertmessage:
    #                         break
    #                     else:
    #                         cc.clickbackrate()
    #                 except:
    #                     break
    #             if "success" in alertmessage or "0Unknown Error" in alertmessage:
    #                 break
    #             if i == len(totalinplaymatch) - 1:
    #                 cc.inplay = False
    #                 break
    #             # cc.clicklogo()
    #
    #     if not cc.inplay:
    #         cc.clicklogo()
    #         driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.PAGE_DOWN)
    #         countmanualodds = driver.find_elements(By.XPATH, cc.manualodds_xpath)
    #         driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.PAGE_UP)
    #         for q in range(0, len(countmanualodds)):
    #             for dj in range(0, q + 3):
    #                 driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
    #             manualodds = driver.find_elements(By.XPATH, cc.manualodds_xpath)
    #             try:
    #                 manualodds[q].click()
    #             except:
    #                 continue
    #             for sp in range(0, 4):
    #                 time.sleep(2)
    #                 driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
    #             try:
    #                 driver.find_element(By.XPATH, cc.wintossback_xpath).click()
    #                 driver.find_element(By.XPATH, cc.manualbetprice_xpath).clear()
    #                 driver.find_element(By.XPATH, cc.manualbetprice_xpath).send_keys(self.betprice)
    #                 cc.clickplacebet()
    #                 alertmessage = cc.getalertmessage()
    #                 if "success" in alertmessage:
    #                     break
    #                 else:
    #                     cc.clicklogo()
    #                     driver.find_element(By.XPATH, cc.wintossback_xpath).click()
    #             except:
    #                 cc.clicklogo()
    #             if "success" in alertmessage or "0Unknown Error" in alertmessage:
    #                 break
    #             elif q == len(countmanualodds) - 1:
    #                 self.logger.info("No Matches Are Availale To Place Bet %s", alertmessage)
    #                 assert False
    #
    #     postexposure = None
    #     exposure = None
    #     postwalletamount = None
    #     actpostwalletamount = None
    #
    #     if "success" in alertmessage:
    #         try:
    #             dbselection = cc.getselection()
    #             dbtypeofbet = cc.gettypeofbet()
    #             dbstake = cc.getstake()
    #             dbpl = cc.getpl()
    #             cc.clickuserprofile()
    #             cc.clickmybet()
    #             time.sleep(2)
    #             postexposure = cc.getliability()
    #             postwalletamount = prewalletamount - float(dbstake)
    #             exposure = float(dbstake) + preexposure
    #             actpostwalletamount = cc.getwalletamount()
    #
    #             if postexposure == exposure and postwalletamount == actpostwalletamount:
    #                 self.logger.info("Test Passed")
    #                 self.logger.info("Message After Click on Place Bet Button %s", alertmessage)
    #                 self.logger.info("Wallet Amount And Exposure are Updated After Place Bet")
    #             else:
    #                 try:
    #                     self.logger.error("Test Failed")
    #                     self.logger.info("Wallet balance and Exposure Balance is not Updated After Bet place")
    #                     self.logger.info("Message After Place Bet %s", alertmessage)
    #                     self.logger.info("User Login With %s", self.username)
    #                     self.logger.info("Wallet Amount Before Place Bet %s", prewalletamount)
    #                     self.logger.info("Wallet Amount After Place Bet %s", actpostwalletamount)
    #                     self.logger.info("Bet Price %s", self.betprice)
    #                     self.logger.info("Exposure Before Place Bet %s", preexposure)
    #                     self.logger.info("Exposure After Place Bet %s", postexposure)
    #                     self.logger.info("")
    #                     self.logger.info(
    #                         "******************** Data From Dashboard Bet list ********************")
    #                     self.logger.info("Bet Place Team Name is %s", dbselection)
    #                     self.logger.info("Bet Place On %s", dbtypeofbet)
    #                     self.logger.info("Bet Stake Amount is %s", dbstake)
    #                     self.logger.info("P/L on Bet Place is %s", dbpl)
    #                     time.sleep(0.5)
    #                     # driver.refresh()
    #                     time.sleep(5)
    #                     rpselection = cc.getreportselection()
    #                     rptypeofbet = cc.getreporttype()
    #                     rpstake = cc.getreportstake()
    #                     rppl = cc.getreportpl()
    #                     self.logger.info("")
    #                     self.logger.info("******************** Data From Open Bet Report ********************")
    #                     self.logger.info("Bet Place Team Name In Open Bet Report is %s", rpselection)
    #                     self.logger.info("Bet Place Type In Open Bet Report is %s", rptypeofbet)
    #                     self.logger.info("Bet Stake Amount In Open Bet Report is %s", rpstake)
    #                     self.logger.info("P/L On Bet Place In Open Bet Report is %s", rppl)
    #
    #                     assert rpselection == dbselection and rptypeofbet == dbtypeofbet and rpstake == dbstake and rppl == dbpl
    #                 except:
    #                     self.logger.info(" ")
    #                     self.logger.info("Data Not Display In Report or Report Is not Update")
    #             assert postexposure == exposure and postwalletamount == actpostwalletamount
    #         except:
    #             assert postexposure == exposure and postwalletamount == actpostwalletamount
    #     elif "0Unknown Error" in alertmessage:
    #         self.logger.info("Bet Not Place Error Message = %s", alertmessage)
    #         assert False
    #
    #     else:
    #         self.logger.info("Bet Not Place Message After PLace Bet %s", alertmessage)
    #         assert False
    #

    # @pytest.mark.roughfiletest
    # def test_aura25(self, setup):

    for w in range(len(websitelist)):
        # self.test_common(setup, websitelist=self.websitelist[w])

        def test_common(self, setup, websitelist):
            driver = setup
            driver.maximize_window()
            cc = B2Bcommonclass(driver)
            driver.get(websitelist[self.w])
            time.sleep(5)
            cc.clicksignin()
            time.sleep(3)
            cc.setusername(self.username)
            cc.setpassword(self.password)
            cc.clicklogin()

            time.sleep(15)
            alertmessage = ""
            cc.clickclose()
            time.sleep(2)
            totalmatches, inplay = cc.getinplaymatchcount()
            prewalletamount = cc.getwalletamount()
            preexposure = cc.getliability()

            if cc.inplay:
                cc.clickinplay()
                time.sleep(2)
                totalinplaymatch = driver.find_elements(By.CSS_SELECTOR, cc.inplaylist_CSS)
                for i in range(0, len(totalinplaymatch)):
                    driver.find_element(By.XPATH, cc.inplaytext_xpath).click()
                    totalinplaymatch[i].click()
                    for c in range(0, 4):
                        try:
                            cc.clickbackrate()
                            cc.setbetprice(self.betprice)
                            cc.clickplacebet()
                            alertmessage = cc.getalertmessage()
                            time.sleep(7)
                            if "success" in alertmessage or "0Unknown Error" in alertmessage or "Rate Exposure limit" in alertmessage:
                                break
                            else:
                                cc.clickbackrate()
                        except:
                            break
                    if "success" in alertmessage or "0Unknown Error" in alertmessage:
                        break
                    if i == len(totalinplaymatch) - 1:
                        cc.inplay = False
                        break
                    # cc.clicklogo()

            if not cc.inplay:
                cc.clicklogo()
                driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.PAGE_DOWN)
                countmanualodds = driver.find_elements(By.XPATH, cc.manualodds_xpath)
                driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.PAGE_UP)
                for q in range(0, len(countmanualodds)):
                    for dj in range(0, q + 3):
                        driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
                    manualodds = driver.find_elements(By.XPATH, cc.manualodds_xpath)
                    try:
                        manualodds[q].click()
                    except:
                        continue
                    for sp in range(0, 4):
                        time.sleep(2)
                        driver.find_element(By.TAG_NAME, "Body").send_keys(Keys.ARROW_DOWN)
                    try:
                        driver.find_element(By.XPATH, cc.wintossback_xpath).click()
                        driver.find_element(By.XPATH, cc.manualbetprice_xpath).clear()
                        driver.find_element(By.XPATH, cc.manualbetprice_xpath).send_keys(self.betprice)
                        cc.clickplacebet()
                        alertmessage = cc.getalertmessage()
                        if "success" in alertmessage:
                            break
                        else:
                            cc.clicklogo()
                            driver.find_element(By.XPATH, cc.wintossback_xpath).click()
                    except:
                        cc.clicklogo()
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
                    dbselection = cc.getselection()
                    dbtypeofbet = cc.gettypeofbet()
                    dbstake = cc.getstake()
                    dbpl = cc.getpl()
                    cc.clickuserprofile()
                    cc.clickmybet()
                    time.sleep(2)
                    postexposure = cc.getliability()
                    postwalletamount = prewalletamount - float(dbstake)
                    exposure = float(dbstake) + preexposure
                    actpostwalletamount = cc.getwalletamount()

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
                            self.logger.info(
                                "******************** Data From Dashboard Bet list ********************")
                            self.logger.info("Bet Place Team Name is %s", dbselection)
                            self.logger.info("Bet Place On %s", dbtypeofbet)
                            self.logger.info("Bet Stake Amount is %s", dbstake)
                            self.logger.info("P/L on Bet Place is %s", dbpl)
                            time.sleep(0.5)
                            # driver.refresh()
                            time.sleep(5)
                            rpselection = cc.getreportselection()
                            rptypeofbet = cc.getreporttype()
                            rpstake = cc.getreportstake()
                            rppl = cc.getreportpl()
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


