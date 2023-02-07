from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class commonclass:
    signin_xpath = "//a[contains(text(),'Sign In')]"
    username_id = 'user_name'
    password_id = 'password'
    popsignin_xpath = "//span[normalize-space()='Sign In']"
    cricketsport = "//div[@class='title'][normalize-space()='Cricket']"
    scrollmarket_class = 'market-data'
    scrollmarketheader = '//*[@id="category-tab"]/div[1]/app-market-type/div[1]/div/div'
    market_xpath = '//div[2][contains(@class,"market-data")]//div[1]//div[1]//a[1]'
    back_xpath = '//a[contains(@class,"back-bet-btn")]//p'
    lay_xpath = '//a[contains(@class,"lay-bet-btn")]//p'
    betprice_xpath = '//input[contains(@class,"ng-touched")]'
    placebet_xpath = '//button[contains(@class,"btn btn-bet")]'
    exposure_xpath = "//li[@class='no-wallet']//li[2]//div[2]"
    withdrawable_xpath = "//li[@class='no-wallet']//li[1]//div[2]"
    walletbalance_xpath = '//div[contains(@class,"bal-title")]//span'
    alertmessage_class = 'toast-message'
    mainteam_xpath = '//*[@id="category-tab"]/div[1]/app-market-type/div[2]/div/div/div[1]/div/div[1]/p/span[2]'
    betteamname_xpath = '//*[@id="tab2"]/div[1]/div[1]/app-matchedbet/div[2]/div[2]/div[2]/div/div[1]/div[1]'
    typeofbet_xpath = '//*[@id="tab2"]/div[1]/div[1]/app-matchedbet/div[2]/div[2]/div[2]'
    stake_xpath = '//*[@id="tab2"]/div[1]/div[1]/app-matchedbet/div[2]/div[2]/div[2]/div/div[3]'
    pl_xpath = '//*[@id="tab2"]/div[1]/div[1]/app-matchedbet/div[2]/div[2]/div[2]/div/div[4]'
    userprofile_xpath = "//a[@class='dropdown-trigger']"
    openbet_xpath = '//*[@id="dropdown1"]/app-user-menu/li[7]/a'
    reportselection_xpath = '//tbody/tr[1]/td[4]'
    reporttype_xpath = '//tbody/tr[1]/td[5]'
    reportstake_xpath = '//tbody/tr[1]/td[7]'
    reportpl_xpath = '//tbody/tr[1]/td[8]'

    def __init__(self, driver):
        self.driver = driver

    def scrollmarketdata(self):
        element = self.driver.find_element(By.XPATH, self.scrollmarketheader)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def gettypeofbet(self):
        bettype = self.driver.find_element(By.XPATH, self.typeofbet_xpath).get_attribute("class")
        if 'blue' in bettype:
            typeofbet = "Back"
        else:
            typeofbet = "Lay"
        return typeofbet

    def getstake(self):
        stake = self.driver.find_element(By.XPATH, self.stake_xpath).text
        return stake

    def getpl(self):
        pl = self.driver.find_element(By.XPATH, self.pl_xpath).text
        return pl

    def getselection(self):
        teamname = self.driver.find_element(By.XPATH, self.betteamname_xpath).text
        return teamname

    def getmainteamname(self):
        teamname = self.driver.find_element(By.XPATH, self.mainteam_xpath).text
        mainteam = []
        for i in teamname:
            if i != "\n":
                mainteam.append(i)
            else:
                break
        mainteam = "".join(mainteam)
        return mainteam

    def clickopenbet(self):
        self.driver.find_element(By.XPATH, self.openbet_xpath).click()

    def getreportselection(self):
        selection = self.driver.find_element(By.XPATH, self.reportselection_xpath).text
        return selection

    def getreportpl(self):
        reportpl = self.driver.find_element(By.XPATH, self.reportpl_xpath).text
        return reportpl

    def getreportstake(self):
        reportstake = self.driver.find_element(By.XPATH, self.reportstake_xpath).text
        return reportstake

    def getreporttype(self):
        reporttype = self.driver.find_element(By.XPATH, self.reporttype_xpath).text
        return reporttype

    def clickuserprofile(self):
        self.driver.find_element(By.XPATH, self.userprofile_xpath).click()

    "Not Used"
    def getbackprice(self):
        backprice = self.driver.find_element(By.XPATH, self.back_xpath).text
        return backprice

    "Not Used"
    def getlayprice(self):
        layprice = self.driver.find_element(By.XPATH, self.lay_xpath).text
        return layprice

    def getalertmessage(self):
        alert = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.alertmessage_class))).text
        return alert

    def eventname(self):
        test1=[]
        ename = self.driver.find_element(By.XPATH, self.market_xpath).text
        for name in ename:
            if name == "\n":
                test1.append(" ")
            elif name !="\n":
                test1.append(name)
        eventname = "".join(test1)
        return eventname

    def clickmarket(self):
        self.driver.find_element(By.XPATH, self.market_xpath).click()

    def scrollmarket(self):
        element = self.driver.find_element(By.CLASS_NAME, self.scrollmarket_class)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def clickcricket(self):
        self.driver.find_element(By.XPATH, self.cricketsport).click()

    def clicksignin(self):
        self.driver.find_element(By.XPATH, self.signin_xpath).click()

    def setusername(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.popsignin_xpath).click()

    def hoveroverwallet(self):
        a = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.walletbalance_xpath)))
        act = a.move_to_element(element)
        act.perform()

    def getwalletamount(self):
        test1 = self.driver.find_element(By.XPATH, self.walletbalance_xpath).text
        amount = [amt for amt in test1 if amt != ","]
        amount = "".join(amount)
        stringamount = str(amount)
        walletamount = float(stringamount)
        return walletamount

    def getexposure(self):
        exposure = self.driver.find_element(By.XPATH, self.exposure_xpath).text
        exposure1 = [exp for exp in exposure if exp != "-"]
        exposure2 = "".join(exposure1)
        strexp = str(exposure2)
        exposure = float(strexp)
        return exposure

    "Not Used"
    def getwithdrawable(self):
        withdrawable = self.driver.find_element(By.XPATH, self.withdrawable_xpath).text
        amt = [amount for amount in withdrawable if amount != ","]
        amount = str(amt)
        withdrawableamount = float(amount)
        return withdrawableamount

    def clickbackrate(self):
        self.driver.find_element(By.XPATH, self.back_xpath).click()

    "Not Used"
    def clicklayrate(self):
        self.driver.find_element(By.XPATH, self.lay_xpath).click()

    def setbetprice(self, betprice):
        self.driver.find_element(By.XPATH, self.betprice_xpath).clear()
        self.driver.find_element(By.XPATH, self.betprice_xpath).send_keys(betprice)

    def clickplacebet(self):
        self.driver.find_element(By.XPATH, self.placebet_xpath).click()


class hattrick:

    backliability = '//*[@id="category-tab"]/div[1]/app-market-type/div[2]/div/div/div[3]/div/div[1]/p/span[2]/span/span[3]'
    layliability = '//*[@id="category-tab"]/div[1]/app-market-type/div[2]/div/div/div[1]/div/div[1]/p/span[2]/span/span[3]'

    def __init__(self, driver):
        self.driver = driver

    def getliability(self, liailitytype):
        if liailitytype == "Back":
            lb = self.driver.find_element(By.XPATH, self.backliability).text
            a = str(lb)
            b = float(a)
            backliaility = abs(b)
            return backliaility
        elif liailitytype == "Lay":
            llb = self.driver.find_element(By.XPATH, self.layliability).text
            ab = str(llb)
            bb = float(ab)
            layliaility = abs(bb)
            return layliaility
        else:
            print("enter valid input")

class empire:

    liability = '//*[@id="category-tab"]/div[1]/app-market-type/div[2]/div/div/div[3]/div/div[1]/span/span[3]'

    def __init__(self, driver):
        self.driver = driver

    def getliability(self):
        liability = self.driver.find_element(By.XPATH, self.liability).text
        return liability


class run567:

    liability = '//*[@id="category-tab"]/div[1]/app-market-type/div[2]/div/div/div[3]/div/div[1]/span/span[3]'

    def __init__(self, driver):
        self.driver = driver

    def getliability(self):
        liability = self.driver.find_element(By.XPATH, self.liability).text
        return liability

    ce = commonclass(driver=None)


class thalaiva:

    liability = '//*[@id="category-tab"]/div[1]/app-market-type/div[2]/div/div/div[3]/div/div[1]/span/span[3]'

    def __init__(self, driver):
        self.driver = driver

    def getliability(self):
        liability = self.driver.find_element(By.XPATH, self.liability).text
        return liability


