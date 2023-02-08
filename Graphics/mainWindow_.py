# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 800))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_tracking = QtWidgets.QCheckBox(self.centralwidget)
        self.show_tracking.setGeometry(QtCore.QRect(270, 650, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_tracking.setFont(font)
        self.show_tracking.setAutoFillBackground(True)
        self.show_tracking.setObjectName("show_tracking")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 190, 781, 411))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName("graphicsView")
        self.connectButtom = QtWidgets.QPushButton(self.centralwidget)
        self.connectButtom.setGeometry(QtCore.QRect(440, 690, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.connectButtom.setFont(font)
        self.connectButtom.setObjectName("connectButtom")
        self.confButtom = QtWidgets.QPushButton(self.centralwidget)
        self.confButtom.setGeometry(QtCore.QRect(40, 690, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confButtom.setFont(font)
        self.confButtom.setObjectName("confButtom")
        self.exitButtom = QtWidgets.QPushButton(self.centralwidget)
        self.exitButtom.setGeometry(QtCore.QRect(954, 690, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exitButtom.setFont(font)
        self.exitButtom.setObjectName("exitButtom")
        self.logo_u = QtWidgets.QLabel(self.centralwidget)
        self.logo_u.setGeometry(QtCore.QRect(50, 10, 200, 94))
        self.logo_u.setText("")
        self.logo_u.setPixmap(QtGui.QPixmap("logo uptc negro.png"))
        self.logo_u.setScaledContents(True)
        self.logo_u.setObjectName("logo_u")
        self.vigilado = QtWidgets.QLabel(self.centralwidget)
        self.vigilado.setGeometry(QtCore.QRect(50, 110, 200, 11))
        self.vigilado.setText("")
        self.vigilado.setPixmap(QtGui.QPixmap("vigilado_pos_jpg.png"))
        self.vigilado.setScaledContents(True)
        self.vigilado.setObjectName("vigilado")
        self.logo_gira = QtWidgets.QLabel(self.centralwidget)
        self.logo_gira.setGeometry(QtCore.QRect(1060, 14, 187, 105))
        self.logo_gira.setText("")
        self.logo_gira.setPixmap(QtGui.QPixmap("Logo GIRA.png"))
        self.logo_gira.setScaledContents(True)
        self.logo_gira.setObjectName("logo_gira")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 20, 1281, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(860, 250, 183, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.gridFrame = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.CurrentX = QtWidgets.QLineEdit(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CurrentX.setFont(font)
        self.CurrentX.setObjectName("CurrentX")
        self.gridLayout_2.addWidget(self.CurrentX, 0, 1, 1, 1)
        self.CurrentY = QtWidgets.QLineEdit(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CurrentY.setFont(font)
        self.CurrentY.setObjectName("CurrentY")
        self.gridLayout_2.addWidget(self.CurrentY, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.CurrentPhi = QtWidgets.QLineEdit(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CurrentPhi.setFont(font)
        self.CurrentPhi.setObjectName("CurrentPhi")
        self.gridLayout_2.addWidget(self.CurrentPhi, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.gridFrame)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1060, 421, 181, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalFrame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadFileButtom = QtWidgets.QPushButton(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loadFileButtom.setFont(font)
        self.loadFileButtom.setObjectName("loadFileButtom")
        self.horizontalLayout.addWidget(self.loadFileButtom)
        self.save = QtWidgets.QPushButton(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.verticalLayout_2.addWidget(self.horizontalFrame)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1060, 250, 183, 168))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.gridFrame1 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.gridFrame1.setObjectName("gridFrame1")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame1)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridFrame1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.positionX = QtWidgets.QLineEdit(self.gridFrame1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.positionX.setFont(font)
        self.positionX.setObjectName("positionX")
        self.gridLayout.addWidget(self.positionX, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridFrame1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.angle_phi = QtWidgets.QLineEdit(self.gridFrame1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.angle_phi.setFont(font)
        self.angle_phi.setObjectName("angle_phi")
        self.gridLayout.addWidget(self.angle_phi, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridFrame1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.positionY = QtWidgets.QLineEdit(self.gridFrame1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.positionY.setFont(font)
        self.positionY.setObjectName("positionY")
        self.gridLayout.addWidget(self.positionY, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.gridFrame1)
        self.sendConfigurationButtom = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sendConfigurationButtom.setFont(font)
        self.sendConfigurationButtom.setObjectName("sendConfigurationButtom")
        self.verticalLayout.addWidget(self.sendConfigurationButtom)
        self.checkConsole = QtWidgets.QCheckBox(self.centralwidget)
        self.checkConsole.setGeometry(QtCore.QRect(850, 500, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkConsole.setFont(font)
        self.checkConsole.setAutoFillBackground(True)
        self.checkConsole.setObjectName("checkConsole")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(620, 695, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status.setFont(font)
        self.status.setStyleSheet("background-color: red")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.console = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(849, 529, 390, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.console.setFont(font)
        self.console.setStyleSheet("background-color: rgb(239, 235, 231)")
        self.console.setObjectName("console")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(830, 170, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAcceptDrops(False)
        self.label_10.setAutoFillBackground(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(920, 200, 261, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAutoFillBackground(True)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.robot_id = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.robot_id.setFont(font)
        self.robot_id.setAutoFillBackground(True)
        self.robot_id.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.robot_id.setObjectName("robot_id")
        self.horizontalLayout_2.addWidget(self.robot_id)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(860, 420, 191, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAutoFillBackground(True)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.control_type = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.control_type.setFont(font)
        self.control_type.setAutoFillBackground(True)
        self.control_type.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.control_type.setObjectName("control_type")
        self.verticalLayout_5.addWidget(self.control_type)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(620, 670, 181, 24))
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAutoFillBackground(True)
        self.label_13.setObjectName("label_13")
        self.size_x = QtWidgets.QLineEdit(self.centralwidget)
        self.size_x.setGeometry(QtCore.QRect(320, 610, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.size_x.setFont(font)
        self.size_x.setObjectName("size_x")
        self.set_size = QtWidgets.QPushButton(self.centralwidget)
        self.set_size.setGeometry(QtCore.QRect(480, 610, 84, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.set_size.setFont(font)
        self.set_size.setObjectName("set_size")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(190, 610, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(390, 610, 16, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAutoFillBackground(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(300, 610, 16, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAutoFillBackground(True)
        self.label_16.setObjectName("label_16")
        self.size_y = QtWidgets.QLineEdit(self.centralwidget)
        self.size_y.setGeometry(QtCore.QRect(410, 610, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.size_y.setFont(font)
        self.size_y.setObjectName("size_y")
        self.play_pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_pause_button.setGeometry(QtCore.QRect(710, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.play_pause_button.setFont(font)
        self.play_pause_button.setText("")
        self.play_pause_button.setObjectName("play_pause_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(770, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clear_button.setFont(font)
        self.clear_button.setText("")
        self.clear_button.setObjectName("clear_button")
        self.discoveryButtom = QtWidgets.QPushButton(self.centralwidget)
        self.discoveryButtom.setGeometry(QtCore.QRect(650, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.discoveryButtom.setFont(font)
        self.discoveryButtom.setText("")
        self.discoveryButtom.setObjectName("discoveryButtom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConfiguration = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionConfiguration.setFont(font)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.actionConfiguration)
        self.menuMenu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MULTIROBOT BASE STATION CONTROL ENVIRONMENT"))
        self.show_tracking.setText(_translate("MainWindow", "Show Tracking"))
        self.connectButtom.setText(_translate("MainWindow", "Connect"))
        self.confButtom.setText(_translate("MainWindow", "Configurations"))
        self.exitButtom.setText(_translate("MainWindow", "Exit"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">MULTIROBOT BASE STATION</p><p align=\"center\">CONTROL ENVIRONMENT</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CURRENT POSE</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Position Y"))
        self.label_9.setText(_translate("MainWindow", "Angle phi"))
        self.label_8.setText(_translate("MainWindow", "Position X"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">FILE MANAGER</p></body></html>"))
        self.loadFileButtom.setText(_translate("MainWindow", "Load"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "GOAL POSE"))
        self.label.setText(_translate("MainWindow", "Position X"))
        self.label_4.setText(_translate("MainWindow", "Angle theta"))
        self.label_2.setText(_translate("MainWindow", "Position Y"))
        self.sendConfigurationButtom.setText(_translate("MainWindow", "Send"))
        self.checkConsole.setText(_translate("MainWindow", "Show Console"))
        self.status.setText(_translate("MainWindow", "Not Connected"))
        self.label_10.setText(_translate("MainWindow", "ROBOT PLACEMENT"))
        self.label_12.setText(_translate("MainWindow", "Robot ID"))
        self.label_11.setText(_translate("MainWindow", "CONTROL TYPE"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">STATUS</p></body></html>"))
        self.size_x.setText(_translate("MainWindow", "2"))
        self.set_size.setText(_translate("MainWindow", "Set"))
        self.label_14.setText(_translate("MainWindow", "Arena size"))
        self.label_15.setText(_translate("MainWindow", "Y"))
        self.label_16.setText(_translate("MainWindow", "X"))
        self.size_y.setText(_translate("MainWindow", "2"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionConfiguration.setText(_translate("MainWindow", "Configurations"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

