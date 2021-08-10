# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainScreen = QtWidgets.QLabel(self.centralwidget)
        self.MainScreen.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.MainScreen.setPixmap(QPixmap("./Images/Dashboard.jpg"))
        # self.MainScreen.setStyleSheet("image: url(:/newPrefix/Dashboard.jpg);")
        self.MainScreen.setText("")
        self.MainScreen.setObjectName("MainScreen")
        self.SideBarLabel = QtWidgets.QLabel(self.centralwidget)
        self.SideBarLabel.setGeometry(QtCore.QRect(-10, -15, 96, 795))
        self.SideBarLabel.setPixmap(QPixmap("./Images/Side Bar.jpg"))
        # self.SideBarLabel.setStyleSheet("image: url(:/newPrefix/Side Bar.jpg);")
        self.SideBarLabel.setText("")
        self.SideBarLabel.setObjectName("SideBarLabel")
        self.ProfilepushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProfilepushButton.setGeometry(QtCore.QRect(947, 15, 44, 44))
        self.ProfilepushButton.setIconSize(QSize(40, 40))
        self.ProfilepushButton.setIcon(QIcon("./Images/Path 206.png"))
        self.ProfilepushButton.setStyleSheet("#ProfilepushButton{\n"
"image: url(:/newPrefix/Path 206.png);\n"
"border: 1px solid #00A65A;\n"
"border-radius: 22px;\n"
"background-color: Transparent;\n"
"\n"
"\n"
"\n"
"\n"
"}")
        self.ProfilepushButton.setText("")
        self.ProfilepushButton.setObjectName("ProfilepushButton")
        self.UsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsernameLabel.setGeometry(QtCore.QRect(863, 30, 72, 14))
        self.UsernameLabel.setStyleSheet("#UsernameLabel{\n"
"font: 11px \"Montserrat\";\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"\n"
"\n"
"\n"
"}")
        # Asad Asad AsAD
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.MsgLabel = QtWidgets.QLabel(self.centralwidget)
        self.MsgLabel.setGeometry(QtCore.QRect(812, 27, 16, 20))
        self.MsgLabel.setPixmap(QPixmap("./Images/Icon feather-message-square.png"))
        # self.MsgLabel.setStyleSheet("image: url(:/newPrefix/Icon feather-message-square.png);")
        self.MsgLabel.setText("")
        self.MsgLabel.setObjectName("MsgLabel")
        self.NotiLabel = QtWidgets.QLabel(self.centralwidget)
        self.NotiLabel.setGeometry(QtCore.QRect(764, 27, 16, 20))
        self.NotiLabel.setPixmap(QPixmap("./Images/Icon ionic-ios-notifications-outline.png"))
        # self.NotiLabel.setStyleSheet("image: url(:/newPrefix/Icon ionic-ios-notifications-outline.png);")
        self.NotiLabel.setText("")
        self.NotiLabel.setObjectName("NotiLabel")
        self.DayandDate = QtWidgets.QLabel(self.centralwidget)
        self.DayandDate.setGeometry(QtCore.QRect(159, 37, 123, 19))
        self.DayandDate.setStyleSheet("#DayandDate{\n"
"font: 16px \"Montserrat\";\n"
"text-align: left;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"\n"
"\n"
"\n"
"}")
        self.DayandDate.setObjectName("DayandDate")
        self.Timelabel = QtWidgets.QLabel(self.centralwidget)
        self.Timelabel.setGeometry(QtCore.QRect(159, 52, 115, 52))
        self.Timelabel.setStyleSheet("#Timelabel{\n"
"text-align: left;\n"
"letter-spacing: NaNpx;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"font: 28px \"Montserrat\";\n"
"\n"
"\n"
"}")
        self.Timelabel.setObjectName("Timelabel")
        self.DashboarLabel = QtWidgets.QLabel(self.centralwidget)
        self.DashboarLabel.setGeometry(QtCore.QRect(159, 155, 150, 27))
        self.DashboarLabel.setStyleSheet("#DashboarLabel{\n"
"text-align: left;\n"
"font: 22px \"Montserrat\";\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"\n"
"\n"
"\n"
"\n"
"}")
        self.DashboarLabel.setObjectName("DashboarLabel")
        self.NumSIgnLanLabel = QtWidgets.QLabel(self.centralwidget)
        self.NumSIgnLanLabel.setGeometry(QtCore.QRect(159, 215, 162, 27))
        self.NumSIgnLanLabel.setStyleSheet("#NumSIgnLanLabel{\n"
"font: 11px \"Montserrat\";\n"
"text-align: left;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"opacity: 1;\n"
"\n"
"}")
        self.NumSIgnLanLabel.setObjectName("NumSIgnLanLabel")
        self.NumAudLanLabel = QtWidgets.QLabel(self.centralwidget)
        self.NumAudLanLabel.setGeometry(QtCore.QRect(583, 215, 123, 28))
        self.NumAudLanLabel.setStyleSheet("#NumAudLanLabel{\n"
"font: 11px \"Montserrat\";\n"
"text-align: left;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"opacity: 1;\n"
"\n"
"}")
        self.NumAudLanLabel.setObjectName("NumAudLanLabel")
        self.AvgSignLanLabel = QtWidgets.QLabel(self.centralwidget)
        self.AvgSignLanLabel.setGeometry(QtCore.QRect(583, 460, 154, 28))
        self.AvgSignLanLabel.setStyleSheet("#AvgSignLanLabel{\n"
"font: 11px \"Montserrat\";\n"
"text-align: left;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"opacity: 1;\n"
"\n"
"}")
        self.AvgSignLanLabel.setObjectName("AvgSignLanLabel")
        self.NumLabel = QtWidgets.QLabel(self.centralwidget)
        self.NumLabel.setGeometry(QtCore.QRect(247, 273, 181, 57))
        self.NumLabel.setStyleSheet("#NumLabel{\n"
"    font: 47px \"Montserrat\";\n"
"text-align: left;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"\n"
"\n"
"}")
        self.NumLabel.setObjectName("NumLabel")
        self.NumLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.NumLabel_2.setGeometry(QtCore.QRect(656, 273, 181, 57))
        self.NumLabel_2.setStyleSheet("#NumLabel_2{\n"
"font: 47px \"Montserrat\";\n"
"text-align: left;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"\n"
"\n"
"}")
        self.NumLabel_2.setObjectName("NumLabel_2")
        self.GraphLabel = QtWidgets.QLabel(self.centralwidget)
        self.GraphLabel.setGeometry(QtCore.QRect(614, 498, 299, 130))
        self.GraphLabel.setPixmap(QPixmap("./Images/Graph.png"))
        # self.GraphLabel.setStyleSheet("image: url(:/newPrefix/Graph.png);")
        self.GraphLabel.setText("")
        self.GraphLabel.setObjectName("GraphLabel")
        self.ScrollBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ScrollBtn.setIconSize(QSize(15, 15))
        self.ScrollBtn.setIcon(QIcon("./Images/Icon awesome-greater-than.png"))
        self.ScrollBtn.setGeometry(QtCore.QRect(488, 214, 30, 30))
        self.ScrollBtn.setStyleSheet("#ScrollBtn{\n"
"    image: url(:/newPrefix/Icon awesome-greater-than.png);\n"
"\n"
"background-color: rgb(0, 104, 56);\n"
"color: rgb(40, 232, 144);\n"
"font: 17px \"Montserrat\";\n"
"border-radius:14px;\n"
"\n"
"}")
        self.ScrollBtn.setText("")
        self.ScrollBtn.setObjectName("ScrollBtn")
        self.ScrollBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ScrollBtn_2.setIconSize(QSize(15, 15))
        self.ScrollBtn_2.setIcon(QIcon("./Images/Icon awesome-greater-than.png"))
        self.ScrollBtn_2.setGeometry(QtCore.QRect(911, 213, 30, 30))
        self.ScrollBtn_2.setStyleSheet("#ScrollBtn_2{\n"
"    image: url(:/newPrefix/Icon awesome-greater-than.png);\n"
"\n"
"background-color: rgb(0, 104, 56);\n"
"color: rgb(40, 232, 144);\n"
"font: 17px \"Montserrat\";\n"
"border-radius:14px;\n"
"\n"
"}")
        self.ScrollBtn_2.setText("")
        self.ScrollBtn_2.setObjectName("ScrollBtn_2")
        self.DayLabel = QtWidgets.QLabel(self.centralwidget)
        self.DayLabel.setGeometry(QtCore.QRect(433, 219, 39, 14))
        self.DayLabel.setStyleSheet("#DayLabel{\n"
"text-align: left;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"font: 11px \"Montserrat\";\n"
"\n"
"\n"
"}")
        self.DayLabel.setObjectName("DayLabel")
        self.DayLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.DayLabel_2.setGeometry(QtCore.QRect(856, 220, 39, 14))
        self.DayLabel_2.setStyleSheet("#DayLabel_2{\n"
"text-align: left;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"font: 11px \"Montserrat\";\n"
"\n"
"\n"
"}")
        self.DayLabel_2.setObjectName("DayLabel_2")
        self.LineLabel = QtWidgets.QLabel(self.centralwidget)
        self.LineLabel.setGeometry(QtCore.QRect(195, 515, 130, 0))
        self.LineLabel.setStyleSheet("")
        self.LineLabel.setText("")
        self.LineLabel.setObjectName("LineLabel")
        self.ActiveUserCountlabel = QtWidgets.QLabel(self.centralwidget)
        self.ActiveUserCountlabel.setGeometry(QtCore.QRect(370, 503, 57, 73))
        self.ActiveUserCountlabel.setStyleSheet("#ActiveUserCountlabel{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 60px \"Montserrat\";\n"
"\n"
"\n"
"\n"
"}")
        self.ActiveUserCountlabel.setObjectName("ActiveUserCountlabel")
        self.ActiveUserlabel = QtWidgets.QLabel(self.centralwidget)
        self.ActiveUserlabel.setGeometry(QtCore.QRect(385, 566, 73, 13))
        self.ActiveUserlabel.setStyleSheet("#ActiveUserlabel{\n"
"\n"
"color:rgb(255, 255, 255);\n"
"font: 10px \"Montserrat\";\n"
"\n"
"\n"
"\n"
"}")
        self.ActiveUserlabel.setObjectName("ActiveUserlabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(445, 510, 18, 18))
        self.label.setPixmap(QPixmap("./Images/Group 269.png"))
        # self.label.setStyleSheet("image: url(:/newPrefix/Group 269.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.SeeAllBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SeeAllBtn.setGeometry(QtCore.QRect(435, 605, 76, 22))
        self.SeeAllBtn.setStyleSheet("#SeeAllBtn{\n"
"border-radius: 5px;\n"
"opacity: 1;\n"
"font: 10px \"Montserrat\";\n"
"color: rgb(16, 106, 56);\n"
"background-color: rgb(40, 232, 144);\n"
"\n"
"\n"
"}")
        self.SeeAllBtn.setObjectName("SeeAllBtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(339, 478, 3, 148))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.scrollAreaActiveUser = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaActiveUser.setGeometry(QtCore.QRect(161, 476, 164, 152))
        self.scrollAreaActiveUser.setStyleSheet("")
        self.scrollAreaActiveUser.setWidgetResizable(True)
        self.scrollAreaActiveUser.setObjectName("scrollAreaActiveUser")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 162, 150))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaActiveUser.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(17, 262, 54, 30))
        self.label_2.setPixmap(QPixmap("./Images/Group 308.png"))
        # self.label_2.setStyleSheet("image: url(:/newPrefix/Group 308.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(17, 330, 56, 35))
        self.label_3.setPixmap(QPixmap("./Images/Group 309.png"))
        # self.label_3.setStyleSheet("image: url(:/newPrefix/Group 309.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 403, 68, 36))
        self.label_4.setPixmap(QPixmap("./Images/Group 310.png"))
        # self.label_4.setStyleSheet("image: url(:/newPrefix/Group 310.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(24, 477, 40, 33))
        self.label_5.setPixmap(QPixmap("./Images/Group 311.png"))
        # self.label_5.setStyleSheet("background-image: url(:/newPrefix/Group 311.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UsernameLabel.setText(_translate("MainWindow", "USERNAME"))
        self.DayandDate.setText(_translate("MainWindow", "Thursday, 25.10"))
        self.Timelabel.setText(_translate("MainWindow", "5:48 PM"))
        self.DashboarLabel.setText(_translate("MainWindow", "DASHBOARD"))
        self.NumSIgnLanLabel.setText(_translate("MainWindow", "NUMBER OF PEOPLE USING \n"
"SIGN LANGUAGE"))
        self.NumAudLanLabel.setText(_translate("MainWindow", "NUMBER OF PEOPLE \n"
"USING AUDIO"))
        self.AvgSignLanLabel.setText(_translate("MainWindow", "AVERAGE SIGN LANGUAGE \n"
"USER"))
        self.NumLabel.setText(_translate("MainWindow", "10,0000"))
        self.NumLabel_2.setText(_translate("MainWindow", "10,0000"))
        self.DayLabel.setText(_translate("MainWindow", "TODAY"))
        self.DayLabel_2.setText(_translate("MainWindow", "TODAY"))
        self.ActiveUserCountlabel.setText(_translate("MainWindow", "10"))
        self.ActiveUserlabel.setText(_translate("MainWindow", "ACTIVE USER"))
        self.SeeAllBtn.setText(_translate("MainWindow", "SEE ALL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
