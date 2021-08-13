# Form implementation generated from reading ui file 'PSLtoUrdu.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon


class Ui_MainWindow_PSLtoUrdu(object):

    # method for opening menu screen
    def Menu(self):
        from Menu import Ui_MainWindow_Menu
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Menu()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 764)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ProfileScreen = QtWidgets.QLabel(self.centralwidget)
        self.ProfileScreen.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.ProfileScreen.setPixmap(QPixmap("./Images/PSL To Urdu.png"))
        # self.ProfileScreen.setStyleSheet("background-image: url(:/newPrefix/PSLToUrdu.png);")
        self.ProfileScreen.setText("")
        self.ProfileScreen.setObjectName("ProfileScreen")
        self.DashboardIcon = QtWidgets.QLabel(self.centralwidget)
        self.DashboardIcon.setGeometry(QtCore.QRect(17, 262, 54, 30))
        self.DashboardIcon.setPixmap(QPixmap("./Images/Group 308.png"))
        # self.DashboardIcon.setStyleSheet("image: url(:/newPrefix/Group 308.png);")
        self.DashboardIcon.setText("")
        self.DashboardIcon.setObjectName("DashboardIcon")
        self.PslToUrduIcon = QtWidgets.QLabel(self.centralwidget)
        self.PslToUrduIcon.setGeometry(QtCore.QRect(17, 330, 56, 35))
        self.PslToUrduIcon.setPixmap(QPixmap("./Images/Group 309.png"))
        # self.PslToUrduIcon.setStyleSheet("image: url(:/newPrefix/Group 309.png);")
        self.PslToUrduIcon.setText("")
        self.PslToUrduIcon.setObjectName("PslToUrduIcon")
        self.AudioToUrduIcon = QtWidgets.QLabel(self.centralwidget)
        self.AudioToUrduIcon.setGeometry(QtCore.QRect(10, 404, 68, 36))
        self.AudioToUrduIcon.setPixmap(QPixmap("./Images/Group 310.png"))
        # self.AudioToUrduIcon.setStyleSheet("Image: url(:/newPrefix/Group 310.png)")
        self.AudioToUrduIcon.setText("")
        self.AudioToUrduIcon.setObjectName("AudioToUrduIcon")
        self.ProfileIcon = QtWidgets.QLabel(self.centralwidget)
        self.ProfileIcon.setGeometry(QtCore.QRect(24, 478, 40, 33))
        self.ProfileIcon.setPixmap(QPixmap("./Images/Group 311.png"))
        # self.ProfileIcon.setStyleSheet("Image:url(:/newPrefix/Group 311.png)")
        self.ProfileIcon.setText("")
        self.ProfileIcon.setObjectName("ProfileIcon")
        self.NotiLabel = QtWidgets.QLabel(self.centralwidget)
        self.NotiLabel.setGeometry(QtCore.QRect(764, 27, 16, 20))
        self.NotiLabel.setPixmap(QPixmap("./Images/Icon ionic-ios-notifications-outline.png"))
        # self.NotiLabel.setStyleSheet("Image: url(:/newPrefix/Icon ionic-ios-notifications-outline.png)")
        self.NotiLabel.setText("")
        self.NotiLabel.setObjectName("NotiLabel")
        self.MsgIcon = QtWidgets.QLabel(self.centralwidget)
        self.MsgIcon.setGeometry(QtCore.QRect(800, 30, 47, 13))
        self.MsgIcon.setPixmap(QPixmap("./Images/Icon feather-message-square.png"))
        # self.MsgIcon.setStyleSheet("Image:url(:/newPrefix/Icon feather-message-square.png)")
        self.MsgIcon.setText("")
        self.MsgIcon.setObjectName("MsgIcon")
        self.UserNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserNameLabel.setGeometry(QtCore.QRect(863, 30, 72, 14))
        self.UserNameLabel.setStyleSheet("#UserNameLabel{\n"
"font: 11px \"Montserrat\";\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"\n"
"\n"
"\n"
"}")
        self.UserNameLabel.setObjectName("UserNameLabel")
        self.ProfilepushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProfilepushButton.setGeometry(QtCore.QRect(947, 15, 44, 44))
        self.ProfilepushButton.setStyleSheet("#ProfilepushButton{\n"
"image: url(:/newPrefix/Path 206.png);\n"
"border: 1px solid #00A65A;\n"
"border-radius: 22px;\n"
"background-color: Transparent;\n"
"\n"
"}")
        self.ProfilepushButton.setText("")
        self.ProfilepushButton.setObjectName("ProfilepushButton")
        self.ProfilepushButton.setIconSize(QSize(35, 35))
        self.ProfilepushButton.setIcon(QIcon("./Images/Path 206.png"))

        self.Cameralabel = QtWidgets.QLabel(self.centralwidget)
        self.Cameralabel.setGeometry(QtCore.QRect(159, 215, 49, 13))
        self.Cameralabel.setStyleSheet("#Cameralabel{\n"
"font: 11px \"Montserrat\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.Cameralabel.setObjectName("Cameralabel")
        self.texLabel = QtWidgets.QLabel(self.centralwidget)
        self.texLabel.setGeometry(QtCore.QRect(700, 215, 31, 13))
        self.texLabel.setStyleSheet("#texLabel{\n"
"font: 11px \"Montserrat\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.texLabel.setObjectName("texLabel")
        self.AudioLabel = QtWidgets.QLabel(self.centralwidget)
        self.AudioLabel.setGeometry(QtCore.QRect(700, 470, 41, 13))
        self.AudioLabel.setStyleSheet("#AudioLabel{\n"
"font: 11px \"Montserrat\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.AudioLabel.setObjectName("AudioLabel")
        self.CameraIcon = QtWidgets.QLabel(self.centralwidget)
        self.CameraIcon.setGeometry(QtCore.QRect(215, 215, 15, 15))
        self.CameraIcon.setPixmap(QPixmap("./Images/Icon awesome-camera.png"))
        # self.CameraIcon.setStyleSheet("Image: url(:/newPrefix/Icon awesome-camera.png)")
        self.CameraIcon.setText("")
        self.CameraIcon.setObjectName("CameraIcon")
        self.TextLabel = QtWidgets.QLabel(self.centralwidget)
        self.TextLabel.setGeometry(QtCore.QRect(732, 215, 15, 15))
        self.TextLabel.setPixmap(QPixmap("./Images/Icon open-text.png"))
        # self.TextLabel.setStyleSheet("image: url(:/newPrefix/Icon open-text.png);")
        self.TextLabel.setText("")
        self.TextLabel.setObjectName("TextLabel")
        self.AudioIcon = QtWidgets.QLabel(self.centralwidget)
        self.AudioIcon.setGeometry(QtCore.QRect(744, 470, 15, 15))
        self.AudioIcon.setPixmap(QPixmap("./Images/Icon material-audiotrack.png"))
        # self.AudioIcon.setStyleSheet("image: url(:/newPrefix/Icon material-audiotrack.png);")
        self.AudioIcon.setText("")
        self.AudioIcon.setObjectName("AudioIcon")
        self.AudiopushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AudiopushButton.setGeometry(QtCore.QRect(780, 504, 105, 105))
        self.AudiopushButton.setStyleSheet("#AudiopushButton{\n"
"image: url(:/newPrefix/Icon open-audio-spectrum.png);\n"
"background-color: transparent;\n"
"\n"
"\n"
"}")
        self.AudiopushButton.setText("")
        self.AudiopushButton.setObjectName("AudiopushButton")
        self.AudiopushButton.setIconSize(QSize(100, 100))
        self.AudiopushButton.setIcon(QIcon("./Images/Icon open-audio-spectrum.png"))

        self.DayandDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.DayandDateLabel.setGeometry(QtCore.QRect(159, 37, 123, 19))
        self.DayandDateLabel.setStyleSheet("#DayandDateLabel{\n"
"font: 16px \"Montserrat\";\n"
"text-align: left;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"\n"
"\n"
"\n"
"}")
        self.DayandDateLabel.setObjectName("DayandDateLabel")
        self.TimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(159, 52, 115, 52))
        self.TimeLabel.setStyleSheet("#TimeLabel{\n"
"text-align: left;\n"
"letter-spacing: NaNpx;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"font: 28px \"Montserrat\";\n"
"\n"
"\n"
"}")
        self.TimeLabel.setObjectName("TimeLabel")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(700, 240, 281, 171))
        self.textEdit.setStyleSheet("#textEdit{\n"
"background-color:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 11px \"Montserrat\";\n"
"\n"
"\n"
"\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.PsltoUrdulabel = QtWidgets.QLabel(self.centralwidget)
        self.PsltoUrdulabel.setGeometry(QtCore.QRect(159, 155, 154, 27))
        self.PsltoUrdulabel.setStyleSheet("#PsltoUrdulabel{\n"
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
        self.PsltoUrdulabel.setObjectName("PsltoUrdulabel")
        self.SideBar = QtWidgets.QPushButton(self.centralwidget)
        self.SideBar.setGeometry(QtCore.QRect(-10, -15, 96, 795))
        self.SideBar.setStyleSheet("#SideBar{\n"
"\n"
"border-radius: 2px;\n"
"background-color: rgb(0, 166, 90);\n"
"\n"
"\n"
"}")
        self.SideBar.setText("")
        self.SideBar.setObjectName("SideBar")

        self.SideBar.clicked.connect(self.Menu)
        self.SideBar.clicked.connect(MainWindow.close)


        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(14, 41, 62, 48))
        self.LogoLabel.setPixmap(QPixmap("./Images/PSL TO URDU logo-02.png"))
        # self.LogoLabel.setStyleSheet("image: url(:/newPrefix/PSL TO URDU logo-02.png);")
        self.LogoLabel.setText("")
        self.LogoLabel.setObjectName("LogoLabel")
        self.ProfileScreen.raise_()
        self.NotiLabel.raise_()
        self.MsgIcon.raise_()
        self.UserNameLabel.raise_()
        self.ProfilepushButton.raise_()
        self.Cameralabel.raise_()
        self.texLabel.raise_()
        self.AudioLabel.raise_()
        self.CameraIcon.raise_()
        self.TextLabel.raise_()
        self.AudioIcon.raise_()
        self.AudiopushButton.raise_()
        self.DayandDateLabel.raise_()
        self.TimeLabel.raise_()
        self.textEdit.raise_()
        self.SideBar.raise_()
        self.DashboardIcon.raise_()
        self.ProfileIcon.raise_()
        self.PslToUrduIcon.raise_()
        self.PsltoUrdulabel.raise_()
        self.AudioToUrduIcon.raise_()
        self.LogoLabel.raise_()
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
        self.UserNameLabel.setText(_translate("MainWindow", "USERNAME"))
        self.Cameralabel.setText(_translate("MainWindow", "CAMERA"))
        self.texLabel.setText(_translate("MainWindow", "TEXT"))
        self.AudioLabel.setText(_translate("MainWindow", "AUDIO"))
        self.DayandDateLabel.setText(_translate("MainWindow", "Thursday, 25.10"))
        self.TimeLabel.setText(_translate("MainWindow", "5:48 PM"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:11px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam</span></p></body></html>"))
        self.PsltoUrdulabel.setText(_translate("MainWindow", "PSL TO URDU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_PSLtoUrdu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
