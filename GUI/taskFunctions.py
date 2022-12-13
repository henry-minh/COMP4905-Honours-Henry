import json
import onLoadFunctions
from PyQt6.QtWidgets import *


##############################################
#            Delete Task Button              #
############################################## 
def clickDeleteTaskBtn(self, event):
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()

    r = self.taskTable.currentRow()
    if r>=0:
        del data['tasks'][r]
        f=open('./GUI/settings.json',"w")
        json.dump(data, f,indent=3)
        f.close()      
            
        #Delete index in Backing Array and thread array
        #print("before stoping thread and popping index from backing array")
        #print(self.taskStatusBacking)
        for j in range(len(self.taskStatusBacking)):
            if self.taskStatusBacking[j]==r:
                self.threadList[j].stopTaskFunc()
                self.threadList.pop(j)   
                self.taskStatusBacking.pop(j)
                break
        #print("after stoping thread and popping index from backing array")    
        #print(self.taskStatusBacking)

        #print("before shifting backing array for out of bound")
        #If the task table shifted down in size, we need to adjust running tasks to prevent index out of bounds
        for j in range(len(self.taskStatusBacking)):
            if self.taskStatusBacking[j]>r:
                self.threadList[j].taskDeletedAdjust()
                self.taskStatusBacking[j]=self.taskStatusBacking[j]-1
        #print("after shifting backing array for out of bound")
        #print(self.taskStatusBacking)

        onLoadFunctions.loadTaskPageInitial(self)   


##############################################
#            Edit Task Button                #
############################################## 
def clickEditTaskBtn(self, event):
    f=open('./GUI/settings.json',"r")
    data=json.load(f)
    f.close()

    r = self.taskTable.currentRow()
    if r>=0:
        self.homePageInput.setText(data['tasks'][r]['site']) 
        self.specificProxyInput.setText(data['tasks'][r]['specificProxy'])
        self.delayInput.setText(data['tasks'][r]['delay'])

        # Very Lazy Way of updating size and keyword input (not good practice if I channge the table around)
        self.keyWordInput.setText(self.taskTable.item(r,1).text())
        self.sizeInput.setText(self.taskTable.item(r,2).text())
        for i in range(0,len(data['proxies'])):
            if (data['proxies'][i]['proxyGroupName']==self.taskTable.item(r,4).text()):
                self.taskProxyGroupComboBox.setCurrentIndex(i)


##############################################
#            Create Task Button              #
############################################## 
def clickCreateTaskBtn(self, event):
    #isValidTask=True
    profileSelected=False
    #proxySelected=False
    taskValueList=[]
    taskValueList.append(self.keyWordInput.toPlainText())
    taskValueList.append(self.homePageInput.text())
    taskValueList.append(self.sizeInput.text())
    taskValueList.append(self.delayInput.text())
    taskValueList.append(self.taskProxyGroupComboBox.currentText())

    #Error check if a task is even selected
    for x in taskValueList:
        if x == "":
            #isValidTask=False
            return
    
    for i in range(0,len(self.profileCheckboxes)):
        if(self.profileCheckboxes[i].isChecked()):
            profileSelected=True
    if(profileSelected==False ):
        return
    
    #Retieve Keywords (poitive and negative)
    keyList = self.keyWordInput.toPlainText().split(',')
    sizeList=self.sizeInput.text().split(',')
    posKeyList=[]
    negKeyList=[]
    for i in range(0,len(keyList)):
        if(keyList[i][0]=="-"):
            negKeyList.append(keyList[i][1:])
        else:
            posKeyList.append(keyList[i])

    f=open('./GUI/settings.json',"r")
    data=json.load(f)  
    f.close()

    #Retrieves the rest the info needed for task creation
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

