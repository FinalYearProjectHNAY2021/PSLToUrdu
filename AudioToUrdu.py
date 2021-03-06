# Form implementation generated from reading ui file 'AudioToUrdu.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from datetime import datetime, date

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QTextStream
from PyQt6.QtGui import QPixmap, QIcon
import speech_recognition as sr



class Ui_MainWindow_AudiotoUrdu(object):

    def speechToText(self):
        input = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say Something:')
            audio = input.listen(source)
            print('Done!')
        text = input.recognize_google(audio, language='ur')
        self.textEdit.setText(text)


    # method for opening menu screen
    def Menu(self):
        from Menu import Ui_MainWindow_Menu
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Menu()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AudioToUrdu = QtWidgets.QLabel(self.centralwidget)
        self.AudioToUrdu.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.AudioToUrdu.setPixmap(QPixmap("./Images/AudioToUrdu.png"))
        # self.AudioToUrdu.setStyleSheet("background-image: url(:/newPrefix/AudioToUrdu.png);")
        self.AudioToUrdu.setText("")
        self.AudioToUrdu.setObjectName("AudioToUrdu")
        self.DashboardIcon = QtWidgets.QLabel(self.centralwidget)
        self.DashboardIcon.setGeometry(QtCore.QRect(17, 262, 54, 30))
        self.DashboardIcon.setPixmap(QPixmap("./Images/Group 308.png"))
        # self.DashboardIcon.setStyleSheet("Image: url(:/newPrefix/Group 308.png)")
        self.DashboardIcon.setText("")
        self.DashboardIcon.setObjectName("DashboardIcon")
        self.PsltoUrduIcon = QtWidgets.QLabel(self.centralwidget)
        self.PsltoUrduIcon.setGeometry(QtCore.QRect(17, 331, 56, 35))
        self.PsltoUrduIcon.setPixmap(QPixmap("./Images/Group 309.png"))
        # self.PsltoUrduIcon.setStyleSheet("Image: url(:/newPrefix/Group 309.png)")
        self.PsltoUrduIcon.setText("")
        self.PsltoUrduIcon.setObjectName("PsltoUrduIcon")
        self.AudiotoUrduIcon = QtWidgets.QLabel(self.centralwidget)
        self.AudiotoUrduIcon.setGeometry(QtCore.QRect(10, 404, 68, 36))
        self.AudiotoUrduIcon.setPixmap(QPixmap("./Images/Group 310.png"))
        # self.AudiotoUrduIcon.setStyleSheet("Image: url(:/newPrefix/Group 310.png)")
        self.AudiotoUrduIcon.setText("")
        self.AudiotoUrduIcon.setObjectName("AudiotoUrduIcon")
        self.ProfileIcon = QtWidgets.QLabel(self.centralwidget)
        self.ProfileIcon.setGeometry(QtCore.QRect(24, 478, 40, 33))
        self.ProfileIcon.setPixmap(QPixmap("./Images/Group 311.png"))
        # self.ProfileIcon.setStyleSheet("Image: url(:/newPrefix/Group 311.png)")
        self.ProfileIcon.setText("")
        self.ProfileIcon.setObjectName("ProfileIcon")
        self.NotiIcon = QtWidgets.QLabel(self.centralwidget)
        self.NotiIcon.setGeometry(QtCore.QRect(764, 27, 20, 20))
        self.NotiIcon.setPixmap(QPixmap("./Images/Icon ionic-ios-notifications-outline.png"))
        # self.NotiIcon.setStyleSheet("image: url(:/newPrefix/Icon ionic-ios-notifications-outline.png);")
        self.NotiIcon.setText("")
        self.NotiIcon.setObjectName("NotiIcon")
        self.MsgIcon = QtWidgets.QLabel(self.centralwidget)
        self.MsgIcon.setGeometry(QtCore.QRect(812, 27, 20, 20))
        self.MsgIcon.setPixmap(QPixmap("./Images/Icon feather-message-square.png"))
        # self.MsgIcon.setStyleSheet("Image: url(:/newPrefix/Icon feather-message-square.png)")
        self.MsgIcon.setText("")
        self.MsgIcon.setObjectName("MsgIcon")
        self.UsernnameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsernnameLabel.setGeometry(QtCore.QRect(863, 30, 72, 14))
        self.UsernnameLabel.setStyleSheet("#UsernnameLabel {\n"
"color: rgb(255, 255, 255);\n"
"font: 11px \"Montserrat\";\n"
"\n"
"\n"
"}")
        self.UsernnameLabel.setObjectName("UsernnameLabel")
        self.profilepushButton = QtWidgets.QPushButton(self.centralwidget)
        self.profilepushButton.setGeometry(QtCore.QRect(947, 15, 44, 44))
        self.profilepushButton.setIconSize(QSize(35, 35))
        self.profilepushButton.setIcon(QIcon("./Images/Path 206.png"))

        self.profilepushButton.setStyleSheet("#profilepushButton{\n"
"image: url(:/newPrefix/Path 206.png);\n"
"border: 1px solid #00A65A;\n"
"border-radius: 22px;\n"
"background-color: Transparent;\n"
"\n"
"    image: url(:/newPrefix/Path 206.png);\n"
"\n"
"\n"
"\n"
"\n"
"}")
        self.profilepushButton.setText("")
        self.profilepushButton.setObjectName("profilepushButton")
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
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        # print("d2 =", d2)
        self.DayandDateLabel.setText(d2)
        print(d2)

        self.Timelabel = QtWidgets.QLabel(self.centralwidget)
        self.Timelabel.setGeometry(QtCore.QRect(159, 52, 115, 52))
        self.Timelabel.setStyleSheet("#Timelabel{\n"
"text-align: left;\n"
# "letter-spacing: NaNpx;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"font: 28px \"Montserrat\";\n"
"\n"
"\n"
"}")
        self.Timelabel.setObjectName("Timelabel")

        now = datetime.now()
        t = now.strftime("%H:%M")
        self.Timelabel.setText(t)
        print(t)

        self.AudiotoUrdulabel = QtWidgets.QLabel(self.centralwidget)
        self.AudiotoUrdulabel.setGeometry(QtCore.QRect(159, 155, 187, 27))
        self.AudiotoUrdulabel.setStyleSheet("#AudiotoUrdulabel{\n"
"text-align: left;\n"
"font: 22px \"Montserrat\";\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"opacity: 1;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.AudiotoUrdulabel.setObjectName("AudiotoUrdulabel")
        self.Audiolabel = QtWidgets.QLabel(self.centralwidget)
        self.Audiolabel.setGeometry(QtCore.QRect(148, 217, 38, 14))
        self.Audiolabel.setStyleSheet("#Audiolabel{\n"
"color: rgb(255, 255, 255);\n"
"font: 11px \"Montserrat\";\n"
"\n"
"\n"
"\n"
"}")
        self.Audiolabel.setObjectName("Audiolabel")
        self.AudiIcon = QtWidgets.QLabel(self.centralwidget)
        self.AudiIcon.setGeometry(QtCore.QRect(194, 217, 14, 14))
        self.AudiIcon.setPixmap(QPixmap("./Images/Icon material-audiotrack.png"))
        # self.AudiIcon.setStyleSheet("image: url(:/newPrefix/Icon material-audiotrack.png);")
        self.AudiIcon.setText("")
        self.AudiIcon.setObjectName("AudiIcon")
        self.AudiopushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AudiopushButton.setGeometry(QtCore.QRect(230, 380, 92, 105))
        self.AudiopushButton.setStyleSheet("#AudiopushButton{\n"
"image: url(:/newPrefix/Icon open-audio-spectrum.png);\n"
"background-color:transparent\n"
"\n"
"}")
        self.AudiopushButton.setText("")
        self.AudiopushButton.setObjectName("AudiopushButton")
        self.AudiopushButton.setIconSize(QSize(100,100))
        self.AudiopushButton.setIcon(QIcon("./Images/Icon open-audio-spectrum.png"))
        self.AudiopushButton.clicked.connect(self.speechToText)

        self.TextIcon = QtWidgets.QLabel(self.centralwidget)
        self.TextIcon.setGeometry(QtCore.QRect(535, 210, 14, 14))
        self.TextIcon.setPixmap(QPixmap("./Images/Icon open-text.png"))
        # self.TextIcon.setStyleSheet("image: url(:/newPrefix/Icon open-text.png);")
        self.TextIcon.setText("")
        self.TextIcon.setObjectName("TextIcon")
        self.TextLabel = QtWidgets.QLabel(self.centralwidget)
        self.TextLabel.setGeometry(QtCore.QRect(500, 210, 31, 14))
        self.TextLabel.setStyleSheet("#TextLabel{\n"
"color: rgb(255, 255, 255);\n"
"font: 11px \"Montserrat\";\n"
"\n"
"\n"
"\n"
"}")
        self.TextLabel.setObjectName("TextLabel")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(500, 240, 471, 381))
        self.textEdit.setStyleSheet("#textEdit{\n"
"background-color:Transparent;\n"
"color: rgb(255, 255, 255);\n"
"    font: 11pt \"Montserrat\";\n"
"\n"
"\n"
"\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.SideBar = QtWidgets.QPushButton(self.centralwidget)
        self.SideBar.setGeometry(QtCore.QRect(-10, -15, 96, 795))
        self.SideBar.setStyleSheet("#SideBar{\n"
"border-radius: 2px;\n"
"background-color: rgb(0, 166, 90);\n"
"\n"
"\n"
"\n"
"}")
        self.SideBar.setText("")
        self.SideBar.setObjectName("SideBar")
        self.SideBar.clicked.connect(self.Menu)
        self.SideBar.clicked.connect(MainWindow.close)


        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(14, 40, 62, 47))
        self.LogoLabel.setText("")
        self.LogoLabel.setObjectName("LogoLabel")
        self.LogoLabel.setPixmap(QPixmap("./Images/check.png"))
        self.AudioToUrdu.raise_()
        self.NotiIcon.raise_()
        self.MsgIcon.raise_()
        self.UsernnameLabel.raise_()
        self.profilepushButton.raise_()
        self.DayandDateLabel.raise_()
        self.Timelabel.raise_()
        self.AudiotoUrdulabel.raise_()
        self.Audiolabel.raise_()
        self.AudiIcon.raise_()
        self.AudiopushButton.raise_()
        self.TextIcon.raise_()
        self.TextLabel.raise_()
        self.textEdit.raise_()
        self.SideBar.raise_()
        self.AudiotoUrduIcon.raise_()
        self.DashboardIcon.raise_()
        self.PsltoUrduIcon.raise_()
        self.ProfileIcon.raise_()
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
        self.UsernnameLabel.setText(_translate("MainWindow", "USERNAME"))
        # self.DayandDateLabel.setText(_translate("MainWindow", "Thursday, 25.10"))
        # self.Timelabel.setText(_translate("MainWindow", "5:48 PM"))
        self.AudiotoUrdulabel.setText(_translate("MainWindow", "AUDIO TO URDU"))
        self.Audiolabel.setText(_translate("MainWindow", "AUDIO"))
        self.TextLabel.setText(_translate("MainWindow", "TEXT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_AudiotoUrdu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
