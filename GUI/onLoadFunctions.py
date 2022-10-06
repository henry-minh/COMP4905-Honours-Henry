import json
from PyQt6.QtWidgets import *

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