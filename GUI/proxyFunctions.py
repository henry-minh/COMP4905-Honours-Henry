import json
import onLoadFunctions
from PyQt6.QtWidgets import *

# create/update
def clickCreateProxyBtn(self, event):
    doesProxyGroupExist = False
    proxyListInput = []
    proxyListInput=self.editProxyInput.toPlainText().split(',')
    print(proxyListInput)
    print("proxy group create button pressed")
    #base case, no name specified
    if self.proxyGroupInput.text()=="":
        return
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()
    for i in range (0,len(data['proxies'])):
        if(data['proxies'][i]['proxyGroupName']==self.proxyGroupInput.text()):
            doesProxyGroupExist=True
            
            for j in range (0,len(proxyListInput)):
                data['proxies'][i]['proxyList'].append(proxyListInput[i]

            #data['proxies'][i]['proxyList'].append({self.editProxyInput.toPlainText()
  
            )
    if doesProxyGroupExist == False:
        data['proxies'].append ({ 
            "proxyGroupName":self.proxyGroupInput.text(),
            "proxyList":proxyListInput
        })
    f=open('./GUI/settings.json',"w")
    json.dump(data, f, indent = 3)
    f.close()
    print("end create button")
# delete
def clickDeleteProxyBtn(self, event):
    print("proxy group delete button pressed")
# proxy combo box
def clickComboProxyBtn(self, event):
    print("proxy group combobox pressed")