import json
import onLoadFunctions
from PyQt6.QtWidgets import *

##############################################
#            Start Task Button             #
############################################## 
def clickStartTaskBtn(self, event):
    print("Clicked Start Task Button")


##############################################
#             Stop Task Button               #
############################################## 
def clickStopTaskBtn(self, event):
    print("Clicked Stop Task Button")


##############################################
#            Delete Task Button              #
############################################## 
def clickDeleteTaskBtn(self, event):
    print("Clicked Delete Task Button")

    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()

    r = self.taskTable.currentRow()
    print(r)
    if r>=0:
        del data['tasks'][r]
        f=open('./GUI/settings.json',"w")
        json.dump(data, f,indent=3)
        f.close()      
        onLoadFunctions.loadTaskPageInitial(self)   


##############################################
#            Edit Task Button                #
############################################## 
def clickEditTaskBtn(self, event):
    print("Clicked Edit Task Button")
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()

    r = self.taskTable.currentRow()
    if r>=0:
        self.homePageInput.setText(data['tasks'][r]['site']) 
        self.specificProxyInput.setText(data['tasks'][r]['specificProxy'])
        self.delayInput.setText(data['tasks'][r]['delay'])

        # Very Lazy Way of edit updating size and keyword input (not good practice if I channge the table around)
        self.keyWordInput.setText(self.taskTable.item(r,1).text())
        self.sizeInput.setText(self.taskTable.item(r,2).text())
    for i in range(0,len(data['proxies'])):
        if (data['proxies'][i]['proxyGroupName']==self.taskTable.item(r,4).text()):
            self.taskProxyGroupComboBox.setCurrentIndex(i)

        

##############################################
#            Create Task Button              #
############################################## 
def clickCreateTaskBtn(self, event):
    print("Clicked Create Task Button")

    isValidTask=True
    profileSelected=False
    proxySelected=False
    taskValueList=[]
    #keyList=[]
    #sizeList=[]
    taskValueList.append(self.keyWordInput.toPlainText())
    taskValueList.append(self.homePageInput.text())
    taskValueList.append(self.sizeInput.text())
    taskValueList.append(self.delayInput.text())
    taskValueList.append(self.taskProxyGroupComboBox.currentText())

    for x in taskValueList:
        if x == "":
            isValidTask=False
            return
    
    for i in range(0,len(self.profileCheckboxes)):
        if(self.profileCheckboxes[i].isChecked()):
            profileSelected=True

    
    if(profileSelected==False ):
        return
    
    keyList = self.keyWordInput.toPlainText().split(',')

    sizeList=self.sizeInput.text().split(',')
    posKeyList=[]
    negKeyList=[]
    for i in range(0,len(keyList)):
        if(keyList[i][0]=="-"):
            negKeyList.append(keyList[i])
        else:
            posKeyList.append(keyList[i])



    f=open('./GUI/settings.json',"r")
    data=json.load(f)  
    f.close()

    for i in range(0,len(self.profileCheckboxes)):    
        if(self.profileCheckboxes[i].isChecked()):

            data['tasks'].append ({
                "site": self.homePageInput.text(),
                "proxyGroup": self.taskProxyGroupComboBox.currentText(),
                "specificProxy": self.specificProxyInput.text(),
                "key": posKeyList,
                "neg": negKeyList,
                "size": sizeList,
                "profile": self.profileCheckboxes[i].text(),
                "delay": self.delayInput.text(),
            })
    f=open('./GUI/settings.json',"w")
    json.dump(data, f, indent = 3)
    f.close()        
    onLoadFunctions.loadTaskPageInitial(self)
    #Adding settings to tasks.json

