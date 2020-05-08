# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interbasin_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_interbasin_dialog(object):
    def setupUi(self, interbasin_dialog):
        interbasin_dialog.setObjectName("interbasin_dialog")
        interbasin_dialog.resize(478, 346)
        self.gridLayout = QtWidgets.QGridLayout(interbasin_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.int_basin_name_display = QtWidgets.QLineEdit(interbasin_dialog)
        self.int_basin_name_display.setEnabled(False)
        self.int_basin_name_display.setObjectName("int_basin_name_display")
        self.gridLayout.addWidget(self.int_basin_name_display, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(interbasin_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(interbasin_dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 289))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.IB_description_box = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.IB_description_box.sizePolicy().hasHeightForWidth())
        self.IB_description_box.setSizePolicy(sizePolicy)
        self.IB_description_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.IB_description_box.setObjectName("IB_description_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.IB_description_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.interbasin_id_label = QtWidgets.QLabel(self.IB_description_box)
        self.interbasin_id_label.setObjectName("interbasin_id_label")
        self.gridLayout_2.addWidget(self.interbasin_id_label, 0, 0, 1, 1)
        self.interbasin_name_label = QtWidgets.QLabel(self.IB_description_box)
        self.interbasin_name_label.setObjectName("interbasin_name_label")
        self.gridLayout_2.addWidget(self.interbasin_name_label, 1, 0, 1, 1)
        self.interbasin_name_edit = QtWidgets.QLineEdit(
            self.IB_description_box)
        self.interbasin_name_edit.setObjectName("interbasin_name_edit")
        self.gridLayout_2.addWidget(self.interbasin_name_edit, 1, 1, 1, 1)
        self.drainage_area_label = QtWidgets.QLabel(self.IB_description_box)
        self.drainage_area_label.setObjectName("drainage_area_label")
        self.gridLayout_2.addWidget(self.drainage_area_label, 2, 0, 1, 1)
        self.drainage_area_edit = QtWidgets.QLineEdit(self.IB_description_box)
        self.drainage_area_edit.setObjectName("drainage_area_edit")
        self.gridLayout_2.addWidget(self.drainage_area_edit, 2, 1, 1, 1)
        self.drainage_area_units = QtWidgets.QLabel(self.IB_description_box)
        self.drainage_area_units.setObjectName("drainage_area_units")
        self.gridLayout_2.addWidget(self.drainage_area_units, 2, 2, 1, 1)
        self.interbasin_id_display = QtWidgets.QLabel(self.IB_description_box)
        self.interbasin_id_display.setObjectName("interbasin_id_display")
        self.gridLayout_2.addWidget(self.interbasin_id_display, 0, 1, 1, 1)
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.IB_description_box)
        self.input_method_box = QtWidgets.QGroupBox(self.frame)
        self.input_method_box.setObjectName("input_method_box")
        self.formLayout_2 = QtWidgets.QFormLayout(self.input_method_box)
        self.formLayout_2.setObjectName("formLayout_2")
        self.table_radio = QtWidgets.QRadioButton(self.input_method_box)
        self.table_radio.setObjectName("table_radio")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.table_radio)
        self.file_radio = QtWidgets.QRadioButton(self.input_method_box)
        self.file_radio.setObjectName("file_radio")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.file_radio)
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.input_method_box)
        self.ave_flow_box = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ave_flow_box.sizePolicy().hasHeightForWidth())
        self.ave_flow_box.setSizePolicy(sizePolicy)
        self.ave_flow_box.setMaximumSize(QtCore.QSize(16777215, 150))
        self.ave_flow_box.setObjectName("ave_flow_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ave_flow_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.flow_file_edit = QtWidgets.QLineEdit(self.ave_flow_box)
        self.flow_file_edit.setEnabled(False)
        self.flow_file_edit.setObjectName("flow_file_edit")
        self.gridLayout_3.addWidget(self.flow_file_edit, 1, 1, 1, 1)
        self.file_button = QtWidgets.QPushButton(self.ave_flow_box)
        self.file_button.setObjectName("file_button")
        self.gridLayout_3.addWidget(self.file_button, 1, 0, 1, 1)
        self.ave_flows_table = QtWidgets.QTableWidget(self.ave_flow_box)
        self.ave_flows_table.setObjectName("ave_flows_table")
        self.ave_flows_table.setColumnCount(1)
        self.ave_flows_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.ave_flows_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ave_flows_table.setHorizontalHeaderItem(0, item)
        self.gridLayout_3.addWidget(self.ave_flows_table, 0, 0, 1, 2)
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.ave_flow_box)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.interbasin_name_label.setBuddy(self.interbasin_name_edit)
        self.drainage_area_label.setBuddy(self.drainage_area_edit)

        self.retranslateUi(interbasin_dialog)
        self.buttonBox.accepted.connect(interbasin_dialog.accept)
        self.buttonBox.rejected.connect(interbasin_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(interbasin_dialog)
        interbasin_dialog.setTabOrder(
            self.interbasin_name_edit, self.drainage_area_edit)
        interbasin_dialog.setTabOrder(
            self.drainage_area_edit, self.ave_flows_table)
        interbasin_dialog.setTabOrder(
            self.ave_flows_table, self.int_basin_name_display)
        interbasin_dialog.setTabOrder(
            self.int_basin_name_display, self.buttonBox)

    def retranslateUi(self, interbasin_dialog):
        _translate = QtCore.QCoreApplication.translate
        interbasin_dialog.setWindowTitle(
            _translate("interbasin_dialog", "Interbasin"))
        self.IB_description_box.setTitle(
            _translate("interbasin_dialog", "Description"))
        self.interbasin_id_label.setText(
            _translate("interbasin_dialog", "Interbasin ID"))
        self.interbasin_name_label.setText(
            _translate("interbasin_dialog", "Interbasin Name"))
        self.drainage_area_label.setText(
            _translate("interbasin_dialog", "Drainage Area"))
        self.drainage_area_units.setText(_translate(
            "interbasin_dialog", "<html><head/><body><p>Km<span style=\" vertical-align:super;\">2</span></p></body></html>"))
        self.interbasin_id_display.setText(
            _translate("interbasin_dialog", "1"))
        self.input_method_box.setTitle(
            _translate("interbasin_dialog", "Input Method"))
        self.table_radio.setText(_translate("interbasin_dialog", "Table"))
        self.file_radio.setText(_translate("interbasin_dialog", "Input File"))
        self.ave_flow_box.setTitle(_translate(
            "interbasin_dialog", "Average Flow (Mm3/time)"))
        self.file_button.setText(_translate(
            "interbasin_dialog", "Select File"))
        item = self.ave_flows_table.verticalHeaderItem(0)
        item.setText(_translate("interbasin_dialog", "A"))
        item = self.ave_flows_table.horizontalHeaderItem(0)
        item.setText(_translate("interbasin_dialog", "1"))
