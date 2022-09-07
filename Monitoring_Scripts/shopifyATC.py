#pip install pandas
import requests
import pandas as pd
from discord_webhook import DiscordWebhook
## shopifyATC
#   WebScrapes Desired Shopify website's products.json (Currently Just works on Deadstock)
#   Uses Keywords and desired Sizes to find an in strock TRUE product
#   Grabs The ID and creates a checkout link
#   Opens a Browser using the ATC Link and attempts to checkout up until the last step.

## Variables
url= "https://www.deadstock.ca/products.json?limit=1000"
keywords =["yeezy","sulfur"]
randomFlag =False
sizeInput=["7","7.5","8","9"]
r = requests.get(url)
data = r.json()
webLink="https://www.deadstock.ca/cart/"
productFoundBool=False
validCartId = False
checkoutSize =0

productList = []    #full product list that gets put in excel
# converting user key words to lower  case
for i in range (len(keywords)):
    keywords[i]=keywords[i].lower()


# Webscraping
for item in data ['products']:
    title=item['title']
    handle=item['handle']
    productType=item['product_type']
    keywordCheckBool =True;

    if productType=="Footwear":
    #get URL for product if it matches keyword
        if productFoundBool==False:
            for productKey in keywords:
                if productKey[0]!="-":
                    if not productKey in handle.lower():
                        keywordCheckBool =False;
                else: 
                    if productKey in handle.lower():
                        keywordCheckBool =False;
                        # Found Matching Item. Now gets Info on all sizes                
            if keywordCheckBool ==True:
                for variant in item ["variants"]:
                    itemId = variant['id']
                    price = variant['price']
                    sku = variant ['sku']
                    available = variant ['available']
                    size = variant ['option2']
                    product = {
                    'title': title,
                    'item id': itemId,
                    'productType': productType,
                    'handle': handle,
                    'size': size,
                    'sku': sku,
                    'price': price,
                    'available': available
                    }
                    productList.append(product)
                    if (available==True and validCartId==False and size in sizeInput):
                        webLink+=str(itemId)+":1"
                        validCartId=True
                        checkoutSize=size
                productFoundBool=True

# save data frame and export to csv file
df = pd.DataFrame(productList)
try:
    df.to_csv('testScrape.csv')
    print('saved to file successfully')
except:
    print('Failed To Save File')
print(webLink)

if(validCartId==True):
    #content='Succesfully Found Product: \n keywords: '+keywords+"sizes entered: "+ sizeInput +"\n Size Checked out: "+checkoutSize+"\n Link: "+webLink
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/985673989181567008/R9MJjtrJ7fwBibWU1fwk7hdx5NiiMC2mx6NmEBY6s_uP9uM2B9fAdyIG6MWOjw0dagLi', content="Success \nCheckout Link: "+webLink)
    response = webhook.execute()
#open browser on product page:
#webbrowser.open(webLink)
