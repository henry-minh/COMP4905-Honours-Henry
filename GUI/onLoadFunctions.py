import json
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets

##############################################
#        Onload Profile Page Table           #
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

    #String variables for keywords and sizes
    keywords=""
    sizes=""

    #Clear Task Table
    for i in range(self.taskTable.rowCount()-1,-1,-1):
        self.taskTable.removeRow(i)

    #Clear Task Checkboxes
    for i in range(0,len(self.profileCheckboxes)):
        self.profileSelectionContainer.layout().removeWidget(self.profileCheckboxes[i])
    for i in range(0,len(self.proxyCheckboxes)):
        self.proxySelectionContainer.layout().removeWidget(self.proxyCheckboxes[i])
    self.profileCheckboxes.clear()
    self.proxyCheckboxes.clear()

    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()

    #Filling in the tables
    for i in range(0,len(data['info'])):
        addProfileCheckbox(self)    
        self.profileCheckboxes[i].setText(data['info'][i]['id'])
    for i in range(0,len(data['proxies'])):
        addProxyCheckbox(self)    
        self.proxyCheckboxes[i].setText(data['proxies'][i]['proxyGroupName'])

    for i in data['tasks']:
        rowPosition = self.taskTable.rowCount()
        self.taskTable.insertRow(rowPosition)
        self.taskTable.setItem(rowPosition,0,QTableWidgetItem(i['site']))
        for j in range (0,len(i['key'])):
            keywords+=i['key'][j]+","
        for j in range (0,len(i['neg'])):
            keywords+=i['size'][j]+","
        for j in range (0,len(i['size'])):
            sizes+=i['size'][j]+","
        keywords = keywords.rstrip(keywords[-1])
        sizes = sizes.rstrip(sizes[-1])
        self.taskTable.setItem(rowPosition,1,QTableWidgetItem(keywords))
        self.taskTable.setItem(rowPosition,2,QTableWidgetItem(sizes))
        self.taskTable.setItem(rowPosition,3,QTableWidgetItem(i['profile']))
        self.taskTable.setItem(rowPosition,4,QTableWidgetItem(i['proxyGroup']))
        self.taskTable.setItem(rowPosition,5,QTableWidgetItem('Stand By'))        
    f.close()      

##############################################
#    Task Page Supplementary Fucntions       #
############################################## 

def addProfileCheckbox(self):
    checkbox = QtWidgets.QCheckBox()
    self.profileCheckboxes.append(checkbox)
    self.profileSelectionContainer.layout().addWidget(checkbox)

def addProxyCheckbox(self):
    checkbox = QtWidgets.QCheckBox()
    self.proxyCheckboxes.append(checkbox)
    self.proxySelectionContainer.layout().addWidget(checkbox)

def loadVariablesInitial(self):
    self.profileCheckboxes = []
    self.proxyCheckboxes = []