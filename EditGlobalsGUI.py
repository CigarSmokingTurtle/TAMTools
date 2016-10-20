# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editGlobalsGUI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class EditGlobalsWIDGET(object):
    def setupUi(self, globalsEditor):
        globalsEditor.setObjectName("globalsEditor")
        globalsEditor.resize(654, 476)
        globalsEditor.setMinimumSize(QtCore.QSize(654, 476))
        globalsEditor.setMaximumSize(QtCore.QSize(654, 476))
        self.columnView = QtWidgets.QColumnView(globalsEditor)
        self.columnView.setGeometry(QtCore.QRect(10, 50, 581, 411))
        self.columnView.setObjectName("columnView")
        self.comboBox = QtWidgets.QComboBox(globalsEditor)
        self.comboBox.setGeometry(QtCore.QRect(90, 10, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(globalsEditor)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(globalsEditor)
        self.pushButton.setGeometry(QtCore.QRect(600, 50, 41, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(globalsEditor)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 100, 41, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(globalsEditor)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 10, 61, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(globalsEditor)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 10, 61, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(globalsEditor)
        QtCore.QMetaObject.connectSlotsByName(globalsEditor)

    def retranslateUi(self, globalsEditor):
        _translate = QtCore.QCoreApplication.translate
        globalsEditor.setWindowTitle(_translate("globalsEditor", "Edit Globals"))
        self.comboBox.setItemText(0, _translate("globalsEditor", "default"))
        self.label.setText(_translate("globalsEditor", "Environment:"))
        self.pushButton.setText(_translate("globalsEditor", "+"))
        self.pushButton_2.setText(_translate("globalsEditor", "-"))
        self.pushButton_3.setText(_translate("globalsEditor", "Add"))
        self.pushButton_4.setText(_translate("globalsEditor", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    globalsEditor = QtWidgets.QDialog()
    ui = editGlobalsWIDGET()
    ui.setupUi(globalsEditor)
    globalsEditor.show()
    sys.exit(app.exec_())

