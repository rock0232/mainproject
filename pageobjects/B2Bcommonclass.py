import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By



class B2Bcommonclass:

    signin_xpath = "//a[@class='btn']//span[@class='animate-btn']"
    username_id = "user_name"
    password_id = "password"
    poplogin_xpath = "//a[@class='btn loginButton']"
    closebutton_xpath = "//div[@class='modal modal-fixed-footer open']//i[@class='fa fa-times']"
    scrollmarket_class = "market-data"
    market_xpath = '//div[1][contains(@class,"market-data")]//div[1]//div[1]//a[1]'
    back_xpath = '//*[@id="category-tab"]/div[1]/app-market-type/div[2]/div/div/div[1]/div/div[4]/a/p'
    lay_xpath = '//a[contains(@class,"lay-bet-btn")]//p'
    betprice_xpath = '//*[@id="category-tab"]/div[1]/app-market-type/div[2]/div/div/div[2]/div/div/form/div[1]/div/div[2]/div[2]/input'
    placebet_xpath = '//button[contains(@class,"btn btn-bet")]'
    alertmessage_class = 'toast-message'
    wallet_xpath = "//li[@class='ac_bal']//span[2]"
    liability_xpath = "//li[@class='liability']//span[2]"
    userporfile_xpath = "//a[@class='dropdown-trigger']"
    mybet_xpath = "//body//pb-header//div//header//div//nav//div//div//ul//li//ul//li//a[contains(text(),'My Bets')]"
    backteamname_xpath = "//div[1][contains(@class,'team-market')]/div[1]/div[1]/div[1]/div[1]/p[1]"
    betteamname_xpath = "//div[@class='matchbet is-hidden is-show']//div[@class='beatteam']"
    typeofbet_xpath = '/html/body/app-root/app-home-layout/body/app-market/main/div[1]/div/div[2]/div/div/div[2]/app-match-bet/div[1]/div[3]'
    stake_xpath = '/html/body/app-root/app-home-layout/body/app-market/main/div[1]/div/div[2]/div/div/div[2]/app-match-bet/div[1]/div[3]/div/div[3]'
    pl_xpath = '/html/body/app-root/app-home-layout/body/app-market/main/div[1]/div/div[2]/div/div/div[2]/app-match-bet/div[1]/div[3]/div/div[4]'
    reportselection_xpath = "//tbody/tr[1]/td[4]"
    reporttype_xpath = '//tbody/tr[1]/td[5]'
    reportstake_xpath = '//tbody/tr[1]/td[7]'
    reportpl_xpath = '//tbody/tr[1]/td[8]'
    inplay_xpath = "//div[@class='date-time in-play']//parent::div//parent::div//following-sibling::a"
    soccer_Xpath = "//div[@class='title'][normalize-space()='Soccer']"
    numofinplaymatch_xpath = '/html/body/app-root/app-home-layout/body/app-dashboard/main/div/div/app-common-dashboard/div/ngx-slick-carousel/div/div/div//child::a//child::div//child::span'
    wintossback_css = "body > app-market:nth-child(3) > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > app-match:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > app-market-type:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4)"
    manualodds_xpath = "//div//a[contains(@title,'ManualODD: 2')]"
    manualbetprice_css = "div[class='hide-on-med-and-down'] div:nth-child(2) > input"
    inplay = True
    inactivemarket_xpath = "//div[contains(text(),' Match Odds')]//ancestor::div[contains(@class,'bet-semiheader is-hidden is-show')]//following-sibling::div[contains(@class,'bet-list is-hidden is-show')]/div/div[2]/div"
    #//div[contains(text(),' Match Odds')]//parent::div[contains(@class,'bet-semiheader is-hidden is-show')]
    logo_class = "brand-logo"
    slidesports_xpath = "//ngx-slick-carousel[@class='slider slick-initialized slick-slider']//button[@aria-label='Next'][normalize-space()='Next']"
    sidebarinplaylogo_xpath = "//div[@class='sports-icon inplay']"
    inplaytext_xpath = "//span[normalize-space()='In Play']"
    inplaylist_CSS = "header .sidenav .upcoming-event ul li a"
    homebutton = "//ul[@class='left']//a[@class='active']"

    def __init__(self, driver):
        self.driver = driver

    def clickinplay(self):
        a = ActionChains(self.driver)
        element1 = self.driver.find_element(By.XPATH, self.sidebarinplaylogo_xpath)
        element2 = self.driver.find_element(By.XPATH, self.inplaytext_xpath)
        act = a.move_to_element(element1).click(element2)
        time.sleep(1)
        act.perform()

    def clicklogo(self):
        self.driver.find_element(By.CLASS_NAME, self.logo_class).click()

    def getinplaymatchcount(self):
        element = self.driver.find_elements(By.XPATH, self.numofinplaymatch_xpath)
        inplay = []
        intinplay = None
        for j in range(len(element)):
            if j == 7 or j ==14 or j ==21:
                try:
                    self.driver.find_element(By.XPATH, self.slidesports_xpath).click()
                    time.sleep(2)
                except:
                    pass
            inplay.append(f"start{j}")
            for s in element[j].text:
                if s == "\n":
                    inplay.append(f"s{j}")
                else:
                    inplay.append(s)
            inplay.append(f"end{j}")
            index1 = inplay.index(f"start{j}")
            index2 = inplay.index(f"s{j}")
            index3 = inplay.index(f"end{j}")
            inpl = inplay[index2+1:index3]
            join = "".join(inpl)
            intinplay = int(join)

            if intinplay > 0:
                element[j].click()
                totalmatch = inplay[index1+1:index2]
                tmatch = "".join(totalmatch)
                cctotalmatches = int(tmatch)
                self.inplay = True
                # self.inplay = False
                return cctotalmatches, intinplay
        if intinplay == 0:
            ind1 = inplay.index("start0")
            ind2 = inplay.index("s0")
            totalmatch = inplay[ind1 + 1:ind2]
            tmatch = "".join(totalmatch)
            cctotalmatches = int(tmatch)
            self.inplay = False
            return cctotalmatches, intinplay

    def clicksocceraport(self):
        self.driver.find_element(By.XPATH, self.soccer_Xpath).click()

    def getreportselection(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.reportselection_xpath)))
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

    def gettypeofbet(self):
        bettype = self.driver.find_element(By.XPATH, self.typeofbet_xpath).get_attribute("class")
        if 'blue' in bettype:
            typeofbet = "Back"
        else:
            typeofbet = "Lay"
        return typeofbet

    def getstake(self):
        sta = self.driver.find_element(By.XPATH, self.stake_xpath).text
        stake = int(sta)
        return str(stake)

    def getpl(self):
        pl = self.driver.find_element(By.XPATH, self.pl_xpath).text
        return pl

    def getselection(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.betteamname_xpath)))
        teamname = self.driver.find_element(By.XPATH, self.betteamname_xpath).text
        return teamname

    def getmainteamname(self):
        teamname = self.driver.find_element(By.XPATH, self.backteamname_xpath).text
        return teamname

    def clickmybet(self):
        self.driver.find_element(By.XPATH, self.mybet_xpath).click()

    def clickuserprofile(self):
        self.driver.find_element(By.XPATH, self.userporfile_xpath).click()

    def getliability(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.liability_xpath)))
        lia = self.driver.find_element(By.XPATH, self.liability_xpath).text
        liability = float(lia)
        return liability

    def getwalletamount(self):
        wal = self.driver.find_element(By.XPATH, self.wallet_xpath).text
        walletamount = float(wal)
        return walletamount

    def getalertmessage(self):
        alert = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.alertmessage_class))).text
        return alert

    def clickplacebet(self):
        self.driver.find_element(By.XPATH, self.placebet_xpath).click()

    def setbetprice(self, betprice):
        self.driver.find_element(By.XPATH, self.betprice_xpath).clear()
        self.driver.find_element(By.XPATH, self.betprice_xpath).send_keys(betprice)

    def clickbackrate(self):
        self.driver.find_element(By.XPATH, self.back_xpath).click()

    def clickmarket(self):
        self.driver.find_element(By.XPATH, self.market_xpath).click()

    def geteventname(self):
        test1=[]
        ename = self.driver.find_element(By.XPATH, self.market_xpath).text
        for name in ename:
            if name == "\n":
                test1.append(" ")
            elif name !="\n":
                test1.append(name)
        eventname = "".join(test1)
        return eventname

    def clickinplaymarket(self):
        count = self.getinplaymatchcount()
        if count is not None:
            relcount = int(count*1.5)
            eventname = []
            for i in range(0,relcount):
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
                try:
                    elememt = self.driver.find_element(By.XPATH, self.inplay_xpath)
                    if elememt:
                        for name in elememt.text:
                            if name == "\n":
                                eventname.append(" ")
                            elif name != "\n":
                                eventname.append(name)
                        elememt.click()
                        break
                except:
                    pass
            if eventname:
                eventname = "".join(eventname)
                return eventname
        else:
            pass

    def scrollmarket(self):
        element = self.driver.find_element(By.CLASS_NAME, self.scrollmarket_class)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def clickclose(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.closebutton_xpath))).click()
        # self.driver.find_element(By.XPATH, self.closebutton_xpath).click()
        # WebDriverWait(self.driver, 10).until(
        #             EC.visibility_of_element_located((By.CLASS_NAME, self.alertmessage_class))).text

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.poplogin_xpath).click()

    def setpassword(self,password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def setusername(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def clicksignin(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.signin_xpath)))
        self.driver.find_element(By.XPATH, self.signin_xpath).click()


