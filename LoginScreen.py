
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
# from RegisterScreen import *
from PyQt6.QtWidgets import QLineEdit, QMessageBox
from pymongo import MongoClient



class Ui_MainWindow1(object):

    def showMessagePassword(self):
        msgBox = QMessageBox()
        msgBox.setText("Invalid credentials")
        msgBox.setWindowTitle("Alert")
        #msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()

    def showMessageEmpty(self):
        msgBox = QMessageBox()
        msgBox.setText("Empty field")
        msgBox.setWindowTitle("Alert")
        #msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()

    def LoginVerification(self):
        connectionString = MongoClient('mongodb://localhost:27017')
        mydb = connectionString['PSL']
        table = mydb.userRegistration
        userName = self.UsernameLineEdit.text()
        password = self.PasswordLineEdit.text()
        check = table.find().count
        corr_pass = ""
        count = 0

        if userName == "" or password == "":
            self.showMessageEmpty()
            self.LogScreen()

        for user in table.find():
            count += 1

            if user.get('UserName') == userName:

                correctPassword = user.get('Password')
                if correctPassword == password:
                    print('Correct Password')
                    self.Dashboard(userName)
                else:
                    print("incorrect password")
                    self.showMessagePassword()
                    self.LogScreen()

                break
            if count == check:
                print("user not found")




    def LogScreen(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window2)
        self.window2.show()


    def RegisterScreen(self):
        from RegisterScreen import Ui_MainWindow_RegisterScreen
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_RegisterScreen()
        self.ui.setupUi(self.window2)
        self.window2.show()


    # method fro opening splash screen
    def SplashScreen(self):
        from SplashScreen import Ui_MainWindow
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()


    # method fro opening dashboard screen
    def Dashboard(self,username):
        from Dashboard import Ui_MainWindow_Dashboard
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Dashboard()
        self.ui.setupUi(self.window2,username)
        self.window2.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginScreen = QtWidgets.QLabel(self.centralwidget)
        self.LoginScreen.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.LoginScreen.setPixmap(QPixmap("./Images/Login Screen.jpg"))
        # self.LoginScreen.setStyleSheet("image: url(:/newPrefix/Login Screen.jpg);")
        self.LoginScreen.setText("")
        self.LoginScreen.setObjectName("LoginScreen")
        self.RegisterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterBtn.setGeometry(QtCore.QRect(856, 13, 154, 38))
        self.RegisterBtn.setStyleSheet("#RegisterBtn{\n"
                                       "box-shadow: 0px 3px 6px #00000066;\n"
                                       "border: 2px solid #39B54A;\n"
                                       "border-radius: 5px;\n"
                                       "opacity: 1;\n"
                                       "font: 18px \"Montserrat\";\n"
                                       "color: #106A38;\n"
                                       "}\n"
                                       "QPushButton#RegisterBtn:hover{\n"
                                       "background-color: #106A38;\n"
                                       "color: #ffffff;\n"
                                       "}")
        self.RegisterBtn.setObjectName("RegisterBtn")

        self.GoToMainBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GoToMainBtn.setGeometry(QtCore.QRect(726, 22, 81, 19))
        self.GoToMainBtn.setStyleSheet("#GoToMainBtn{\n"
                                       "background: transparent;\n"
                                       "color: #106A38;\n"
                                       "    font: 15px \"Montserrat\";\n"
                                       "}")
        self.GoToMainBtn.setObjectName("GoToMainBtn")
        self.UserLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserLabel.setGeometry(QtCore.QRect(61, 343, 100, 22))
        self.UserLabel.setStyleSheet("#UserLabel{\n"
                                     "color: var(--unnamed-color-106a38);\n"
                                     "text-align: left;\n"
                                     "font: 57 18px \"Montserrat Medium\";\n"
                                     "letter-spacing: 0px;\n"
                                     "color: #106A38;\n"
                                     "opacity: 1;\n"
                                     "\n"
                                     "}")
        self.UserLabel.setObjectName("UserLabel")
        self.UsernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameLineEdit.setGeometry(QtCore.QRect(61, 368, 285, 48))
        self.UsernameLineEdit.setStyleSheet("#UsernameLineEdit{\n"
                                            "border: 2px solid var(--unnamed-color-106a38);\n"
                                            "box-shadow: 0px 3px 6px #00000066;\n"
                                            "border: 2px solid #106A38;\n"
                                            "border-radius: 6px;\n"
                                            "opacity: 1;\n"
                                            "}")
        self.UsernameLineEdit.setObjectName("UsernameLineEdit")
        self.UsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsernameLabel.setGeometry(QtCore.QRect(61, 343, 100, 22))
        self.UsernameLabel.setStyleSheet("#UsernameLabel{\n"
                                         "color: var(--unnamed-color-106a38);\n"
                                         "text-align: left;\n"
                                         "font: 57 18px \"Montserrat Medium\";\n"
                                         "letter-spacing: 0px;\n"
                                         "color: #106A38;\n"
                                         "opacity: 1;\n"
                                         "}")
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)

        self.PasswordLabel.setGeometry(QtCore.QRect(61, 444, 88, 22))
        self.PasswordLabel.setStyleSheet("#PasswordLabel{\n"
                                         "color: var(--unnamed-color-106a38);\n"
                                         "text-align: left;\n"
                                         "font: 57 18px \"Montserrat Medium\";\n"
                                         "letter-spacing: 0px;\n"
                                         "color: #106A38;\n"
                                         "opacity: 1;\n"
                                         "}")
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.PasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.PasswordLineEdit.setGeometry(QtCore.QRect(61, 469, 285, 48))
        self.PasswordLineEdit.setStyleSheet("#PasswordLineEdit{\n"
                                            "border: 2px solid var(--unnamed-color-106a38);\n"
                                            "box-shadow: 0px 3px 6px #00000066;\n"
                                            "border: 2px solid #106A38;\n"
                                            "border-radius: 6px;\n"
                                            "opacity: 1;\n"
                                            "\n"
                                            "}")

        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LoginBtn.setGeometry(QtCore.QRect(107, 560, 178, 44))

        self.LoginBtn.setStyleSheet("#LoginBtn{\n"


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
                                    "QPushButton#LoginBtn:hover{\n"
                                    "color: #FFFFFF ;\n"
                                    "background-color: #106A38;\n"
                                    "}\n"
                                    "")
        self.LoginBtn.setObjectName("LoginBtn")
        self.LoginBtn.clicked.connect(self.LoginVerification)
        self.LoginBtn.clicked.connect(MainWindow.close)

        self.CreateAnAccount = QtWidgets.QPushButton(self.centralwidget)
        self.CreateAnAccount.setGeometry(QtCore.QRect(111, 612, 134, 18))
        self.CreateAnAccount.setStyleSheet("#CreateAnAccount{\n"
                                           "color: var(--unnamed-color-3cb44a);\n"
                                           "font: normal normal bold 14px Montserrat;\n"
                                           "color: #3CB44A;\n"
                                           "opacity: 1;\n"
                                           "background-color: Transparent;\n"
                                           " background-repeat: no-repeat;\n"
                                           " border: none;\n"
                                           " cursor: pointer;\n"
                                           " overflow: hidden;\n"
                                           " outline: none;\n"
                                           "\n"
                                           "}")
        self.CreateAnAccount.setObjectName("CreateAnAccount")
        self.CreateAnAccount.clicked.connect(self.RegisterScreen)
        self.CreateAnAccount.clicked.connect(MainWindow.close)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(267, 612, 18, 18))
        self.label.setPixmap(QPixmap("./Images/Icon awesome-arrow-alt-circle-right.png"))
        # self.label.setStyleSheet("image: url(:/newPrefix/Icon awesome-arrow-alt-circle-right.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.UserLabel.raise_()
        self.LoginScreen.raise_()
        self.RegisterBtn.raise_()
        self.GoToMainBtn.raise_()
        self.UsernameLineEdit.raise_()
        self.UsernameLabel.raise_()
        self.PasswordLabel.raise_()
        self.PasswordLineEdit.raise_()
        self.LoginBtn.raise_()
        self.CreateAnAccount.raise_()
        self.label.raise_()
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
        self.RegisterBtn.setText(_translate("MainWindow", "Register"))

        self.RegisterBtn.clicked.connect(self.RegisterScreen)
        self.RegisterBtn.clicked.connect(MainWindow.close)

        self.GoToMainBtn.setText(_translate("MainWindow", "Go to Main"))
        self.GoToMainBtn.clicked.connect(self.SplashScreen)
        self.GoToMainBtn.clicked.connect(MainWindow.close)

        self.UserLabel.setText(_translate("MainWindow", "Username"))
        self.UsernameLabel.setText(_translate("MainWindow", "Username"))
        self.PasswordLabel.setText(_translate("MainWindow", "Password"))
        self.LoginBtn.setText(_translate("MainWindow", "Login"))
        self.CreateAnAccount.setText(_translate("MainWindow", "Create an Account"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
