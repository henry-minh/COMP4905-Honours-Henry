import json
import onLoadFunctions
from PyQt6.QtWidgets import *

##############################################
#            Create Proxy Button             #
############################################## 
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
            data['proxies'][i]['proxyList'].clear()
            for j in range (0,len(proxyListInput)):
                
                data['proxies'][i]['proxyList'].append(proxyListInput[j])

            #data['proxies'][i]['proxyList'].append({self.editProxyInput.toPlainText()
  
           
    if doesProxyGroupExist == False:
    
        print(proxyListInput)
        data['proxies'].append ({ 
            "proxyGroupName":self.proxyGroupInput.text(),
            "proxyList":proxyListInput
        })
    f=open('./GUI/settings.json',"w")
    json.dump(data, f, indent = 3)
    f.close()

    
    onLoadFunctions.loadTaskPageInitial(self)
    print("end create button")


##############################################
#             Proxy ComboBox                 #
############################################## 
def clickComboProxyBtn(self, event):
    print("proxy group combobox pressed")
    self.editProxyInput.clear()
    self.proxyGroupInput.setText(self.proxyListComboBox.currentText())
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()
    for i in range (0,len(data['proxies'])):
        if(data['proxies'][i]['proxyGroupName']==self.proxyGroupInput.text()):
            print("match")
            for j in range(0,len(data['proxies'][i]['proxyList'])):
                print(data['proxies'][i]['proxyList'][j])
                self.editProxyInput.insertPlainText(data['proxies'][i]['proxyList'][j])
                if(j!=len(data['proxies'][i]['proxyList'])-1):
                    self.editProxyInput.insertPlainText(",")


##############################################
#            Delete Proxy Button             #
############################################## 
def clickDeleteProxyBtn(self, event):
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()
    for i in range(0,len(data['proxies'])):
        if(data['proxies'][i].get("proxyGroupName")==self.proxyGroupInput.text()):
            del data['proxies'][i]
            break
    f=open('./GUI/settings.json',"w")
    json.dump(data, f,indent=3)
    f.close()
    onLoadFunctions.loadProxyPageInitial(self)
    onLoadFunctions.loadTaskPageInitial(self)