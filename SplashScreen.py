# Form implementation generated from reading ui file 'SplashScreen.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

# from RegisterScreen import Ui_MainWindow_RegisterScreen


# def login():
#     from LoginScreen import Ui_MainWindow1


class Ui_MainWindow(object):

    # method fro opening new window
    def LoginScreen(self):
        from LoginScreen import Ui_MainWindow1
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window2)
        self.window2.show()

        # Hasnain noor
        # method fro opening new window
    def RegisterScreen(self):
        from RegisterScreen import Ui_MainWindow_RegisterScreen
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_RegisterScreen()
        self.ui.setupUi(self.window3)
        self.window3.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 768)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -3, 1024, 791))
        self.label.setPixmap(QPixmap("./Images/Splash Screen.png"))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LoginBtn.setGeometry(QtCore.QRect(95, 576, 178, 44))
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
                                    "}")
        self.LoginBtn.setObjectName("LoginBtn")
        # button click method for screen change

        self.LoginBtn.clicked.connect(self.LoginScreen)
        self.LoginBtn.clicked.connect(MainWindow.close)
        self.CreateAnAccount = QtWidgets.QPushButton(self.centralwidget)
        self.CreateAnAccount.setGeometry(QtCore.QRect(99, 623, 134, 18))

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

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(255, 623, 18, 18))
        self.label_2.setPixmap(QPixmap("./Images/Icon awesome-arrow-alt-circle-right.png"))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(91, 315, 457, 189))
        self.plainTextEdit.setStyleSheet("#plainTextEdit{\n"
                                         "background-color: Transparent;\n"
                                         " background-repeat: no-repeat;\n"
                                         " border: none;\n"
                                         " cursor: pointer;\n"
                                         " overflow: hidden;\n"
                                         " outline: none;\n"
                                         "text-align: left;\n"
                                         "font: normal normal normal 20px/27px Segoe UI;\n"
                                         "letter-spacing: 0px;\n"
                                         "color: #707070;\n"
                                         "opacity: 1;\n"
                                         "\n"
                                         "}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 21))
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
        self.LoginBtn.setText(_translate("MainWindow", "Login"))
        self.CreateAnAccount.setText(_translate("MainWindow", "Create an account"))
        self.plainTextEdit.setPlainText(_translate("MainWindow",
                                                   "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
