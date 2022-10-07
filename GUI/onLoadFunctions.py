import json
from PyQt6.QtWidgets import *
##############################################
#        Onload Profile Table                #
############################################## 
def loadProfileTableInitial(self):
    #Update Table
    for i in range(self.profileTable.rowCount()-1,-1,-1):
        self.profileTable.removeRow(i)
    f=open('./GUI/settings.json',"r")
    data=json.load(f)  
    for i in data['info']:
        rowPosition = self.profileTable.rowCount()
        self.profileTable.insertRow(rowPosition)

        self.profileTable.setItem(rowPosition,0,QTableWidgetItem(i['id']))
        self.profileTable.setItem(rowPosition,1,QTableWidgetItem(i['pCardNumber']))
        self.profileTable.setItem(rowPosition,2,QTableWidgetItem(i['pFirstName']+" "+i['pLastName']))
        self.profileTable.setItem(rowPosition,3,QTableWidgetItem(i['pMonth']+"/"+i['pYear']))
        self.profileTable.setItem(rowPosition,4,QTableWidgetItem(i['pCCV']))        
    f.close()      
##############################################
#        Onload Proxy Group ComboBox         #
############################################## 
def loadProxyPageInitial(self):
    
    self.proxyListComboBox.clear()
    self.proxyGroupInput.clear()
    f=open('./GUI/settings.json',"r")
    data=json.load(f)  
    for i in data['proxies']:
        self.proxyListComboBox.addItem(i['proxyGroupName'])
    f.close()     

##############################################
#        Onload Task Creation Page           #
############################################## 
def loadTaskPageInitial(self):
    print("Load Task Page Initial")