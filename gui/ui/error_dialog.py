# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\error_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        ErrorDialog.setObjectName("ErrorDialog")
        ErrorDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ErrorDialog.resize(247, 108)
        self.verticalLayout = QtWidgets.QVBoxLayout(ErrorDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ErrorDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(ErrorDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ErrorDialog)
        self.buttonBox.accepted.connect(ErrorDialog.accept)
        self.buttonBox.rejected.connect(ErrorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ErrorDialog)

    def retranslateUi(self, ErrorDialog):
        _translate = QtCore.QCoreApplication.translate
        ErrorDialog.setWindowTitle(_translate("ErrorDialog", "Dialog"))
        self.label.setText(_translate("ErrorDialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Error: Complete the General Setup</span></p><p align=\"center\"><span style=\" font-weight:600;\"> before editing this node</span></p></body></html>"))
