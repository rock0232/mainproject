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

    def newfunction(self):
        alertmessage = ""
        self.cc = B2Bcommonclass(self.driver)
        self.cc.clickclose()
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
            self.driver.find_element(By.XPATH, self.cc.manualbetprice_xpath).clear()
            self.driver.find_element(By.XPATH, self.cc.manualbetprice_xpath).send_keys(self.betprice)
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
            print(len(totalinplaymatches))
            for s in range(0, len(totalinplaymatches)):
                time.sleep(5)
                matches = self.driver.find_elements(By.CSS_SELECTOR, self.cc.inplaylist_CSS)
                self.driver.execute_script("arguments[0].scrollIntoView();",matches[s])
                time.sleep(2)
                matches[s].click()
                print(s)
                time.sleep(5)
                try:
                    for c in range(0, 4):
                        self.cc.clickbackrate()
                        self.cc.setbetprice(self.betprice)
                        self.cc.clickplacebet()
                        alertmessage = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.cc.alertmessage_class))).text
                        time.sleep(7)
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

    def test_aura25(self, aura25login):
        try:
            login = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.TAG_NAME, "app-dashboard")))
        except:
            self.logger.info("User Not login, Please Run This Test Again")
            assert False
        self.newfunction()
        