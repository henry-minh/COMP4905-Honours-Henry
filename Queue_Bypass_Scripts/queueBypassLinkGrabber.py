import requests
from discord_webhook import DiscordWebhook
## queueBypassLinkGrabber

def getBypassLink():

    # Variables used for Veritfication
    bypassPidFound=False
    foundBypassPID = False     # foundBypassPID
    webLink="https://capsuletoronto.com/cart/"
    pageNum=0

    while foundBypassPID == False:
        #print("test")
        pageNum +=1
        url= "https://capsuletoronto.com/products.json?limit=250&page="
        url+=str(pageNum)
        r = requests.get(url)
        data = r.json()
        if sum(len(v) for v in data.values())==0:
            foundBypassPID=True
            break    
        # Webscraping
        for item in data ['products']:
            title=item['title']
            handle=item['handle']
            productType=item['product_type']
            #get URL for product if it matches keyword
            if foundBypassPID ==False:
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
                    
                    if (available==True):
                        print("success in if statement")
                        webLink+=str(itemId)+":1"
                        foundBypassPID=True
                        bypassPidFound=True
                        break
    if(bypassPidFound==True):
        #webhook = DiscordWebhook(url='https://discord.com/api/webhooks/985673989181567008/R9MJjtrJ7fwBibWU1fwk7hdx5NiiMC2mx6NmEBY6s_uP9uM2B9fAdyIG6MWOjw0dagLi', content="Queue Bypsass Test \nCheckout Link: "+webLink)
        #response = webhook.execute()
        return webLink
    else:
        return "error"
getBypassLink()




