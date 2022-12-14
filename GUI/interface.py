# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets, QtSvg
import resourceCompiler
def clickClose():
    print ("closed")
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 599)
        MainWindow.setStyleSheet("*{\n"
"    border:none;\n"
"    background-color: transparent;\n"
"    background:transparent;\n"
"    margin:0;\n"
"    padding:0;\n"
"    color: white;\n"
"\n"
"}\n"
"#centralwidget{\n"
"    background-color: #1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"    background-color: #16191d;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer{\n"
"    background-color: #2c313c;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"    text-align:left;\n"
"    padding: 2px 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"    background-color: #052F89;\n"
"}\n"
"\n"
"#frame_4, #frame_8, #popupNotificationSubContainer{\n"
"    background-color:#16191d;\n"
"    border-radius:10px;\n"
"}\n"
"#stackedWidget{\n"
"    background: #052F89;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QtWidgets.QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leftMenuSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuBtn = QtWidgets.QPushButton(self.frame)
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/feather/align-justify.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.homeBtn = QtWidgets.QPushButton(self.frame_2)
        self.homeBtn.setStyleSheet("background-color: #1f232a;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/feather/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(24, 24))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_3.addWidget(self.homeBtn)
        self.dataBtn = QtWidgets.QPushButton(self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/feather/menu.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QtCore.QSize(24, 24))
        self.dataBtn.setObjectName("dataBtn")
        self.verticalLayout_3.addWidget(self.dataBtn)
        self.reportBtn = QtWidgets.QPushButton(self.frame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/feather/printer.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.reportBtn.setIcon(icon3)
        self.reportBtn.setIconSize(QtCore.QSize(24, 24))
        self.reportBtn.setObjectName("reportBtn")
        self.verticalLayout_3.addWidget(self.reportBtn)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingdBtn = QtWidgets.QPushButton(self.frame_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/feather/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settingdBtn.setIcon(icon4)
        self.settingdBtn.setIconSize(QtCore.QSize(24, 24))
        self.settingdBtn.setObjectName("settingdBtn")
        self.verticalLayout_4.addWidget(self.settingdBtn)
        self.infoBtn = QtWidgets.QPushButton(self.frame_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/feather/info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QtCore.QSize(24, 24))
        self.infoBtn.setObjectName("infoBtn")
        self.verticalLayout_4.addWidget(self.infoBtn)
        self.helpBtn = QtWidgets.QPushButton(self.frame_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/feather/help-circle.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QtCore.QSize(24, 24))
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout_4.addWidget(self.helpBtn)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.centerMenuContainer = QtWidgets.QWidget(self.centralwidget)
        self.centerMenuContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.centerMenuContainer.setObjectName("centerMenuContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.centerMenuSubContainer = QtWidgets.QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.centerMenuSubContainer.setObjectName("centerMenuSubContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.centerMenuSubContainer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_ = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_.setFont(font)
        self.label_.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_.setObjectName("label_")
        self.horizontalLayout_4.addWidget(self.label_)
        self.pushButton_ = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/feather/x-circle.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_.setIcon(icon7)
        self.pushButton_.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_.setObjectName("pushButton_")
        self.horizontalLayout_4.addWidget(self.pushButton_, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_4, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centerMenuSubContainer)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_3)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_5)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.centerMenuContainer)
        self.mainBodyContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet("")
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.headerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName("headerContainer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.headerContainer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setMaximumSize(QtCore.QSize(30, 30))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/feather/moomin.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.frame_5, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.frame_6 = QtWidgets.QFrame(self.headerContainer)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_6.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/feather/more-horizontal.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_5.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/feather/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon9)
        self.pushButton_5.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.horizontalLayout_5.addWidget(self.frame_6, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.headerContainer)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/feather/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_4.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/feather/square.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon11)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_3.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/feather/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon12)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_3.clicked.connect(clickClose)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_10.addWidget(self.headerContainer, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.mainBodyConent = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyConent.sizePolicy().hasHeightForWidth())
        self.mainBodyConent.setSizePolicy(sizePolicy)
        self.mainBodyConent.setObjectName("mainBodyConent")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.mainBodyConent)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.mainContentsContainer = QtWidgets.QWidget(self.mainBodyConent)
        self.mainContentsContainer.setObjectName("mainContentsContainer")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.mainContentsContainer)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_10 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_16.addWidget(self.label_10)
        self.stackedWidget_3.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_11 = QtWidgets.QLabel(self.page_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_18.addWidget(self.label_11)
        self.stackedWidget_3.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_12 = QtWidgets.QLabel(self.page_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_17.addWidget(self.label_12)
        self.stackedWidget_3.addWidget(self.page_8)
        self.verticalLayout_15.addWidget(self.stackedWidget_3)
        self.horizontalLayout_9.addWidget(self.mainContentsContainer)
        self.rightMenuContainer = QtWidgets.QWidget(self.mainBodyConent)
        self.rightMenuContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.rightMenuContainer.setObjectName("rightMenuContainer")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.rightMenuSubContainer = QtWidgets.QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.rightMenuSubContainer.setObjectName("rightMenuSubContainer")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_8 = QtWidgets.QFrame(self.rightMenuSubContainer)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_10.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_12.addWidget(self.frame_8)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.rightMenuSubContainer)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8)
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_14.addWidget(self.label_9)
        self.stackedWidget_2.addWidget(self.page_2)
        self.verticalLayout_12.addWidget(self.stackedWidget_2)
        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)
        self.horizontalLayout_9.addWidget(self.rightMenuContainer, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_10.addWidget(self.mainBodyConent)
        self.popupNotificationContainer = QtWidgets.QWidget(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName("popupNotificationContainer")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.popupNotificationSubContainer = QtWidgets.QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName("popupNotificationSubContainer")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_14 = QtWidgets.QLabel(self.popupNotificationSubContainer)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_20.addWidget(self.label_14)
        self.frame_9 = QtWidgets.QFrame(self.popupNotificationSubContainer)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_8.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/feather/x-octagon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_8.setIcon(icon13)
        self.pushButton_8.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_11.addWidget(self.pushButton_8, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_20.addWidget(self.frame_9)
        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)
        self.verticalLayout_10.addWidget(self.popupNotificationContainer)
        self.footerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName("footerContainer")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.footerContainer)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_10 = QtWidgets.QFrame(self.footerContainer)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_15 = QtWidgets.QLabel(self.frame_10)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.horizontalLayout_12.addWidget(self.frame_10)
        self.sizeGrip = QtWidgets.QFrame(self.footerContainer)
        self.sizeGrip.setMinimumSize(QtCore.QSize(10, 10))
        self.sizeGrip.setMaximumSize(QtCore.QSize(40, 40))
        self.sizeGrip.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sizeGrip.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sizeGrip.setObjectName("sizeGrip")
        self.horizontalLayout_12.addWidget(self.sizeGrip)
        self.verticalLayout_10.addWidget(self.footerContainer)
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuBtn.setToolTip(_translate("MainWindow", "Menu"))
        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "Home"))
        self.dataBtn.setToolTip(_translate("MainWindow", "Dats Analysis"))
        self.dataBtn.setText(_translate("MainWindow", "Data Analysis"))
        self.reportBtn.setToolTip(_translate("MainWindow", "View Reports"))
        self.reportBtn.setText(_translate("MainWindow", "Reports"))
        self.settingdBtn.setToolTip(_translate("MainWindow", "Go to Settings"))
        self.settingdBtn.setText(_translate("MainWindow", "Settings"))
        self.infoBtn.setToolTip(_translate("MainWindow", "Information about the App"))
        self.infoBtn.setText(_translate("MainWindow", "Information"))
        self.helpBtn.setToolTip(_translate("MainWindow", "Get More Help"))
        self.helpBtn.setText(_translate("MainWindow", "Help"))
        self.label_.setText(_translate("MainWindow", "More Menu"))
        self.pushButton_.setToolTip(_translate("MainWindow", "Close Menu"))
        self.label_2.setText(_translate("MainWindow", "Settings"))
        self.label_4.setText(_translate("MainWindow", "Help"))
        self.label_3.setText(_translate("MainWindow", "Information"))
        self.label_6.setText(_translate("MainWindow", "Title"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "More"))
        self.pushButton_5.setToolTip(_translate("MainWindow", "Profile"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Minimize Window"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Restore Window"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Close Window"))
        self.label_10.setText(_translate("MainWindow", "Home"))
        self.label_11.setText(_translate("MainWindow", "Data Analysis"))
        self.label_12.setText(_translate("MainWindow", "Reports"))
        self.label_7.setText(_translate("MainWindow", "Right Menu"))
        self.pushButton_7.setToolTip(_translate("MainWindow", "Close Menu"))
        self.label_8.setText(_translate("MainWindow", "Profile"))
        self.label_9.setText(_translate("MainWindow", "More..."))
        self.label_14.setText(_translate("MainWindow", "Notification"))
        self.label_13.setText(_translate("MainWindow", "Notification Message"))
        self.pushButton_8.setToolTip(_translate("MainWindow", "Close Notification"))
        self.label_15.setText(_translate("MainWindow", "Henry Nguyen Honours Project"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
