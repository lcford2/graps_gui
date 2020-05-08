# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\junction_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_junction_dialog(object):
    def setupUi(self, junction_dialog):
        junction_dialog.setObjectName("junction_dialog")
        junction_dialog.resize(400, 142)
        junction_dialog.setWindowOpacity(1.0)
        self.gridLayout = QtWidgets.QGridLayout(junction_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(junction_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.flow_jun_name_display = QtWidgets.QLineEdit(junction_dialog)
        self.flow_jun_name_display.setEnabled(False)
        self.flow_jun_name_display.setObjectName("flow_jun_name_display")
        self.gridLayout.addWidget(self.flow_jun_name_display, 1, 0, 1, 1)
        self.jun_desc_box = QtWidgets.QGroupBox(junction_dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.jun_desc_box.sizePolicy().hasHeightForWidth())
        self.jun_desc_box.setSizePolicy(sizePolicy)
        self.jun_desc_box.setObjectName("jun_desc_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.jun_desc_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.flow_jun_id_label = QtWidgets.QLabel(self.jun_desc_box)
        self.flow_jun_id_label.setObjectName("flow_jun_id_label")
        self.gridLayout_2.addWidget(self.flow_jun_id_label, 0, 0, 1, 1)
        self.flow_jun_name_label = QtWidgets.QLabel(self.jun_desc_box)
        self.flow_jun_name_label.setObjectName("flow_jun_name_label")
        self.gridLayout_2.addWidget(self.flow_jun_name_label, 1, 0, 1, 1)
        self.flow_jun_node_edit = QtWidgets.QLineEdit(self.jun_desc_box)
        self.flow_jun_node_edit.setObjectName("flow_jun_node_edit")
        self.gridLayout_2.addWidget(self.flow_jun_node_edit, 1, 2, 1, 1)
        self.flow_jun_id_display = QtWidgets.QLabel(self.jun_desc_box)
        self.flow_jun_id_display.setObjectName("flow_jun_id_display")
        self.gridLayout_2.addWidget(self.flow_jun_id_display, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.jun_desc_box, 0, 0, 1, 2)
        self.flow_jun_name_label.setBuddy(self.flow_jun_node_edit)

        self.retranslateUi(junction_dialog)
        self.buttonBox.accepted.connect(junction_dialog.accept)
        self.buttonBox.rejected.connect(junction_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(junction_dialog)
        junction_dialog.setTabOrder(
            self.flow_jun_node_edit, self.flow_jun_name_display)
        junction_dialog.setTabOrder(self.flow_jun_name_display, self.buttonBox)

    def retranslateUi(self, junction_dialog):
        _translate = QtCore.QCoreApplication.translate
        junction_dialog.setWindowTitle(
            _translate("junction_dialog", "Junction"))
        self.jun_desc_box.setTitle(_translate(
            "junction_dialog", "Description"))
        self.flow_jun_id_label.setText(_translate(
            "junction_dialog", "Flow Junction Node ID"))
        self.flow_jun_name_label.setText(_translate(
            "junction_dialog", "Flow Junction Node Name"))
        self.flow_jun_id_display.setText(_translate("junction_dialog", "1"))
