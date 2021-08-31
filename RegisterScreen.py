# Form implementation generated from reading ui file 'RegisterScreen.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLineEdit, QMessageBox

from LoginScreen import Ui_MainWindow1
from SplashScreen import *
from pymongo import MongoClient


class Ui_MainWindow_RegisterScreen(object):

    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setText("All the Fields Are Empty")
        msgBox.setWindowTitle("Alert")
        #msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()

    # def check(self, e):
    #     print(e)
    #     regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    #
    #     if (re.search(regex, e)):
    #         return True
    #
    #     else:
    #         return False

    def insertData(self):
        connectionString = MongoClient('mongodb://localhost:27017')
        mydb = connectionString['PSL']
        table = mydb.userRegistration

        data = {
            'FirstName': self.FirstNameLineEdit.text(),
            'LastName': self.LastNamelineEdit.text(),
            'Email': self.EmaillineEdit.text(),
            'UserName': self.UserNamelineEdit.text(),
            'Password': self.PasswordlineEdit.text()
        }
        table.insert_one(data)

    def databaseMethod(self):
        if self.FirstNameLineEdit.text() == "" or self.LastNamelineEdit.text() == "" or self.LastNamelineEdit.text() == "" or self.UserNamelineEdit.text() == "" or self.PasswordlineEdit.text() == "":
            self.showDialog()
        # elif self.check(self.EmaillineEdit.text()) == False:
        #     print("Enter a valid email")
        else:
            self.insertData()
        #     connectionString = MongoClient('mongodb://localhost:27017')
        #     mydb = connectionString['PSL']
        #     table = mydb.userRegistration
        #
        #     data = {
        #         'FirstName': self.FirstNameLineEdit.text(),
        #         'LastName': self.LastNamelineEdit.text(),
        #         'Email': self.EmaillineEdit.text(),
        #         'UserName': self.UserNamelineEdit.text(),
        #         'Password': self.PasswordlineEdit.text()
        #     }
        #     table.insert_one(data)



        # table.insert_one(data)
    # method fro opening login screen
    def LoginScreen(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window2)
        self.window2.show()


    # method fro opening splash screen
    def SplashScreen(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def RegisterScreen(self):
        from RegisterScreen import Ui_MainWindow_RegisterScreen
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_RegisterScreen()
        self.ui.setupUi(self.window3)
        self.window3.show()

    def setupUi(self, MainWindow):
        global Password, Password, Email, Password, Password, Email
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RegisterMain = QtWidgets.QLabel(self.centralwidget)
        self.RegisterMain.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.RegisterMain.setPixmap(QPixmap("./Images/Register Screen.jpg"))
        # self.RegisterMain.setStyleSheet("image: url(:/newPrefix/Register Screen.jpg);")
        self.RegisterMain.setText("")
        self.RegisterMain.setObjectName("RegisterMain")
        self.LoginBtnTop = QtWidgets.QPushButton(self.centralwidget)
        self.LoginBtnTop.setGeometry(QtCore.QRect(856, 13, 154, 38))
        self.LoginBtnTop.setStyleSheet("#LoginBtnTop{\n"
                                       "box-shadow: 0px 3px 6px #00000066;\n"
                                       "border: 2px solid #39B54A;\n"
                                       "border-radius: 5px;\n"
                                       "opacity: 1;\n"
                                       "font: 18px \"Montserrat\";\n"
                                       "color: #106A38;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#LoginBtnTop:hover{\n"
                                       "background-color: #106A38;\n"
                                       "color: #ffffff;\n"
                                       "}")
        self.LoginBtnTop.setObjectName("LoginBtnTop")
        self.GotoMainBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GotoMainBtn.setGeometry(QtCore.QRect(762, 22, 81, 19))
        self.GotoMainBtn.setStyleSheet("#GotoMainBtn{\n"
                                       "background: transparent;\n"
                                       "color: #106A38;\n"
                                       "font: 15px \"Montserrat\";\n"
                                       "\n"
                                       "}")
        self.GotoMainBtn.setObjectName("GotoMainBtn")
        self.GotoMainBtn.clicked.connect(self.SplashScreen)
        self.GotoMainBtn.clicked.connect(MainWindow.close)

        self.FirstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FirstNameLineEdit.setPlaceholderText("First Name")
        self.FirstNameLineEdit.setGeometry(QtCore.QRect(64, 272, 282, 41))
        self.FirstNameLineEdit.setStyleSheet("#FirstNameLineEdit{\n"
                                             "border: 2px solid var(--unnamed-color-106a38);\n"
                                             "box-shadow: 0px 3px 6px #00000066;\n"
                                             "border: 2px solid #106A38;\n"
                                             "border-radius: 6px;\n"
                                             "opacity: 1;\n"
                                             "font: 15px \"Montserrat\";\n"
                                             "color: #39B54A;\n"
                                             "text-align: left;\n"
                                             "\n"
                                             "}")
        self.FirstNameLineEdit.setObjectName("FirstNameLineEdit")
        self.LastNamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LastNamelineEdit.setPlaceholderText("Last Name")
        self.LastNamelineEdit.setGeometry(QtCore.QRect(64, 336, 282, 41))
        self.LastNamelineEdit.setStyleSheet("#LastNamelineEdit{\n"
                                            "\n"
                                            "border: 2px solid var(--unnamed-color-106a38);\n"
                                            "box-shadow: 0px 3px 6px #00000066;\n"
                                            "border: 2px solid #106A38;\n"
                                            "border-radius: 6px;\n"
                                            "opacity: 1;\n"
                                            "font: 15px \"Montserrat\";\n"
                                            "color: #39B54A;\n"
                                            "text-align: left;\n"
                                            "\n"
                                            "\n"
                                            "}")
        self.LastNamelineEdit.setObjectName("LastNamelineEdit")
        self.EmaillineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.EmaillineEdit.setPlaceholderText("E-mail")
        self.EmaillineEdit.setGeometry(QtCore.QRect(64, 400, 282, 41))
        self.EmaillineEdit.setStyleSheet("#EmaillineEdit{\n"
                                         "\n"
                                         "border: 2px solid var(--unnamed-color-106a38);\n"
                                         "box-shadow: 0px 3px 6px #00000066;\n"
                                         "border: 2px solid #106A38;\n"
                                         "border-radius: 6px;\n"
                                         "opacity: 1;\n"
                                         "font: 15px \"Montserrat\";\n"
                                         "color: #39B54A;\n"
                                         "text-align: left;\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "}")
        self.EmaillineEdit.setObjectName("EmaillineEdit")
        self.UserNamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UserNamelineEdit.setPlaceholderText("Username")
        self.UserNamelineEdit.setGeometry(QtCore.QRect(64, 464, 282, 41))
        self.UserNamelineEdit.setStyleSheet("#UserNamelineEdit{\n"
                                            "border: 2px solid var(--unnamed-color-106a38);\n"
                                            "box-shadow: 0px 3px 6px #00000066;\n"
                                            "border: 2px solid #106A38;\n"
                                            "border-radius: 6px;\n"
                                            "opacity: 1;\n"
                                            "font: 15px \"Montserrat\";\n"
                                            "color: #39B54A;\n"
                                            "text-align: left;\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "}")
        self.UserNamelineEdit.setObjectName("UserNamelineEdit")
        self.PasswordlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.PasswordlineEdit.setPlaceholderText("Password")
        self.PasswordlineEdit.setGeometry(QtCore.QRect(64, 528, 282, 41))
        self.PasswordlineEdit.setStyleSheet("#PasswordlineEdit{\n"
                                            "border: 2px solid var(--unnamed-color-106a38);\n"
                                            "box-shadow: 0px 3px 6px #00000066;\n"
                                            "border: 2px solid #106A38;\n"
                                            "border-radius: 6px;\n"
                                            "opacity: 1;\n"
                                            "font: 15px \"Montserrat\";\n"
                                            "color: #39B54A;\n"
                                            "text-align: left;\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "}")
        self.PasswordlineEdit.setObjectName("PasswordlineEdit")
        self.RegisterpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterpushButton.setGeometry(QtCore.QRect(106, 606, 178, 44))
        self.RegisterpushButton.setStyleSheet("#RegisterpushButton{\n"
                                              "border-radius: 5px;\n"
                                              "box-shadow: 0px 3px 6px #000000;\n"
                                              "border: 2px solid #39B54A;\n"
                                              "opacity: 1;\n"
                                              "font-family: Montserrat;\n"
                                              "font-size: 21px;\n"
                                              "font-weight: 800;\n"
                                              "color: #106A38;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton#RegisterpushButton:hover{\n"
                                              "\n"
                                              "color: #FFFFFF ;\n"
                                              "background-color: #106A38;\n"
                                              "\n"
                                              "\n"
                                              "}")
        self.RegisterpushButton.setObjectName("RegisterpushButton")
        self.RegisterpushButton.clicked.connect(self.databaseMethod)
        self.RegisterpushButton.clicked.connect(self.LoginScreen)
        self.RegisterpushButton.clicked.connect(MainWindow.close)

        self.AlreadyAUserpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AlreadyAUserpushButton.setGeometry(QtCore.QRect(137, 660, 125, 18))
        self.AlreadyAUserpushButton.setStyleSheet("#AlreadyAUserpushButton{\n"
                                                  "color: var(--unnamed-color-3cb44a);\n"
                                                  "font: 14px \"Montserrat\";\n"
                                                  "font-weight:bold;\n"
                                                  "color: #3CB44A;\n"
                                                  "opacity: 1;\n"
                                                  "background-color: Transparent;\n"
                                                  " background-repeat: no-repeat;\n"
                                                  " border: none;\n"
                                                  " cursor: pointer;\n"
                                                  " overflow: hidden;\n"
                                                  " outline: none;\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "}")
        self.AlreadyAUserpushButton.setObjectName("AlreadyAUserpushButton")
        self.AlreadyAUserpushButton.clicked.connect(self.LoginScreen)
        self.AlreadyAUserpushButton.clicked.connect(MainWindow.close)
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
        self.LoginBtnTop.setText(_translate("MainWindow", "Login"))
        self.LoginBtnTop.clicked.connect(self.LoginScreen)
        self.LoginBtnTop.clicked.connect(MainWindow.close)

        self.GotoMainBtn.setText(_translate("MainWindow", "Go to Main"))
        # self.FirstNameLineEdit.setText(_translate("MainWindow", "   First name"))
        # self.LastNamelineEdit.setText(_translate("MainWindow", "   Last name"))
        # self.EmaillineEdit.setText(_translate("MainWindow", "   E-mail"))
        # self.UserNamelineEdit.setText(_translate("MainWindow", "   User name"))
        # self.PasswordlineEdit.setText(_translate("MainWindow", "   Password"))
        self.RegisterpushButton.setText(_translate("MainWindow", "Register"))
        self.AlreadyAUserpushButton.setText(_translate("MainWindow", "Already A User ?"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_RegisterScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
