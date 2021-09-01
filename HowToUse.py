# Form implementation generated from reading ui file 'HowToUse.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.label.setStyleSheet("background-image: url(:/newPrefix/HowToUseBg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.BackPushBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BackPushBtn.setGeometry(QtCore.QRect(34, 32, 25, 19))
        self.BackPushBtn.setStyleSheet("#BackPushBtn{\n"
"image: url(:/newPrefix/BackBtnIcon.png);\n"
"background: transparent;\n"
"opacity: 1;\n"
"}")
        self.BackPushBtn.setText("")
        self.BackPushBtn.setObjectName("BackPushBtn")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(421, 28, 191, 51))
        self.plainTextEdit.setStyleSheet("#plainTextEdit{\n"
"font: 23px \"Montserrat\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"\n"
"\n"
"\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.scrollAreahowtoUse = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreahowtoUse.setGeometry(QtCore.QRect(70, 90, 903, 586))
        self.scrollAreahowtoUse.setStyleSheet("background-color:transparent;")
        self.scrollAreahowtoUse.setWidgetResizable(True)
        self.scrollAreahowtoUse.setObjectName("scrollAreahowtoUse")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1563, 567))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMinimumSize(QtCore.QSize(511, 548))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/PslToUrduHowToUse.jpg);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setMinimumSize(QtCore.QSize(511, 0))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/AudioToUrduHowToUse.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setMinimumSize(QtCore.QSize(511, 0))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/TextToAudioHowToUse.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.scrollAreahowtoUse.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "HOW TO USE"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
