# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurations.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_confWindow(object):
    def setupUi(self, confWindow):
        confWindow.setObjectName("confWindow")
        confWindow.resize(320, 240)
        font = QtGui.QFont()
        font.setPointSize(10)
        confWindow.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(confWindow)
        self.buttonBox.setGeometry(QtCore.QRect(100, 159, 120, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalFrame = QtWidgets.QFrame(confWindow)
        self.verticalFrame.setGeometry(QtCore.QRect(80, 11, 160, 131))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.baudParameter = QtWidgets.QComboBox(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.baudParameter.setFont(font)
        self.baudParameter.setAutoFillBackground(True)
        self.baudParameter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.baudParameter.setObjectName("baudParameter")
        self.verticalLayout.addWidget(self.baudParameter)
        self.label_2 = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.portParameter = QtWidgets.QComboBox(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portParameter.setFont(font)
        self.portParameter.setAutoFillBackground(True)
        self.portParameter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.portParameter.setObjectName("portParameter")
        self.verticalLayout.addWidget(self.portParameter)

        self.retranslateUi(confWindow)
        self.buttonBox.accepted.connect(confWindow.accept)
        self.buttonBox.rejected.connect(confWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(confWindow)

    def retranslateUi(self, confWindow):
        _translate = QtCore.QCoreApplication.translate
        confWindow.setWindowTitle(_translate("confWindow", "Configurations Window"))
        self.label.setText(_translate("confWindow", "Baud"))
        self.label_2.setText(_translate("confWindow", "Serial Port"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confWindow = QtWidgets.QDialog()
    ui = Ui_confWindow()
    ui.setupUi(confWindow)
    confWindow.show()
    sys.exit(app.exec_())

