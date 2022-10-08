from PyQt6 import uic,  QtCore
import sys, os
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets
import interface
import json
import profileFunctions,proxyFunctions,onLoadFunctions,taskFunctions
class page(QMainWindow):
    def __init__(self):
        #Load interface UI file & Hide Default TaskBar
        super().__init__()
        uic.loadUi("./GUI/interface7.ui",self)
        self.setWindowTitle("bar hide")
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
#self.checkboxes = []

##############################################
#         On Load Function Invoctions        #
##############################################
        onLoadFunctions.loadVariablesInitial(self)
        onLoadFunctions.loadProfileTableInitial(self)
        onLoadFunctions.loadProxyPageInitial(self)
        onLoadFunctions.loadTaskPageInitial(self)


##############################################
#                 connects                   #
##############################################    
        # TaskBar Functions Connect    
        self.closeBtn.clicked.connect(self.clickClose)   
        self.restoreBtn.clicked.connect(self.clickMaximize)    
        self.minimizeBtn.clicked.connect(self.clickMinimize)     

        # Tab Functionality
        self.tasksBtn.clicked.connect(self.clickTasksTab)     
        self.proxiesBtn.clicked.connect(self.clickProxiesTab)     
        self.profilesBtn.clicked.connect(self.clickProfilesTab)     
        self.captchasBtn.clicked.connect(self.clickCaptchasTab)     
        self.settingsBtn.clicked.connect(self.clickSettingsTab)   
        self.notificationCloseBtn.clicked.connect(self.clickNotificationCloseBtn)   
        self.hidden=False

        #Profile Page Buttons
        self.extraCreateProfileBtn.clicked.connect(self.clickCreateProfileBtn)
        self.deleteProfileBtn.clicked.connect(self.clickDeleteProfileBtn)
        self.extraClearBtn.clicked.connect(self.clickClearProfileBtn)
        self.editProfileBtn.clicked.connect(self.clickEditProfileBtn)

        #Proxy Page Buttons
        self.proxyCreateUpdateBtn.clicked.connect(self.clickCreateProxyBtn)
        self.proxyDeleteBtn.clicked.connect(self.clickDeleteProxyBtn)
        self.proxyListComboBox.currentTextChanged.connect(self.clickComboProxyBtn)

        #Task Page Buttons
        self.taskPageStartBtn.clicked.connect(self.clickStartTaskBtn)
        self.taskPageStopBtn.clicked.connect(self.clickStopTaskBtn)
        self.taskPageDeleteBtn.clicked.connect(self.clickDeleteTaskBtn)
        self.taskPageEditBtn.clicked.connect(self.clickEditTaskBtn)
        self.createTaskBtn.clicked.connect(self.clickCreateTaskBtn)

##############################################
#     Minimize Maximize Clse Window          #
##############################################
# TaskBar Functions  
    def clickClose(self,event):
        print ("closed application")
        self.close()
    def clickMaximize(self,event):
        print ("maximize")
        self.showMaximized()
    def clickMinimize(self,event):
        print ("minimize")
        self.showMinimized()


#######################################
#       Drag Window Functions         #
#######################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


#######################################
#       Change Tab Functions          #
#######################################
    def clickTasksTab(self, event):
        self.stackedMainMenu.setCurrentIndex(0)
        self.stackedCenterMenuSub.setCurrentIndex(0)
        self.centerMenuContainer.show()
        self.hidden=False;        
    def clickProxiesTab(self, event):
        self.stackedMainMenu.setCurrentIndex(1)
        self.stackedCenterMenuSub.setCurrentIndex(1)
        self.centerMenuContainer.hide()
        self.hidden=True 
    def clickProfilesTab(self, event):
        self.stackedMainMenu.setCurrentIndex(2)
        self.stackedCenterMenuSub.setCurrentIndex(2)
        self.centerMenuContainer.show()
        self.hidden=False;     
    def clickCaptchasTab(self, event):
        self.stackedMainMenu.setCurrentIndex(3)
        self.centerMenuContainer.hide()
        self.hidden=True
    def clickSettingsTab(self, event):
        self.stackedMainMenu.setCurrentIndex(4)
        self.centerMenuContainer.hide()
        self.hidden=True


#######################################
#       Notification Functions        #
#######################################
    def clickNotificationCloseBtn(self, event):
        self.popupNotificationContainer.hide()
        self.hidden=True;    


#######################################
#       Profile Page Functions        #
#######################################
    def clickDeleteProfileBtn(self, text):
        profileFunctions.clickDeleteProfileBtn(self, text)

    def clickCreateProfileBtn(self, text):
        profileFunctions.clickCreateProfileBtn(self, text)            

    def clickClearProfileBtn(self, text):
        profileFunctions.clickClearProfileBtn(self, text)    

    def clickEditProfileBtn(self, text):
        profileFunctions.clickEditProfileBtn(self, text)


#######################################
#       Proxy Page Functions          #
#######################################
    def clickCreateProxyBtn(self, text):
        proxyFunctions.clickCreateProxyBtn(self, text)

    def clickDeleteProxyBtn(self, text):
        proxyFunctions.clickDeleteProxyBtn(self, text)            

    def clickComboProxyBtn(self, text):
        proxyFunctions.clickComboProxyBtn(self, text) 


#######################################
#        Task Page Functions          #
#######################################
    def clickStartTaskBtn(self, text):
        taskFunctions.clickStartTaskBtn(self, text)

    def clickStopTaskBtn(self, text):
        taskFunctions.clickStopTaskBtn(self, text)            

    def clickDeleteTaskBtn(self, text):
        taskFunctions.clickDeleteTaskBtn(self, text) 

    def clickEditTaskBtn(self, text):
        taskFunctions.clickEditTaskBtn(self, text)

    def clickCreateTaskBtn(self, text):
        taskFunctions.clickCreateTaskBtn(self, text)  

#######################################
#         Launch Application          #
#######################################

app = QApplication(sys.argv)
window = page()
window.show()
sys.exit(app.exec())
