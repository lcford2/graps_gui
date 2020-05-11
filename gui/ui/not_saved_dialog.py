# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\not_saved_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NotSavedDialog(object):
    def setupUi(self, NotSavedDialog):
        NotSavedDialog.setObjectName("NotSavedDialog")
        NotSavedDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        NotSavedDialog.resize(251, 133)
        self.verticalLayout = QtWidgets.QVBoxLayout(NotSavedDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(NotSavedDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(NotSavedDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NotSavedDialog)
        self.buttonBox.accepted.connect(NotSavedDialog.accept)
        self.buttonBox.rejected.connect(NotSavedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NotSavedDialog)

    def retranslateUi(self, NotSavedDialog):
        _translate = QtCore.QCoreApplication.translate
        NotSavedDialog.setWindowTitle(_translate("NotSavedDialog", "Unsaved Changes"))
        self.label.setText(_translate("NotSavedDialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Warning!</span></p><p align=\"center\">There are unsaved changes. </p><p align=\"center\">Do you want to save before closing?</p></body></html>"))
