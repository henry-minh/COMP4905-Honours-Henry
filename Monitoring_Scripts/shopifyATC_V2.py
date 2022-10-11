#pip install pandas
import requests

import pandas as pd
from discord_webhook import DiscordWebhook
## shopifyATC
#   WebScrapes Desired Shopify website's products.json (Currently just works on Deadstock)
#   Uses Keywords and desired Sizes to find an in strock TRUE product
#   Grabs The ID and creates a checkout link
#   Opens a Browser using the ATC Link and attempts to checkout up until the last step.

# To do List
# 1. implement random keyword functionality
# 2. research how to improve speed


## Product Specification Parameters
keywords =["adidas","-terrex","-qntm"]
randomFlag =False
sizeInput=["7","7.5","8","9"]
# converting user key words to lower  case
for i in range (len(keywords)):
    keywords[i]=keywords[i].lower()

# Variables used for Veritfication

validCartId = False
itemDNE = False     # DNE => Does not Exist
checkoutSize =0

productList = []    #full product list that gets put in excel
webLink="https://www.deadstock.com/cart/"

size=""
#if product not found and json isnt empty Loop through other 5 pages
## Variables used for monitoring
pageNum=0

while itemDNE == False:
    print("test")
    pageNum +=1
    url= "https://deadstock.ca/products.json?limit=1000&page="
    url+=str(pageNum)
    r = requests.get(url)
    data = r.json()
    if sum(len(v) for v in data.values())==0:
        itemDNE=True
        break
    #else Enter Delay and repeat (or we can just end the program temporarily)
    # Webscraping
    for item in data ['products']:
        title=item['title']
        handle=item['handle']
        productType=item['product_type']
        keywordCheckBool =True;

        if productType=="Footwear":
        #get URL for product if it matches keyword
        
            for productKey in keywords:
                if productKey[0]!="-":
                    if not productKey in handle.lower():
                        keywordCheckBool =False;
                        print("False Check 1")
                else: 
                    if productKey in handle.lower():
                        keywordCheckBool =False;
                        print("False Check 2")
            # Found Matching Item. Now gets Info on all sizes                
            if keywordCheckBool ==True:
                print("Pass Check" +handle)
                
                for variant in item ["variants"]:
                    itemId = variant['id']
                    price = variant['price']
                    sku = variant ['sku']
                    available = variant ['available']
                    if variant ['option1'] in sizeInput:
                        size=variant ['option1']
                    if variant ['option2'] in sizeInput:
                        size=variant ['option2']
                    if variant ['option3'] in sizeInput:
                        size=variant ['option3']
                    #size = variant ['option1']

                    if (available==True and validCartId==False and size in sizeInput):
                        webLink+=str(itemId)+":1"
                        validCartId=True
                        checkoutSize=size
                        break
                
                itemDNE = True
            


if(validCartId==True):
    #content='Succesfully Found Product: \n keywords: '+keywords+"sizes entered: "+ sizeInput +"\n Size Checked out: "+checkoutSize+"\n Link: "+webLink
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/985673989181567008/R9MJjtrJ7fwBibWU1fwk7hdx5NiiMC2mx6NmEBY6s_uP9uM2B9fAdyIG6MWOjw0dagLi', content="Success \nCheckout Link: "+webLink)
    response = webhook.execute()
#open browser on product page:
#webbrowser.open(webLink)


# save data frame and export to csv file
"""
df = pd.DataFrame(productList)
try:
    df.to_csv('testScrape.csv')
    print('saved to file successfully')
except:
    print('Failed To Save File')
print(webLink)
"""

