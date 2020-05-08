# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\draw_link.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_linkDraw_dialog(object):
    def setupUi(self, linkDraw_dialog):
        linkDraw_dialog.setObjectName("linkDraw_dialog")
        linkDraw_dialog.resize(378, 234)
        linkDraw_dialog.setSizeGripEnabled(True)
        linkDraw_dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(linkDraw_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(linkDraw_dialog)
        self.groupBox.setObjectName("groupBox")
        self.start_edit = QtWidgets.QLineEdit(self.groupBox)
        self.start_edit.setGeometry(QtCore.QRect(100, 70, 51, 22))
        self.start_edit.setText("")
        self.start_edit.setObjectName("start_edit")
        self.stop_edit = QtWidgets.QLineEdit(self.groupBox)
        self.stop_edit.setGeometry(QtCore.QRect(100, 100, 51, 22))
        self.stop_edit.setText("")
        self.stop_edit.setObjectName("stop_edit")
        self.start_label = QtWidgets.QLabel(self.groupBox)
        self.start_label.setEnabled(True)
        self.start_label.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.start_label.setObjectName("start_label")
        self.stop_label = QtWidgets.QLabel(self.groupBox)
        self.stop_label.setGeometry(QtCore.QRect(20, 100, 71, 16))
        self.stop_label.setObjectName("stop_label")
        self.info_label = QtWidgets.QLabel(self.groupBox)
        self.info_label.setGeometry(QtCore.QRect(20, 20, 441, 41))
        self.info_label.setObjectName("info_label")
        self.start_edit.raise_()
        self.stop_edit.raise_()
        self.start_label.raise_()
        self.stop_label.raise_()
        self.info_label.raise_()
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(linkDraw_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Apply | QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(linkDraw_dialog)
        self.buttonBox.accepted.connect(linkDraw_dialog.accept)
        self.buttonBox.rejected.connect(linkDraw_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(linkDraw_dialog)

    def retranslateUi(self, linkDraw_dialog):
        _translate = QtCore.QCoreApplication.translate
        linkDraw_dialog.setWindowTitle(_translate("linkDraw_dialog", "Link"))
        self.groupBox.setTitle(_translate(
            "linkDraw_dialog", "Link Information"))
        self.start_label.setText(_translate("linkDraw_dialog", "Start Node:"))
        self.stop_label.setText(_translate("linkDraw_dialog", "Stop Node:"))
        self.info_label.setText(_translate("linkDraw_dialog", "Enter the node ID for the start and stop node of this link:\n"
                                           "(ex. W3, R5)"))
