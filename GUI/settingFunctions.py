import json
from PyQt6.QtWidgets import *
from discord_webhook import DiscordWebhook


def clickWebHookBtn(self, event):
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()    
    data['webhook']=self.webhookInput.text()
    f=open('./GUI/settings.json',"w")
    json.dump(data, f, indent = 3)
    f.close()
    try:
        webhook = DiscordWebhook(url=self.webhookInput.text(), content="WebHook Test Successful")
        response = webhook.execute()
    except:
        print("Invalid Discord Webhook")

