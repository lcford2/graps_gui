# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\help_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_help_dialog(object):
    def setupUi(self, help_dialog):
        help_dialog.setObjectName("help_dialog")
        help_dialog.resize(853, 749)
        self.gridLayout = QtWidgets.QGridLayout(help_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.help_view = QtWebEngineWidgets.QWebEngineView(help_dialog)
        self.help_view.setUrl(QtCore.QUrl("about:blank"))
        self.help_view.setObjectName("help_view")
        self.gridLayout.addWidget(self.help_view, 0, 0, 1, 1)

        self.retranslateUi(help_dialog)
        QtCore.QMetaObject.connectSlotsByName(help_dialog)

    def retranslateUi(self, help_dialog):
        _translate = QtCore.QCoreApplication.translate
        help_dialog.setWindowTitle(_translate("help_dialog", "Help"))
from PyQt5 import QtWebEngineWidgets
