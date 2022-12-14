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

    #Error checking if no name is specified
    if self.proxyGroupInput.text()=="":
        return
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()

    #Check if the proxy group exists already
    for i in range (0,len(data['proxies'])):
        if(data['proxies'][i]['proxyGroupName']==self.proxyGroupInput.text()):
            doesProxyGroupExist=True
            data['proxies'][i]['proxyList'].clear()
            for j in range (0,len(proxyListInput)):     
                data['proxies'][i]['proxyList'].append(proxyListInput[j])

    #Proxy group DNE so we can append it to settins.json
    if doesProxyGroupExist == False:
        data['proxies'].append ({ 
            "proxyGroupName":self.proxyGroupInput.text(),
            "proxyList":proxyListInput
        })
    f=open('./GUI/settings.json',"w")
    json.dump(data, f, indent = 3)
    f.close()

    #Update UI
    onLoadFunctions.loadProxyPageInitial(self)
    onLoadFunctions.loadTaskPageInitial(self)


##############################################
#             Proxy ComboBox                 #
############################################## 
def clickComboProxyBtn(self, event):
    self.editProxyInput.clear()
    self.proxyGroupInput.setText(self.proxyListComboBox.currentText())
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()
    for i in range (0,len(data['proxies'])):
        if(data['proxies'][i]['proxyGroupName']==self.proxyGroupInput.text()):
            for j in range(0,len(data['proxies'][i]['proxyList'])):
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
            
            #Delete index in Backing Array & Close Running Threads if task is running
            if i in self.taskStatusBacking:
                self.threadList[i].stopTaskFunc()
                self.taskStatusBacking.pop(i)

            #If the task table shifted down in size, we need to adjust running tasks to prevent index out of bounds
            for j in range(len(self.taskStatusBacking)):
                if self.taskStatusBacking[i]>i:
                    self.threadList[i].taskDeletedAdjust()
            break

    f=open('./GUI/settings.json',"w")
    json.dump(data, f,indent=3)
    f.close()

    onLoadFunctions.loadProxyPageInitial(self)
    onLoadFunctions.loadTaskPageInitial(self)