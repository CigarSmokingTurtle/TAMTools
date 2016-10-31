# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UrlParser.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class JSONParserWIDGET(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("JSON Formatter")
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(800, 600))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(690, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.originalJSONWindow = QtWidgets.QTextEdit(Dialog)
        self.originalJSONWindow.setGeometry(QtCore.QRect(20, 50, 761, 87))
        self.originalJSONWindow.setObjectName("originalJSONWindow")
        self.parsedJSONWindow = QtWidgets.QTextEdit(Dialog)
        self.parsedJSONWindow.setGeometry(QtCore.QRect(20, 170, 761, 411))
        self.parsedJSONWindow.setObjectName("parsedJSONWindow")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 131, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "JSON Formatter"))
        self.pushButton.setText(_translate("Dialog", "Format"))
        self.label.setText(_translate("Dialog", "Original JSON:"))
        self.label_2.setText(_translate("Dialog", "Formatted JSON:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = JSONParserWIDGET()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

