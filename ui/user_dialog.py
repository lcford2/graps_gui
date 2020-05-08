# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\user_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_dialog(object):
    def setupUi(self, user_dialog):
        user_dialog.setObjectName("user_dialog")
        user_dialog.resize(851, 471)
        self.gridLayout = QtWidgets.QGridLayout(user_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(user_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.user_name_display = QtWidgets.QLineEdit(user_dialog)
        self.user_name_display.setEnabled(False)
        self.user_name_display.setAcceptDrops(True)
        self.user_name_display.setObjectName("user_name_display")
        self.gridLayout.addWidget(self.user_name_display, 2, 0, 1, 1)
        self.user_dia_tab = QtWidgets.QTabWidget(user_dialog)
        self.user_dia_tab.setObjectName("user_dia_tab")
        self.descrip_tab = QtWidgets.QWidget()
        self.descrip_tab.setObjectName("descrip_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.descrip_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.descrip_box = QtWidgets.QGroupBox(self.descrip_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descrip_box.sizePolicy().hasHeightForWidth())
        self.descrip_box.setSizePolicy(sizePolicy)
        self.descrip_box.setObjectName("descrip_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.descrip_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.user_id_label = QtWidgets.QLabel(self.descrip_box)
        self.user_id_label.setObjectName("user_id_label")
        self.gridLayout_3.addWidget(self.user_id_label, 0, 0, 1, 1)
        self.user_name_label = QtWidgets.QLabel(self.descrip_box)
        self.user_name_label.setObjectName("user_name_label")
        self.gridLayout_3.addWidget(self.user_name_label, 1, 0, 1, 1)
        self.user_name_edit = QtWidgets.QLineEdit(self.descrip_box)
        self.user_name_edit.setObjectName("user_name_edit")
        self.gridLayout_3.addWidget(self.user_name_edit, 1, 1, 1, 1)
        self.user_type_label = QtWidgets.QLabel(self.descrip_box)
        self.user_type_label.setObjectName("user_type_label")
        self.gridLayout_3.addWidget(self.user_type_label, 2, 0, 1, 1)
        self.user_type_combo = QtWidgets.QComboBox(self.descrip_box)
        self.user_type_combo.setObjectName("user_type_combo")
        self.user_type_combo.addItem("")
        self.user_type_combo.addItem("")
        self.user_type_combo.addItem("")
        self.user_type_combo.addItem("")
        self.user_type_combo.addItem("")
        self.gridLayout_3.addWidget(self.user_type_combo, 2, 1, 1, 1)
        self.min_release_label = QtWidgets.QLabel(self.descrip_box)
        self.min_release_label.setObjectName("min_release_label")
        self.gridLayout_3.addWidget(self.min_release_label, 3, 0, 1, 1)
        self.min_release_edit = QtWidgets.QLineEdit(self.descrip_box)
        self.min_release_edit.setObjectName("min_release_edit")
        self.gridLayout_3.addWidget(self.min_release_edit, 3, 1, 1, 1)
        self.min_release_unit = QtWidgets.QLabel(self.descrip_box)
        self.min_release_unit.setObjectName("min_release_unit")
        self.gridLayout_3.addWidget(self.min_release_unit, 3, 2, 1, 1)
        self.max_release_label = QtWidgets.QLabel(self.descrip_box)
        self.max_release_label.setObjectName("max_release_label")
        self.gridLayout_3.addWidget(self.max_release_label, 4, 0, 1, 1)
        self.max_release_edit = QtWidgets.QLineEdit(self.descrip_box)
        self.max_release_edit.setObjectName("max_release_edit")
        self.gridLayout_3.addWidget(self.max_release_edit, 4, 1, 1, 1)
        self.max_release_unit = QtWidgets.QLabel(self.descrip_box)
        self.max_release_unit.setObjectName("max_release_unit")
        self.gridLayout_3.addWidget(self.max_release_unit, 4, 2, 1, 1)
        self.user_id_display = QtWidgets.QLabel(self.descrip_box)
        self.user_id_display.setObjectName("user_id_display")
        self.gridLayout_3.addWidget(self.user_id_display, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.descrip_box, 0, 0, 1, 1)
        self.contract_box = QtWidgets.QGroupBox(self.descrip_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contract_box.sizePolicy().hasHeightForWidth())
        self.contract_box.setSizePolicy(sizePolicy)
        self.contract_box.setObjectName("contract_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.contract_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.contract_restric_label = QtWidgets.QLabel(self.contract_box)
        self.contract_restric_label.setObjectName("contract_restric_label")
        self.gridLayout_2.addWidget(self.contract_restric_label, 3, 0, 1, 1)
        self.contract_restrict_unit = QtWidgets.QLabel(self.contract_box)
        self.contract_restrict_unit.setObjectName("contract_restrict_unit")
        self.gridLayout_2.addWidget(self.contract_restrict_unit, 3, 2, 1, 1)
        self.tariff_edit = QtWidgets.QLineEdit(self.contract_box)
        self.tariff_edit.setObjectName("tariff_edit")
        self.gridLayout_2.addWidget(self.tariff_edit, 0, 1, 1, 1)
        self.tariff_label = QtWidgets.QLabel(self.contract_box)
        self.tariff_label.setObjectName("tariff_label")
        self.gridLayout_2.addWidget(self.tariff_label, 0, 0, 1, 1)
        self.penalty_unit = QtWidgets.QLabel(self.contract_box)
        self.penalty_unit.setObjectName("penalty_unit")
        self.gridLayout_2.addWidget(self.penalty_unit, 1, 2, 1, 1)
        self.tariff_unit = QtWidgets.QLabel(self.contract_box)
        self.tariff_unit.setObjectName("tariff_unit")
        self.gridLayout_2.addWidget(self.tariff_unit, 0, 2, 1, 1)
        self.reliability_unit = QtWidgets.QLabel(self.contract_box)
        self.reliability_unit.setObjectName("reliability_unit")
        self.gridLayout_2.addWidget(self.reliability_unit, 2, 2, 1, 1)
        self.reliability_label = QtWidgets.QLabel(self.contract_box)
        self.reliability_label.setObjectName("reliability_label")
        self.gridLayout_2.addWidget(self.reliability_label, 2, 0, 1, 1)
        self.contract_restict_edit = QtWidgets.QLineEdit(self.contract_box)
        self.contract_restict_edit.setObjectName("contract_restict_edit")
        self.gridLayout_2.addWidget(self.contract_restict_edit, 3, 1, 1, 1)
        self.penalty_label = QtWidgets.QLabel(self.contract_box)
        self.penalty_label.setObjectName("penalty_label")
        self.gridLayout_2.addWidget(self.penalty_label, 1, 0, 1, 1)
        self.penalty_edit = QtWidgets.QLineEdit(self.contract_box)
        self.penalty_edit.setObjectName("penalty_edit")
        self.gridLayout_2.addWidget(self.penalty_edit, 1, 1, 1, 1)
        self.reliability_edit = QtWidgets.QLineEdit(self.contract_box)
        self.reliability_edit.setObjectName("reliability_edit")
        self.gridLayout_2.addWidget(self.reliability_edit, 2, 1, 1, 1)
        self.penalty_comp_label = QtWidgets.QLabel(self.contract_box)
        self.penalty_comp_label.setObjectName("penalty_comp_label")
        self.gridLayout_2.addWidget(self.penalty_comp_label, 4, 0, 1, 1)
        self.penalty_comp_edit = QtWidgets.QLineEdit(self.contract_box)
        self.penalty_comp_edit.setObjectName("penalty_comp_edit")
        self.gridLayout_2.addWidget(self.penalty_comp_edit, 4, 1, 1, 1)
        self.penalty_comp_unit = QtWidgets.QLabel(self.contract_box)
        self.penalty_comp_unit.setObjectName("penalty_comp_unit")
        self.gridLayout_2.addWidget(self.penalty_comp_unit, 4, 2, 1, 1)
        self.gridLayout_8.addWidget(self.contract_box, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 0, 2, 1, 1)
        self.user_dia_tab.addTab(self.descrip_tab, "")
        self.demand_tab = QtWidgets.QWidget()
        self.demand_tab.setObjectName("demand_tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.demand_tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.demand_data_box = QtWidgets.QGroupBox(self.demand_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demand_data_box.sizePolicy().hasHeightForWidth())
        self.demand_data_box.setSizePolicy(sizePolicy)
        self.demand_data_box.setMaximumSize(QtCore.QSize(16777215, 120))
        self.demand_data_box.setObjectName("demand_data_box")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.demand_data_box)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.demand_table = QtWidgets.QTableWidget(self.demand_data_box)
        self.demand_table.setObjectName("demand_table")
        self.demand_table.setColumnCount(1)
        self.demand_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.demand_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.demand_table.setHorizontalHeaderItem(0, item)
        self.gridLayout_5.addWidget(self.demand_table, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.demand_data_box, 2, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem2, 4, 0, 1, 1)
        self.demand_file_box = QtWidgets.QGroupBox(self.demand_tab)
        self.demand_file_box.setObjectName("demand_file_box")
        self.formLayout = QtWidgets.QFormLayout(self.demand_file_box)
        self.formLayout.setObjectName("formLayout")
        self.demand_file_button = QtWidgets.QPushButton(self.demand_file_box)
        self.demand_file_button.setObjectName("demand_file_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.demand_file_button)
        self.demand_file_edit = QtWidgets.QLineEdit(self.demand_file_box)
        self.demand_file_edit.setEnabled(False)
        self.demand_file_edit.setObjectName("demand_file_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.demand_file_edit)
        self.gridLayout_9.addWidget(self.demand_file_box, 3, 0, 1, 2)
        self.input_method_box = QtWidgets.QGroupBox(self.demand_tab)
        self.input_method_box.setObjectName("input_method_box")
        self.formLayout_2 = QtWidgets.QFormLayout(self.input_method_box)
        self.formLayout_2.setObjectName("formLayout_2")
        self.table_radio = QtWidgets.QRadioButton(self.input_method_box)
        self.table_radio.setObjectName("table_radio")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.table_radio)
        self.file_radio = QtWidgets.QRadioButton(self.input_method_box)
        self.file_radio.setObjectName("file_radio")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.file_radio)
        self.gridLayout_9.addWidget(self.input_method_box, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 1, 1, 1, 1)
        self.user_dia_tab.addTab(self.demand_tab, "")
        self.restrict_comp_tab = QtWidgets.QWidget()
        self.restrict_comp_tab.setObjectName("restrict_comp_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.restrict_comp_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.restrict_box = QtWidgets.QGroupBox(self.restrict_comp_tab)
        self.restrict_box.setObjectName("restrict_box")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.restrict_box)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.restrict_frac_table = QtWidgets.QTableWidget(self.restrict_box)
        self.restrict_frac_table.setObjectName("restrict_frac_table")
        self.restrict_frac_table.setColumnCount(1)
        self.restrict_frac_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.restrict_frac_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.restrict_frac_table.setHorizontalHeaderItem(0, item)
        self.gridLayout_7.addWidget(self.restrict_frac_table, 3, 0, 1, 1)
        self.restrict_comp_table = QtWidgets.QTableWidget(self.restrict_box)
        self.restrict_comp_table.setObjectName("restrict_comp_table")
        self.restrict_comp_table.setColumnCount(1)
        self.restrict_comp_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.restrict_comp_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.restrict_comp_table.setHorizontalHeaderItem(0, item)
        self.gridLayout_7.addWidget(self.restrict_comp_table, 1, 0, 1, 1)
        self.restrict_comp_label = QtWidgets.QLabel(self.restrict_box)
        self.restrict_comp_label.setObjectName("restrict_comp_label")
        self.gridLayout_7.addWidget(self.restrict_comp_label, 0, 0, 1, 1)
        self.restrict_frac_label = QtWidgets.QLabel(self.restrict_box)
        self.restrict_frac_label.setObjectName("restrict_frac_label")
        self.gridLayout_7.addWidget(self.restrict_frac_label, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.restrict_box, 0, 0, 1, 1)
        self.user_dia_tab.addTab(self.restrict_comp_tab, "")
        self.hydro_tab = QtWidgets.QWidget()
        self.hydro_tab.setObjectName("hydro_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.hydro_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.num_turbines_label = QtWidgets.QLabel(self.hydro_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_turbines_label.sizePolicy().hasHeightForWidth())
        self.num_turbines_label.setSizePolicy(sizePolicy)
        self.num_turbines_label.setObjectName("num_turbines_label")
        self.gridLayout_4.addWidget(self.num_turbines_label, 0, 0, 1, 1)
        self.num_turbines_edit = QtWidgets.QLineEdit(self.hydro_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_turbines_edit.sizePolicy().hasHeightForWidth())
        self.num_turbines_edit.setSizePolicy(sizePolicy)
        self.num_turbines_edit.setObjectName("num_turbines_edit")
        self.gridLayout_4.addWidget(self.num_turbines_edit, 0, 1, 1, 1)
        self.hydropower_elev_label = QtWidgets.QLabel(self.hydro_tab)
        self.hydropower_elev_label.setObjectName("hydropower_elev_label")
        self.gridLayout_4.addWidget(self.hydropower_elev_label, 2, 0, 1, 1)
        self.hydro_elev_table = QtWidgets.QTableWidget(self.hydro_tab)
        self.hydro_elev_table.setObjectName("hydro_elev_table")
        self.hydro_elev_table.setColumnCount(1)
        self.hydro_elev_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.hydro_elev_table.setHorizontalHeaderItem(0, item)
        self.gridLayout_4.addWidget(self.hydro_elev_table, 5, 0, 1, 6)
        self.hydro_table = QtWidgets.QTableWidget(self.hydro_tab)
        self.hydro_table.setObjectName("hydro_table")
        self.hydro_table.setColumnCount(6)
        self.hydro_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.hydro_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hydro_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hydro_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hydro_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.hydro_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.hydro_table.setHorizontalHeaderItem(5, item)
        self.gridLayout_4.addWidget(self.hydro_table, 1, 0, 1, 6)
        self.elev_file_edit = QtWidgets.QLineEdit(self.hydro_tab)
        self.elev_file_edit.setEnabled(False)
        self.elev_file_edit.setObjectName("elev_file_edit")
        self.gridLayout_4.addWidget(self.elev_file_edit, 4, 1, 1, 1)
        self.elev_file_button = QtWidgets.QPushButton(self.hydro_tab)
        self.elev_file_button.setObjectName("elev_file_button")
        self.gridLayout_4.addWidget(self.elev_file_button, 4, 0, 1, 1)
        self.input_method_box_2 = QtWidgets.QGroupBox(self.hydro_tab)
        self.input_method_box_2.setObjectName("input_method_box_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.input_method_box_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.file_radio_2 = QtWidgets.QRadioButton(self.input_method_box_2)
        self.file_radio_2.setObjectName("file_radio_2")
        self.gridLayout_10.addWidget(self.file_radio_2, 1, 0, 1, 1)
        self.table_radio_2 = QtWidgets.QRadioButton(self.input_method_box_2)
        self.table_radio_2.setObjectName("table_radio_2")
        self.gridLayout_10.addWidget(self.table_radio_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.input_method_box_2, 3, 0, 1, 1)
        self.user_dia_tab.addTab(self.hydro_tab, "")
        self.gridLayout.addWidget(self.user_dia_tab, 0, 0, 1, 2)
        self.user_name_label.setBuddy(self.user_name_edit)
        self.user_type_label.setBuddy(self.user_type_combo)
        self.min_release_label.setBuddy(self.min_release_edit)
        self.max_release_label.setBuddy(self.max_release_edit)
        self.contract_restric_label.setBuddy(self.contract_restict_edit)
        self.tariff_label.setBuddy(self.tariff_edit)
        self.reliability_label.setBuddy(self.reliability_edit)
        self.penalty_label.setBuddy(self.penalty_edit)
        self.penalty_comp_label.setBuddy(self.penalty_comp_edit)
        self.restrict_comp_label.setBuddy(self.restrict_comp_table)
        self.restrict_frac_label.setBuddy(self.restrict_frac_table)
        self.num_turbines_label.setBuddy(self.num_turbines_edit)

        self.retranslateUi(user_dialog)
        self.user_dia_tab.setCurrentIndex(0)
        self.buttonBox.accepted.connect(user_dialog.accept)
        self.buttonBox.rejected.connect(user_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(user_dialog)
        user_dialog.setTabOrder(self.user_name_edit, self.user_type_combo)
        user_dialog.setTabOrder(self.user_type_combo, self.min_release_edit)
        user_dialog.setTabOrder(self.min_release_edit, self.max_release_edit)
        user_dialog.setTabOrder(self.max_release_edit, self.tariff_edit)
        user_dialog.setTabOrder(self.tariff_edit, self.penalty_edit)
        user_dialog.setTabOrder(self.penalty_edit, self.reliability_edit)
        user_dialog.setTabOrder(self.reliability_edit, self.contract_restict_edit)
        user_dialog.setTabOrder(self.contract_restict_edit, self.demand_table)
        user_dialog.setTabOrder(self.demand_table, self.restrict_comp_table)
        user_dialog.setTabOrder(self.restrict_comp_table, self.restrict_frac_table)
        user_dialog.setTabOrder(self.restrict_frac_table, self.hydro_table)
        user_dialog.setTabOrder(self.hydro_table, self.buttonBox)
        user_dialog.setTabOrder(self.buttonBox, self.user_name_display)
        user_dialog.setTabOrder(self.user_name_display, self.user_dia_tab)

    def retranslateUi(self, user_dialog):
        _translate = QtCore.QCoreApplication.translate
        user_dialog.setWindowTitle(_translate("user_dialog", "User"))
        self.descrip_box.setTitle(_translate("user_dialog", "Description"))
        self.user_id_label.setText(_translate("user_dialog", "User ID"))
        self.user_name_label.setText(_translate("user_dialog", "User Name"))
        self.user_type_label.setText(_translate("user_dialog", "User Type"))
        self.user_type_combo.setItemText(0, _translate("user_dialog", "Municipal"))
        self.user_type_combo.setItemText(1, _translate("user_dialog", "Industry"))
        self.user_type_combo.setItemText(2, _translate("user_dialog", "Agricultural"))
        self.user_type_combo.setItemText(3, _translate("user_dialog", "Hydropower"))
        self.user_type_combo.setItemText(4, _translate("user_dialog", "Environmental"))
        self.min_release_label.setText(_translate("user_dialog", "Minimum Release"))
        self.min_release_unit.setText(_translate("user_dialog", "<html><head/><body><p>Mm<span style=\" vertical-align:super;\">3</span></p></body></html>"))
        self.max_release_label.setText(_translate("user_dialog", "Maximum Release"))
        self.max_release_unit.setText(_translate("user_dialog", "<html><head/><body><p>Mm<span style=\" vertical-align:super;\">3</span></p></body></html>"))
        self.user_id_display.setText(_translate("user_dialog", "1"))
        self.contract_box.setTitle(_translate("user_dialog", "Contract"))
        self.contract_restric_label.setText(_translate("user_dialog", "Contract Restriction Volume"))
        self.contract_restrict_unit.setText(_translate("user_dialog", "<html><head/><body><p>Mm<span style=\" vertical-align:super;\">3</span></p></body></html>"))
        self.tariff_label.setText(_translate("user_dialog", "Tariff"))
        self.penalty_unit.setText(_translate("user_dialog", "$"))
        self.tariff_unit.setText(_translate("user_dialog", "$"))
        self.reliability_unit.setText(_translate("user_dialog", "ln%"))
        self.reliability_label.setText(_translate("user_dialog", "Reliability"))
        self.penalty_label.setText(_translate("user_dialog", "Penalty"))
        self.penalty_comp_label.setText(_translate("user_dialog", "Penalty Compensation"))
        self.penalty_comp_unit.setText(_translate("user_dialog", "$"))
        self.user_dia_tab.setTabText(self.user_dia_tab.indexOf(self.descrip_tab), _translate("user_dialog", "User Description"))
        self.demand_data_box.setTitle(_translate("user_dialog", "Demand Table"))
        item = self.demand_table.verticalHeaderItem(0)
        item.setText(_translate("user_dialog", "A"))
        item = self.demand_table.horizontalHeaderItem(0)
        item.setText(_translate("user_dialog", "1"))
        self.demand_file_box.setTitle(_translate("user_dialog", "Demand Fraction File"))
        self.demand_file_button.setText(_translate("user_dialog", "Select File"))
        self.input_method_box.setTitle(_translate("user_dialog", "Input Method"))
        self.table_radio.setText(_translate("user_dialog", "Table "))
        self.file_radio.setText(_translate("user_dialog", "Input File"))
        self.user_dia_tab.setTabText(self.user_dia_tab.indexOf(self.demand_tab), _translate("user_dialog", "User Demand"))
        self.restrict_box.setTitle(_translate("user_dialog", "Restriction"))
        item = self.restrict_frac_table.verticalHeaderItem(0)
        item.setText(_translate("user_dialog", "A"))
        item = self.restrict_frac_table.horizontalHeaderItem(0)
        item.setText(_translate("user_dialog", "1"))
        item = self.restrict_comp_table.verticalHeaderItem(0)
        item.setText(_translate("user_dialog", "A"))
        item = self.restrict_comp_table.horizontalHeaderItem(0)
        item.setText(_translate("user_dialog", "1"))
        self.restrict_comp_label.setText(_translate("user_dialog", "Restriction Compensation ($)"))
        self.restrict_frac_label.setText(_translate("user_dialog", "Restriction Fraction"))
        self.user_dia_tab.setTabText(self.user_dia_tab.indexOf(self.restrict_comp_tab), _translate("user_dialog", "Restriction Compensation"))
        self.num_turbines_label.setText(_translate("user_dialog", "Number of Turbines"))
        self.hydropower_elev_label.setText(_translate("user_dialog", "Turbine Tail Elevation (m)"))
        item = self.hydro_elev_table.horizontalHeaderItem(0)
        item.setText(_translate("user_dialog", "1"))
        item = self.hydro_table.horizontalHeaderItem(0)
        item.setText(_translate("user_dialog", "Maximum Discharge (m3/sec)"))
        item = self.hydro_table.horizontalHeaderItem(1)
        item.setText(_translate("user_dialog", "Installed Capacity (MWatts)"))
        item = self.hydro_table.horizontalHeaderItem(2)
        item.setText(_translate("user_dialog", "Turbine Efficiency"))
        item = self.hydro_table.horizontalHeaderItem(3)
        item.setText(_translate("user_dialog", "Energy Coefficient 1"))
        item = self.hydro_table.horizontalHeaderItem(4)
        item.setText(_translate("user_dialog", "Energy Coefficient 2"))
        item = self.hydro_table.horizontalHeaderItem(5)
        item.setText(_translate("user_dialog", "Unit Rate Energy"))
        self.elev_file_button.setText(_translate("user_dialog", "Select File"))
        self.input_method_box_2.setTitle(_translate("user_dialog", "Input Method"))
        self.file_radio_2.setText(_translate("user_dialog", "Input File"))
        self.table_radio_2.setText(_translate("user_dialog", "Table"))
        self.user_dia_tab.setTabText(self.user_dia_tab.indexOf(self.hydro_tab), _translate("user_dialog", "Hydropower"))
