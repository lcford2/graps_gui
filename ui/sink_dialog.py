# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sink_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sink_dialog(object):
    def setupUi(self, sink_dialog):
        sink_dialog.setObjectName("sink_dialog")
        sink_dialog.resize(529, 277)
        self.gridLayout = QtWidgets.QGridLayout(sink_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.sink_desc_box = QtWidgets.QGroupBox(sink_dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sink_desc_box.sizePolicy().hasHeightForWidth())
        self.sink_desc_box.setSizePolicy(sizePolicy)
        self.sink_desc_box.setMaximumSize(QtCore.QSize(304, 218))
        self.sink_desc_box.setObjectName("sink_desc_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sink_desc_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sink_id_label = QtWidgets.QLabel(self.sink_desc_box)
        self.sink_id_label.setObjectName("sink_id_label")
        self.gridLayout_2.addWidget(self.sink_id_label, 0, 0, 1, 1)
        self.sink_name_label = QtWidgets.QLabel(self.sink_desc_box)
        self.sink_name_label.setObjectName("sink_name_label")
        self.gridLayout_2.addWidget(self.sink_name_label, 1, 0, 1, 1)
        self.sink_name_edit = QtWidgets.QLineEdit(self.sink_desc_box)
        self.sink_name_edit.setObjectName("sink_name_edit")
        self.gridLayout_2.addWidget(self.sink_name_edit, 1, 1, 1, 1)
        self.max_store_label = QtWidgets.QLabel(self.sink_desc_box)
        self.max_store_label.setObjectName("max_store_label")
        self.gridLayout_2.addWidget(self.max_store_label, 2, 0, 1, 1)
        self.max_store_edit = QtWidgets.QLineEdit(self.sink_desc_box)
        self.max_store_edit.setObjectName("max_store_edit")
        self.gridLayout_2.addWidget(self.max_store_edit, 2, 1, 1, 1)
        self.storage_unit_label = QtWidgets.QLabel(self.sink_desc_box)
        self.storage_unit_label.setObjectName("storage_unit_label")
        self.gridLayout_2.addWidget(self.storage_unit_label, 2, 2, 1, 1)
        self.sink_id_display = QtWidgets.QLabel(self.sink_desc_box)
        self.sink_id_display.setObjectName("sink_id_display")
        self.gridLayout_2.addWidget(self.sink_id_display, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.sink_desc_box, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(sink_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(sink_dialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.sink_name_label.setBuddy(self.sink_name_edit)
        self.max_store_label.setBuddy(self.max_store_edit)

        self.retranslateUi(sink_dialog)
        self.buttonBox.accepted.connect(sink_dialog.accept)
        self.buttonBox.rejected.connect(sink_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(sink_dialog)
        sink_dialog.setTabOrder(self.sink_name_edit, self.max_store_edit)
        sink_dialog.setTabOrder(self.max_store_edit, self.lineEdit)
        sink_dialog.setTabOrder(self.lineEdit, self.buttonBox)

    def retranslateUi(self, sink_dialog):
        _translate = QtCore.QCoreApplication.translate
        sink_dialog.setWindowTitle(_translate("sink_dialog", "Sink"))
        self.sink_desc_box.setTitle(_translate("sink_dialog", "Description"))
        self.sink_id_label.setText(_translate("sink_dialog", "Sink ID"))
        self.sink_name_label.setText(_translate("sink_dialog", "Sink Name"))
        self.max_store_label.setText(
            _translate("sink_dialog", "Maximum Storage"))
        self.storage_unit_label.setText(_translate(
            "sink_dialog", "<html><head/><body><p>Mm<span style=\" vertical-align:super;\">3</span></p></body></html>"))
        self.sink_id_display.setText(_translate("sink_dialog", "1"))
