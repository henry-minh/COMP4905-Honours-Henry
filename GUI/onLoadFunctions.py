#Imports I actually Do Need
import json
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets

from PyQt6.QtCore import *

#Used for threading
from threading import Event

#Imports I dont think I need
#from time import sleep
#from threading import Thread
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
    self.profileTable.resizeColumnsToContents()    


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
    self.taskProxyGroupComboBox.clear()
    #Clear Task Table
    for i in range(self.taskTable.rowCount()-1,-1,-1):
        self.taskTable.removeRow(i)

    #Clear Task Checkboxes
    for i in range(0,len(self.profileCheckboxes)):
        self.profileSelectionContainer.layout().removeWidget(self.profileCheckboxes[i])
    self.profileCheckboxes.clear()

    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()

    #Filling in the tables
    for i in range(0,len(data['info'])):
        addProfileCheckbox(self)    
        self.profileCheckboxes[i].setText(data['info'][i]['id'])

    for i in data['proxies']:
        self.taskProxyGroupComboBox.addItem(i['proxyGroupName'])

    for i in data['tasks']:
        keywords=""
        sizes=""
        rowPosition = self.taskTable.rowCount()
        self.taskTable.insertRow(rowPosition)
        self.taskTable.setItem(rowPosition,0,QTableWidgetItem(i['site']))
        for j in range (0,len(i['key'])):
            keywords+=i['key'][j]+","
        for j in range (0,len(i['neg'])):
            keywords+="-"+i['neg'][j]+","
        for j in range (0,len(i['size'])):
            sizes+=i['size'][j]+","

        keywords = keywords.rstrip(keywords[-1])
        sizes = sizes.rstrip(sizes[-1])

        self.taskTable.setItem(rowPosition,1,QTableWidgetItem(keywords))
        self.taskTable.setItem(rowPosition,2,QTableWidgetItem(sizes))
        self.taskTable.setItem(rowPosition,3,QTableWidgetItem(i['profile']))
        self.taskTable.setItem(rowPosition,4,QTableWidgetItem(i['proxyGroup']))        
        self.taskTable.setItem(rowPosition,5,QTableWidgetItem(i['delay']))

        self.taskTable.setItem(rowPosition,6,QTableWidgetItem('Stand By'))        
    f.close()      
    self.taskTable.resizeColumnsToContents()


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

#Only Runs once at the start
def loadVariablesInitial(self):
    self.profileCheckboxes = []
    # Used for threadnig testing
    self.counter = 0
    self.event = Event()
    self.threadList =[]
    self.taskStatusBacking=[]


##############################################
#    Task Page Supplementary Fucntions       #
############################################## 
def loadSettingPageInitial(self):
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()    
    self.webhookInput.setText(data['webhook'])


