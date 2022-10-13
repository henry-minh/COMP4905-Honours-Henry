import json
import onLoadFunctions
import requests
import time
from PyQt6.QtWidgets import *
from discord_webhook import DiscordWebhook
##############################################
#            Start Task Button             #
############################################## 
def clickStartTaskBtn(self, event):
    start= time.time()

    rowSelected = self.taskTable.currentRow()

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
       
        try:
            webhook = DiscordWebhook(url=self.webhookInput.text(), content="Successful Cart Creation: "+webCartLink+"\nProduct: "+cartedProductName+"\nsize: "+size+"\nExecuted in: "+str(executionTime)+"ms")
            response = webhook.execute()
        except:
            print("Invalid Discord Webhook")

        #Scraping the shopify site
    #end= time.time()
    self.taskTable.setItem(rowSelected,5,QTableWidgetItem('Stand By'))
    #print("Task Exectuion Time = ",end-start,"ms")


##############################################
#             Stop Task Button               #
############################################## 
def clickStopTaskBtn(self, event):
    print("Clicked Stop Task Button")
