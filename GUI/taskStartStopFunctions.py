from PyQt6.QtWidgets import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from seleniumwire import webdriver

import json
import requests
import time
from discord_webhook import DiscordWebhook
from random import randrange

#Used for for threading tasks
from time import sleep
from threading import Thread
from threading import Event


###########################
#      Thread Class       #
###########################
class CustomThread(Thread):
    # constructor
    def __init__(self, event, rowSelected,gui,taskStatusBacking,threadList):
        # call the parent constructor
        super(CustomThread, self).__init__()

        # store the event
        self.event = event
        self.rowSelected=rowSelected
        self.gui=gui
        self.stopTask=False 

        #thread lists
        self.taskStatusBacking=taskStatusBacking
        self.threadList=threadList

    def run(self):
        productFound=1
        if self.rowSelected<0:
            return

        #Variable Setup
        f=open('./GUI/settings.json',"r")
        settingsData=json.load(f)
        f.close()

        proxyInfo=None
        proxyUtilized=None
        profileInfo=None
        taskInfo=settingsData['tasks'][self.rowSelected]
        webUrl=None
        sessionUrl=None
        chromePath = 'chromedriver.exe'

        for i in range(0,len(settingsData['info'])):
            if(settingsData['info'][i].get('id'))==taskInfo['profile']:
                profileInfo=settingsData['info'][i]

        for i in range(0,len(settingsData['proxies'])):
            if(settingsData['proxies'][i].get('proxyGroupName'))==taskInfo['proxyGroup']:
                proxyInfo=settingsData['proxies'][i]    
        a=proxyInfo.get('proxyList')[randrange(len(proxyInfo.get('proxyList')))]
        b=''
        if a=='':
            proxyUtilized="local"
        else:

            b=proxyInfo.get('proxyList')[randrange(len(proxyInfo.get('proxyList')))].split(":")
            proxyUtilized=b[2]+"@"+b[3]+":"+b[0]+":"+b[1]
        webUrl=taskInfo['site']

        ###########################
        #   Create Queue Bypass   #
        ###########################
        self.gui.taskTable.setItem(self.rowSelected,6,QTableWidgetItem('Creating Queue Bypass'))
        #Get Dummy Product Link For Bypass
        dummyProductLink=productPlaceholder(self.gui,proxyUtilized,webUrl)
        if dummyProductLink=='invalid':
            print("invalid link")
            return

        #Proxy Setup if Applicable & Open Browser, format: http://hp7u1otc:0k6h0cga@81.200.148.5:3190
        optionsDebug = webdriver.ChromeOptions()
        optionsDebug.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser=None
        if proxyUtilized!="local":
            http=("http://%s:%s@%s:%s"%(b[2],b[3],b[0],b[1]))
            optionsProxy = {
                'proxy': {
                    'http': http, 
                    'https': http
                }
            }
            browser = webdriver.Chrome(chromePath,seleniumwire_options=optionsProxy,options=optionsDebug)
        else:
            browser = webdriver.Chrome(chromePath,options=optionsDebug)

        # (1) First thing we do is clear the cart & load dummy product or the checkout sesion won't be created for some reason
        browser.get(webUrl+'cart/clear')
        browser.get(dummyProductLink)

        # (2) Wait Through queue up to 5 min (Will need to update this to pull the actual queue timer on the page later)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(("id", "checkout_shipping_address_country")))

        #(3) Get the session URL and clear the cart
        sessionUrl = browser.current_url
        browser.get(webUrl+'cart/clear')

        ##############################
        #      Product Monitor       #
        ##############################
        #(4) Product Monitor Loop
        delayFlag=False
        while not self.event.is_set() :
            self.gui.taskTable.setItem(self.rowSelected,6,QTableWidgetItem('Monitoring'))
            if self.stopTask==True:
                break
            productFound=productMonitor(self.gui,self.rowSelected,proxyUtilized)
            if productFound=='invalid':
                print("invalid url, Thread now closing")
                return 
            if delayFlag == True:
                
                delay=float(settingsData['tasks'][self.rowSelected]['delay'])/1000
                print("Product Monitor Delaying for ", delay, " seconds")    
                sleep(delay)
            delayFlag=True
        
        ##############################
        #    (Cart Actual Product)   #
        ##############################
        #(5) Checkout Product, If Bot protection is up, waits for the user to sovle and redirect to checkout page 1
        self.gui.taskTable.setItem(self.rowSelected,6,QTableWidgetItem('Checking Out'))
        browser.get(productFound)
        checkoutPageStatus=False
        while checkoutPageStatus==False:
            try:
                browser.find_element(By.ID, "checkout_email")
                checkoutPageStatus=True
            except:
                print("Solve Captcha or Checkout Page Loading")
        start= time.time()
        
        ##############################
        #      Checkout Page 1       #
        ##############################
        #(6) Fill out Checkout Page 1 
        select = Select(browser.find_element("id", 'checkout_shipping_address_country'))
        time.sleep(.05)
        select.select_by_visible_text(profileInfo.get('sCountry'))
        time.sleep(.05)
        browser.find_element("id", "checkout_email").send_keys(profileInfo.get('email'))
        time.sleep(.05)
        browser.find_element("id", "checkout_shipping_address_first_name").send_keys(profileInfo.get('sFirstName'))
        time.sleep(.05)
        browser.find_element("id", "checkout_shipping_address_last_name").send_keys(profileInfo.get('sLastName'))
        time.sleep(.05)
        browser.find_element("id", "checkout_shipping_address_address1").send_keys(profileInfo.get('sAdd1'))
        time.sleep(.05)
        browser.find_element("id", "checkout_shipping_address_city").send_keys(profileInfo.get('sCity'))
        select = Select(browser.find_element("id", 'checkout_shipping_address_province'))
        time.sleep(.05)
        select.select_by_visible_text(profileInfo.get('sProvince'))
        time.sleep(.05)
        browser.find_element("id", "checkout_shipping_address_zip").send_keys(profileInfo.get('sZip'))
        time.sleep(.05)
        browser.find_element("id", "checkout_shipping_address_phone").send_keys(profileInfo.get('pPhoneNumber'))
        time.sleep(.05)
        browser.find_element("id", "checkout_shipping_address_address2").send_keys(profileInfo.get('sAdd2'))
        time.sleep(.05)
        browser.find_element("id", "continue_button").click()

        ##############################
        #      Checkout Page 2       #
        ##############################
        #(6) Fill out Checkout Page 2
        WebDriverWait(browser, 20).until(EC.visibility_of_element_located(("id", "continue_button")))
        
        #sometimes the continue button isnt clickable right away since shipping rates need to be loaded
        while(1):
            try:
                browser.find_element("id", "continue_button").click()
                WebDriverWait(browser, 1).until(EC.visibility_of_element_located(("xpath", "//*[@title='Field container for: Card number']")))
                break
            except:
                print("Continue Button Waiting to be Clickable")

        ##############################
        #      Checkout Page 3       #
        ##############################
        #(7) Fill out Checkout Page 3
        
        test=browser.find_element("xpath","//*[@title='Field container for: Card number']")
        iframe = browser.find_element("xpath","//*[@title='Field container for: Card number']")

        browser.switch_to.frame(iframe)
        time.sleep(.00009)
        browser.find_element("id", "number").send_keys(profileInfo.get('pCardNumber')[0:4])
        time.sleep(.00009)
        browser.find_element("id", "number").send_keys(profileInfo.get('pCardNumber')[4:10])
        time.sleep(.00009)
        browser.find_element("id", "number").send_keys(profileInfo.get('pCardNumber')[10:14])

        browser.switch_to.default_content()
        iframe = browser.find_element("xpath","//*[@title='Field container for: Name on card']")
        browser.switch_to.frame(iframe)
        time.sleep(.00009)
        browser.find_element("id", "name").send_keys(profileInfo.get('sFirstName'))

        browser.switch_to.default_content()
        iframe = browser.find_element("xpath","//*[@title='Field container for: Expiration date (MM / YY)']")
        browser.switch_to.frame(iframe)
        time.sleep(.00009)
        browser.find_element("id", "expiry").send_keys(profileInfo.get('pMonth'))
        time.sleep(.00009)
        browser.find_element("id", "expiry").send_keys(profileInfo.get('pYear'))

        browser.switch_to.default_content()
        iframe = browser.find_element("xpath","//*[@title='Field container for: Security code']")
        browser.switch_to.frame(iframe)
        time.sleep(.00009)
        browser.find_element("id", "verification_value").send_keys(profileInfo.get('pCCV'))

        time.sleep(.00009)
        browser.switch_to.default_content()
        #browser.find_element("id", "continue_button").click()

        #Temporary Checkout Page From One of My Previous Purchases
        end= time.time()
        executionTime=end-start
        print("Checkout Button Clicked, Checkout Execution time: ",executionTime)
        browser.get('https://nrml.ca/13343831/orders/086a03063ea7fbebca66276c1a8b353f')

        ##############################
        #      Checkout Page 4       #
        ##############################
        #(8) Confirmation Page
        #Confirmation page always has the unique class "step__footer__continue-btn btn"
        #Normally I'd use the class that contains the order # but it doesnt always show
        #If unsuccessful, notify the user that the product is sold out

        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".step__footer__continue-btn")))
            confirmationUrl = browser.current_url
            #Discord Webhook the Confirmation Page
            webhook = DiscordWebhook(url=self.gui.webhookInput.text(), content="Successfully Checked Out!: "+confirmationUrl+"\nCheckout Page Execution Time: "+str(executionTime)+" seconds")
            response = webhook.execute()
        except:
            print("Checkout Unsuccessful or Sold out")
        self.gui.taskTable.setItem(self.rowSelected,6,QTableWidgetItem('Stand By'))
        time.sleep(5)
        browser.quit()

        #(9) Delete threads from list & thread backing array
        print("Thread "+str(self.rowSelected)+' closing down\n')
        for j in range(len(self.taskStatusBacking)):
            if self.taskStatusBacking[j]==self.rowSelected:
                self.threadList.pop(j)
                self.taskStatusBacking.pop(j) 
                break;
        print("Task Complete, Thread Closed, Thread List Status is now => ",self.threadList)
        print("Task Complete, Thread Closed, Thread Backing Array is now => ",self.taskStatusBacking)

    #stopTask is used to notify that a producct has been found
    def stopTaskFunc(self):
        self.stopTask=True

    #Edge Case if task is deleted while other tasks are running and indexes are rearranged
    def taskDeletedAdjust(self):
        self.rowSelected=self.rowSelected-1


##############################
#     Start Task Button      #
##############################
def clickStartTaskBtn(self, event):
    rowSelected=self.taskTable.currentRow()
    if rowSelected >=0:
        thread1 = CustomThread(self.event,rowSelected,self,self.taskStatusBacking,self.threadList)
        self.threadList.append(thread1)
        self.threadList[len(self.threadList)-1].start()
        self.taskStatusBacking.append(rowSelected)
        print("Task Started, thread backing array is =>",self.taskStatusBacking)
        print("Task Started, thread array is =>",self.threadList)
    #Need to add to the backing array the rowSelected variable
    #Need a condition where if a task is already running it wont append again


##############################
#      Stop Task Button      #
##############################
def clickStopTaskBtn(self, event):
    r = self.taskTable.currentRow()
    if r>=0:  
        self.taskTable.setItem(r,6,QTableWidgetItem('Closing..'))
        print("Task Stopped, thread backing array is =>",self.taskStatusBacking)
        print("Task Stopped, thread array is =>",self.threadList)
        for j in range(len(self.taskStatusBacking)):
            if self.taskStatusBacking[j]==r:
                self.threadList[j].stopTaskFunc()   
                self.threadList.pop(j)
                self.taskStatusBacking.pop(j)
                break

def clickStopAllTaskBtn(self, event):
    self.event.set()
    self.threadList.clear()
    self.taskStatusBacking.clear()
    self.event = Event()

def productPlaceholder(self,proxyUtilized,webUrl):
    # Proxy Implementation
    itemDNE=False
    data=None
    pageNum=0
    while itemDNE == False:
        pageNum +=1
        webScrapeLink=webUrl+"products.json?limit=250&page="
        webScrapeLink+=str(pageNum)
        r=None
        if proxyUtilized=="local":
            r = requests.get(webScrapeLink)
        else:
            proxy  = {'http': proxyUtilized}
            print("A proxy was used => ",proxy)
            r = requests.get(webScrapeLink,proxies=proxy)
        try:
            data = r.json()
        except:
            print("Invalid Link")
            return "invalid"
        #Scrape products.json file
        for item in data ['products']:
            title=item['title']
            handle=item['handle']
            productType=item['product_type']
            variantObject=item['variants']
            productAvailable =True;
            if productAvailable ==True:
                for obj in variantObject:
                    itemId = obj['id']
                    available = obj ['available']
                    if (available==True):
                        finalLink=webUrl+"cart/"+str(itemId)+":1"
                        print("Placeholder product found: " +handle)
                        return finalLink
                        
def productMonitor(self,row,proxyUtilized):
    start= time.time()
    rowSelected=row
    f=open('./GUI/settings.json',"r")
    settingsData=json.load(f)
    f.close()    

    #Task Criterias
    posKeyList=[]
    negKeyList=[]
    userSizeList =[]
    randomFlag =False
    webCartLink=""
    webScrapeLink=""
    cartedProductName=""

    # Variables used for Veritfication
    validCartId = False
    itemDNE = False  
    pageNum=0
    checkoutSize =0

    # fix the use of this var
    size=""
    if rowSelected>=0:
        self.taskTable.setItem(rowSelected,6,QTableWidgetItem('Monitoring'))
        posKeyList=settingsData['tasks'][rowSelected]['key']
        negKeyList=settingsData['tasks'][rowSelected]['neg']
        userSizeList=settingsData['tasks'][rowSelected]['size']
        webCartLink=settingsData['tasks'][rowSelected]['site']+"cart/"

        # Maybe go back and make sure keyword values are negative at creation time instead of doing it here
        for i in range (len(posKeyList)):
            posKeyList[i]=posKeyList[i].lower()
        for i in range (len(negKeyList)):
            negKeyList[i]=negKeyList[i].lower()
        
    else:
        end= time.time()
        print("No Row Selected, Exectuion Time = ",end-start," seconds")
        return
    
    if "random" in userSizeList:
        randomFlag =True

    while itemDNE == False:
        pageNum +=1
        webScrapeLink=settingsData['tasks'][rowSelected]['site']+"products.json?limit=250&page="
        webScrapeLink+=str(pageNum)

    # Proxy Implementation
        r=None
        if proxyUtilized=="local":
            r = requests.get(webScrapeLink)
        else:
            proxy  = {'http': proxyUtilized}
            r = requests.get(webScrapeLink,proxies=proxy)
        #r = requests.get(webScrapeLink)
        try:
            data = r.json()
        except:
            print("Invalid Link")
            return

        if sum(len(v) for v in data.values())==0:
            itemDNE=True
            print("No Products Loaded")
            return

        # Checking Item Availibility
        for item in data ['products']:
            title=item['title']
            handle=item['handle']
            productType=item['product_type']
            variantObject=item['variants']
            productAvailable =True;
            
            if productType=="Footwear" or productType=="MENS FOOTWEAR" or productType =="MENS FOOTWEAR":
                #Compare product handle to positive and negative keywords
                for item in posKeyList:
                    if not item in handle.lower():
                        productAvailable =False;
                for item in negKeyList:
                    if item in handle.lower():
                        productAvailable =False;
            # Only webscraped footwear or return false
            else:
                productAvailable =False;

            if productAvailable ==True and itemDNE == False:
                cartedProductName=handle
                itemDNE = True
                for obj in variantObject:
                    itemId = obj['id']
                    price = obj['price']
                    sku = obj ['sku']
                    available = obj ['available']
                    if obj ['option1'] in userSizeList:
                        size=obj ['option1']
                    if obj ['option2'] in userSizeList:
                        size=obj ['option2']
                    if obj ['option3'] in userSizeList:
                        size=obj ['option3']

                    if (available==True and validCartId==False and size in userSizeList):
                        webCartLink+=str(itemId)+":1"
                        validCartId=True
                        break
                
    if(validCartId==True):
        print("Checkout product found in size ",size," :",webCartLink)
        end= time.time()
        executionTime=end-start
        webhook = DiscordWebhook(url=self.webhookInput.text(), content="Successful Cart Creation: "+webCartLink+"\nProduct: "+cartedProductName+"\nsize: "+size+"\nExecuted in: "+str(executionTime)+" seconds")
        webhook.execute()
        
        try:
            for j in range(len(self.taskStatusBacking)):
                if self.taskStatusBacking[j]==rowSelected:
                    self.threadList[j].stopTaskFunc()  
            return webCartLink           
        except:
            print("Invalid Discord Webhook")
            return 'invalid'
    else:
        print("Product Not Found, Monitoring Again")
        return 'invalid'