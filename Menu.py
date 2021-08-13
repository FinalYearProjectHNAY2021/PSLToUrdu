# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon

class Ui_MainWindow_Menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MenuBackground = QtWidgets.QLabel(self.centralwidget)
        self.MenuBackground.setGeometry(QtCore.QRect(0, 0, 1024, 800))
        self.MenuBackground.setPixmap(QPixmap("./Images/MenuBackground.jpg"))
        #         self.MenuBackground.setStyleSheet("\n"
        # "#MenuBackground{\ n"
        # "background-image: url(:/newPrefix/MenuBackground.jpg);\n"
        # "\n"
        # "\n"
        # "\n"
        # "}")
        self.MenuBackground.setText("")
        self.MenuBackground.setObjectName("MenuBackground")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(276, 34, 474, 474))
        self.LogoLabel.setPixmap(QPixmap("./Images/PSL TO URDU logo-02.png"))
        # self.LogoLabel.setStyleSheet("image: url(:/newPrefix/PSL TO URDU logo-02.png);")
        self.LogoLabel.setText("")
        self.LogoLabel.setObjectName("LogoLabel")
        self.DashBoardBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DashBoardBtn.setGeometry(QtCore.QRect(231, 450, 123, 80))
        self.DashBoardBtn.setIconSize(QSize(200, 200))
        self.DashBoardBtn.setIcon(QIcon("./Images/Group 303.png"))
        self.DashBoardBtn.setStyleSheet("#DashBoardBtn{\n"
                                        "image: url(:/newPrefix/Group 303.png);\n"
                                        "background-color: transparent;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.DashBoardBtn.setText("")
        self.DashBoardBtn.setObjectName("DashBoardBtn")
        self.PSLtoUrduBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PSLtoUrduBtn.setGeometry(QtCore.QRect(383, 444, 126, 86))
        self.PSLtoUrduBtn.setIconSize(QSize(200, 200))
        self.PSLtoUrduBtn.setIcon(QIcon("./Images/Group 304.png"))
        self.PSLtoUrduBtn.setStyleSheet("#PSLtoUrduBtn{\n"
                                        "image: url(:/newPrefix/Group 304.png);\n"
                                        "background-color: transparent;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.PSLtoUrduBtn.setText("")
        self.PSLtoUrduBtn.setObjectName("PSLtoUrduBtn")
        self.AudiotoUrduBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AudiotoUrduBtn.setGeometry(QtCore.QRect(537, 450, 153, 78))
        self.AudiotoUrduBtn.setIconSize(QSize(200, 200))
        self.AudiotoUrduBtn.setIcon(QIcon("./Images/Group 305.png"))
        self.AudiotoUrduBtn.setStyleSheet("#AudiotoUrduBtn{\n"
                                          "    image: url(:/newPrefix/Group 305.png);\n"
                                          "background-color: transparent;\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "}\n"
                                          "")
        self.AudiotoUrduBtn.setText("")
        self.AudiotoUrduBtn.setObjectName("AudiotoUrduBtn")
        self.ProfileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ProfileBtn.setGeometry(QtCore.QRect(717, 455, 80, 72))
        self.ProfileBtn.setIconSize(QSize(200, 200))
        self.ProfileBtn.setIcon(QIcon("./Images/Group 306.png"))
        self.ProfileBtn.setStyleSheet("#ProfileBtn{\n"
                                      "background-color: transparent;\n"
                                      "    image: url(:/newPrefix/Group 306.png);\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "}\n"
                                      "")
        self.ProfileBtn.setText("")
        self.ProfileBtn.setObjectName("ProfileBtn")
        self.LogoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LogoutBtn.setGeometry(QtCore.QRect(825, 640, 158, 46))

        self.LogoutBtn.setStyleSheet("#LogoutBtn{\n"
                                     "font: 20px \"Montserrat\";\n"
                                     "color:rgb(16, 106, 56);\n"
                                     "    background-color: rgb(40, 232, 144);\n"
                                     "border-radius: 5px;\n"
                                     "\n"
                                     "opacity: 1;\n"
                                     "}")
        self.LogoutBtn.setObjectName("LogoutBtn")
        self.BackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BackBtn.setGeometry(QtCore.QRect(40, 640, 158, 46))
        self.BackBtn.setStyleSheet("#BackBtn{\n"
                                   "font: 20px \"Montserrat\";\n"
                                   "color:rgb(16, 106, 56);\n"
                                   "    background-color: rgb(40, 232, 144);\n"
                                   "border-radius: 5px;\n"
                                   "\n"
                                   "opacity: 1;\n"
                                   "}")
        self.BackBtn.setObjectName("BackBtn")
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
        self.LogoutBtn.setText(_translate("MainWindow", "LOGOUT"))
        self.BackBtn.setText(_translate("MainWindow", "BACK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
