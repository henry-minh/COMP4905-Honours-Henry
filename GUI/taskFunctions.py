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


##############################################
#            Create Task Button              #
############################################## 
def clickCreateTaskBtn(self, event):
    print("Clicked Create Task Button")