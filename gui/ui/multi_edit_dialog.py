# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\multi_edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_multi_edit_dialog(object):
    def setupUi(self, multi_edit_dialog):
        multi_edit_dialog.setObjectName("multi_edit_dialog")
        multi_edit_dialog.resize(648, 427)
        self.gridLayout = QtWidgets.QGridLayout(multi_edit_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.combo_label = QtWidgets.QLabel(multi_edit_dialog)
        self.combo_label.setObjectName("combo_label")
        self.gridLayout.addWidget(self.combo_label, 0, 1, 1, 1)
        self.attribute_selector = QtWidgets.QListWidget(multi_edit_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attribute_selector.sizePolicy().hasHeightForWidth())
        self.attribute_selector.setSizePolicy(sizePolicy)
        self.attribute_selector.setMaximumSize(QtCore.QSize(200, 16777215))
        self.attribute_selector.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.attribute_selector.setObjectName("attribute_selector")
        item = QtWidgets.QListWidgetItem()
        self.attribute_selector.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.attribute_selector.addItem(item)
        self.gridLayout.addWidget(self.attribute_selector, 3, 1, 1, 1)
        self.editor_label = QtWidgets.QLabel(multi_edit_dialog)
        self.editor_label.setObjectName("editor_label")
        self.gridLayout.addWidget(self.editor_label, 0, 0, 1, 1)
        self.block_type_combo = QtWidgets.QComboBox(multi_edit_dialog)
        self.block_type_combo.setObjectName("block_type_combo")
        self.block_type_combo.addItem("")
        self.block_type_combo.addItem("")
        self.block_type_combo.addItem("")
        self.block_type_combo.addItem("")
        self.block_type_combo.addItem("")
        self.gridLayout.addWidget(self.block_type_combo, 1, 1, 1, 1)
        self.selector_label = QtWidgets.QLabel(multi_edit_dialog)
        self.selector_label.setObjectName("selector_label")
        self.gridLayout.addWidget(self.selector_label, 2, 1, 1, 1)
        self.attribute_editor = QtWidgets.QTableWidget(multi_edit_dialog)
        self.attribute_editor.setAcceptDrops(True)
        self.attribute_editor.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.attribute_editor.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.attribute_editor.setObjectName("attribute_editor")
        self.attribute_editor.setColumnCount(1)
        self.attribute_editor.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.attribute_editor.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.attribute_editor.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.attribute_editor.setHorizontalHeaderItem(0, item)
        self.attribute_editor.horizontalHeader().setCascadingSectionResizes(True)
        self.attribute_editor.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.attribute_editor, 1, 0, 3, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(multi_edit_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(multi_edit_dialog)
        self.buttonBox.accepted.connect(multi_edit_dialog.accept)
        self.buttonBox.rejected.connect(multi_edit_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(multi_edit_dialog)

    def retranslateUi(self, multi_edit_dialog):
        _translate = QtCore.QCoreApplication.translate
        multi_edit_dialog.setWindowTitle(_translate("multi_edit_dialog", "Dialog"))
        self.combo_label.setText(_translate("multi_edit_dialog", "Block Type Selector"))
        __sortingEnabled = self.attribute_selector.isSortingEnabled()
        self.attribute_selector.setSortingEnabled(False)
        item = self.attribute_selector.item(0)
        item.setText(_translate("multi_edit_dialog", "Attribute 1"))
        item = self.attribute_selector.item(1)
        item.setText(_translate("multi_edit_dialog", "Attribute 2"))
        self.attribute_selector.setSortingEnabled(__sortingEnabled)
        self.editor_label.setText(_translate("multi_edit_dialog", "Attribute Editor"))
        self.block_type_combo.setItemText(0, _translate("multi_edit_dialog", "Reservoirs"))
        self.block_type_combo.setItemText(1, _translate("multi_edit_dialog", "Users"))
        self.block_type_combo.setItemText(2, _translate("multi_edit_dialog", "Watersheds"))
        self.block_type_combo.setItemText(3, _translate("multi_edit_dialog", "Junctions"))
        self.block_type_combo.setItemText(4, _translate("multi_edit_dialog", "Inter-basin Transfers"))
        self.selector_label.setText(_translate("multi_edit_dialog", "Attribute Selector"))
        item = self.attribute_editor.verticalHeaderItem(0)
        item.setText(_translate("multi_edit_dialog", "R1"))
        item = self.attribute_editor.verticalHeaderItem(1)
        item.setText(_translate("multi_edit_dialog", "R2"))
        item = self.attribute_editor.horizontalHeaderItem(0)
        item.setText(_translate("multi_edit_dialog", "Attribute"))
