import json
import onLoadFunctions
import requests
import time
from PyQt6.QtWidgets import *
from discord_webhook import DiscordWebhook

##############################################
#      Used for for threading tasks          #
############################################## 

from time import sleep
from threading import Thread
from threading import Event


class CustomThread(Thread):
    # constructor
    def __init__(self, event, rowSelected,gui):
        # call the parent constructor
        super(CustomThread, self).__init__()
        # store the event
        self.event = event
        self.rowSelected=rowSelected
        self.gui=gui
        self.stopTask=False 
    # execute task
    def run(self):
        productFound=1
        # execute a task in a loop
        if self.rowSelected>=0:
            self.gui.taskTable.setItem(self.rowSelected,6,QTableWidgetItem('Monitoring'))
        f=open('./GUI/settings.json',"r")
        settingsData=json.load(f)
        f.close()
        while not self.event.is_set() :
            if self.stopTask==True:
                break
            delay=float(settingsData['tasks'][self.rowSelected]['delay'])/1000
            # block for a moment
            
            # check for stop
            
            
            # report a message
            print("Worker thread "+str(self.rowSelected)+" running...\n")
            print("calling product monitor function, row is: "+str(self.rowSelected))
            productFound=productMonitor(self.gui,self.rowSelected)
            if productFound==0:
                print("Product Found, Thread now closing")
                break
            
            sleep(delay)
        if self.rowSelected>=0:

            self.gui.taskTable.setItem(self.rowSelected,6,QTableWidgetItem('Stand By'))        

        print("Thread "+str(self.rowSelected)+' closing down\n')

    def stopTaskFunc(self):
        self.stopTask=True

    def taskDeletedAdjust(self):
        print("Taking into account deleted index in settings.json for tasks")
        print(str(self.rowSelected)+" => "+str(self.rowSelected-1))
        self.rowSelected=self.rowSelected-1



##############################################
#            Start Task Button             #
############################################## 
def clickStartTaskBtn(self, event):
    print("Start Button clicked")
    rowSelected=self.taskTable.currentRow()
    thread1 = CustomThread(self.event,rowSelected,self)
    self.threadList.append(thread1)
    
    self.threadList[len(self.threadList)-1].start()
    self.taskStatusBacking.append(rowSelected)
    print(self.taskStatusBacking)
    print(self.threadList)
    

    #Need to add to the backing array the rowSelected variable
    # Need a condition where if a task is already running it wont append again

##############################################
#             Stop Task Button               #
############################################## 
def clickStopTaskBtn(self, event):
    r = self.taskTable.currentRow()
    if r>=0:  
        print("Stop Button Pressed")
        self.taskTable.setItem(r,6,QTableWidgetItem('Closing..'))
        print(self.taskStatusBacking)
        print(self.threadList)
        for j in range(len(self.taskStatusBacking)):
            if self.taskStatusBacking[j]==r:
                self.threadList[j].stopTaskFunc()   
                self.threadList.pop(j)
                self.taskStatusBacking.pop(j)
                break

def clickStopAllTaskBtn(self, event):
    print("Stop All Tasks Button Pressed")
    self.event.set()
    self.threadList.clear()
    self.event = Event()

def productMonitor(self,row):
    start= time.time()
    rowSelected=row
    #rowSelected = self.taskTable.currentRow()

    f=open('./GUI/settings.json',"r")
    settingsData=json.load(f)
    f.close()    

    ## Product Specification Parameters
    posKeyList=[]
    negKeyList=[]
    userSizeList =[]
    randomFlag =False
    webCartLink=""
    webScrapeLink=""
    cartedProductName=""

    # Variables used for Veritfication
    validCartId = False
    itemDNE = False     # DNE => Does not Exist
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
        print("No Row Selected, Exectuion Time = ",end-start,"ms")
        return
    
    if "random" in userSizeList:
        randomFlag =True
    
    #print(webScrapeLink)

    while itemDNE == False:
        pageNum +=1
        webScrapeLink=settingsData['tasks'][rowSelected]['site']+"products.json?limit=250&page="
        webScrapeLink+=str(pageNum)
        r = requests.get(webScrapeLink)
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
            

            if productType=="Footwear":
                #Compare product handle to positive and negative keywords
                for item in posKeyList:
                    if not item in handle.lower():
                        productAvailable =False;
                        #print("Positive Key Word Condition Failed")
                for item in negKeyList:
                    if item in handle.lower():
                        productAvailable =False;
                        #print("Negative Key Word Condition Failed")
            # Only doing footwear so we return false
            else:
                productAvailable =False;



            if productAvailable ==True and itemDNE == False:
                print("Passed Check: " +handle)
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
                    #size = variant ['option1']

                    if (available==True and validCartId==False and size in userSizeList):
                        webCartLink+=str(itemId)+":1"
                        validCartId=True
                        break


                
    if(validCartId==True):
        print("Availible product found ",webCartLink)
        print("Availible in Size: ",size)
        end= time.time()
        executionTime=end-start
        #self.taskTable.setItem(rowSelected,6,QTableWidgetItem('Stand By'))
        
        try:
            for j in range(len(self.taskStatusBacking)):
                if self.taskStatusBacking[j]==rowSelected:
                    self.threadList[j].stopTaskFunc()   
                    self.threadList.pop(j)
                    self.taskStatusBacking.pop(j)
            print(self.taskStatusBacking)
            print(self.threadList)
            webhook = DiscordWebhook(url=self.webhookInput.text(), content="Successful Cart Creation: "+webCartLink+"\nProduct: "+cartedProductName+"\nsize: "+size+"\nExecuted in: "+str(executionTime)+"ms")
            response = webhook.execute()
            return 0
        except:
            print("Invalid Discord Webhook")
    else:
        print("Product Not Found, Monitoring Again")
        return 1
        #Scraping the shopify site
    #end= time.time()
    
    #print("Task Exectuion Time = ",end-start,"ms")



