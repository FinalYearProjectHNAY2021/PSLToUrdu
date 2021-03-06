# Form implementation generated from reading ui file 'Privacy.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon


class Ui_MainWindow_PrivacyPolicy(object):

    # method for profile screen
    def Profile(self):
        from Profile import Ui_MainWindow_Profile
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Profile()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 533)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 431, 533))
        self.label.setText("")
        self.label.setObjectName("label")
        self.PrivacyPolicyLabel = QtWidgets.QLabel(self.centralwidget)
        self.PrivacyPolicyLabel.setGeometry(QtCore.QRect(85, 28, 271, 28))
        self.PrivacyPolicyLabel.setStyleSheet("#PrivacyPolicyLabel{\n"
"font: 63 23px \"Montserrat\";\n"
"color: rgb(57, 181, 74);\n"
"font-weight: 600;\n"
"\n"
"}")
        self.PrivacyPolicyLabel.setObjectName("PrivacyPolicyLabel")
        self.BackpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackpushButton.setGeometry(QtCore.QRect(34, 32, 25, 19))
        self.BackpushButton.setIconSize(QSize(35, 35))
        self.BackpushButton.setIcon(QIcon("./Images/BackGreenIcon.png"))
        self.BackpushButton.setStyleSheet("\n"
"#BackpushButton{\n"
"background:transparent;\n"
"image: url(:/newPrefix/BackGreenIcon.png);    \n"
"\n"
"\n"
"}")
        self.BackpushButton.setText("")
        self.BackpushButton.setObjectName("BackpushButton")
        self.BackpushButton.clicked.connect(self.Profile)
        self.BackpushButton.clicked.connect(MainWindow.close)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(35, 85, 342, 355))
        self.scrollArea.setMinimumSize(QtCore.QSize(342, 355))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 323, 465))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ConditionLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ConditionLabel.setMinimumSize(QtCore.QSize(305, 29))
        self.ConditionLabel.setStyleSheet("#ConditionLabel{\n"
"font:  16pt \"Montserrat\";\n"
"font-weight: 600;\n"
"color: rgb(57, 181, 74);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.ConditionLabel.setObjectName("ConditionLabel")
        self.verticalLayout.addWidget(self.ConditionLabel)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setMinimumSize(QtCore.QSize(305, 73))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.PrivacyLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PrivacyLabel.setMinimumSize(QtCore.QSize(305, 29))
        self.PrivacyLabel.setStyleSheet("#PrivacyLabel{\n"
"font:  16pt \"Montserrat\";\n"
"font-weight: 600;\n"
"color: rgb(57, 181, 74);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.PrivacyLabel.setObjectName("PrivacyLabel")
        self.verticalLayout.addWidget(self.PrivacyLabel)
        self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_2.setMinimumSize(QtCore.QSize(305, 72))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.PolicyLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PolicyLabel.setMinimumSize(QtCore.QSize(305, 29))
        self.PolicyLabel.setStyleSheet("#PolicyLabel{\n"
"font:  16pt \"Montserrat\";\n"
"font-weight: 600;\n"
"color: rgb(57, 181, 74);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.PolicyLabel.setObjectName("PolicyLabel")
        self.verticalLayout.addWidget(self.PolicyLabel)
        self.textEdit_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_3.setMinimumSize(QtCore.QSize(305, 72))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout.addWidget(self.textEdit_3)
        self.Label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label_2.setMinimumSize(QtCore.QSize(305, 29))
        self.Label_2.setStyleSheet("#Label_2{\n"
"font:  16pt \"Montserrat\";\n"
"font-weight: 600;\n"
"color: rgb(57, 181, 74);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.Label_2.setObjectName("Label_2")
        self.verticalLayout.addWidget(self.Label_2)
        self.textEdit_4 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_4.setMinimumSize(QtCore.QSize(305, 72))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout.addWidget(self.textEdit_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.AcceptPushBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AcceptPushBtn.setGeometry(QtCore.QRect(158, 473, 115, 32))
        self.AcceptPushBtn.setStyleSheet("#AcceptPushBtn{\n"
"    font: 75 10px \"Montserrat\";\n"
"font-weight:900;\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 181, 74);\n"
"border-radius: 5px;\n"
"}")
        self.AcceptPushBtn.setObjectName("AcceptPushBtn")
        self.AcceptPushBtn.clicked.connect(self.Profile)
        self.AcceptPushBtn.clicked.connect(MainWindow.close)

        self.DeclinePushBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DeclinePushBtn.setGeometry(QtCore.QRect(294, 473, 115, 32))
        self.DeclinePushBtn.setStyleSheet("#DeclinePushBtn{\n"
"font: 75 10px \"Montserrat\";\n"
"font-weight:900;\n"
"    color: rgb(0, 0, 0);\n"
"border: 2px solid #39B54A;\n"
"opacity: 1;\n"
"\n"
"}")
        self.DeclinePushBtn.setObjectName("DeclinePushBtn")

        self.DeclinePushBtn.clicked.connect(self.Profile)
        self.DeclinePushBtn.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PrivacyPolicyLabel.setText(_translate("MainWindow", "PRIVACY AND POLICY"))
        self.ConditionLabel.setText(_translate("MainWindow", "Condition Of Use"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, </p></body></html>"))
        self.PrivacyLabel.setText(_translate("MainWindow", "Privacy"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, </p></body></html>"))
        self.PolicyLabel.setText(_translate("MainWindow", "Policy"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, </p></body></html>"))
        self.Label_2.setText(_translate("MainWindow", "Policy"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, </p></body></html>"))
        self.AcceptPushBtn.setText(_translate("MainWindow", "Accept"))
        self.DeclinePushBtn.setText(_translate("MainWindow", "Decline"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_PrivacyPolicy()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
