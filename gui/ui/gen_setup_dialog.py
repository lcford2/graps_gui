# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gen_setup_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_genSet_dialog(object):
    def setupUi(self, genSet_dialog):
        genSet_dialog.setObjectName("genSet_dialog")
        genSet_dialog.resize(573, 423)
        self.gridLayout = QtWidgets.QGridLayout(genSet_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(genSet_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.userDescription = QtWidgets.QTabWidget(genSet_dialog)
        self.userDescription.setObjectName("userDescription")
        self.userDescription_tab = QtWidgets.QWidget()
        self.userDescription_tab.setObjectName("userDescription_tab")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.userDescription_tab)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gen_setup_box = QtWidgets.QGroupBox(self.userDescription_tab)
        self.gen_setup_box.setObjectName("gen_setup_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gen_setup_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.time_step = QtWidgets.QLabel(self.gen_setup_box)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.time_step.setFont(font)
        self.time_step.setObjectName("time_step")
        self.gridLayout_3.addWidget(self.time_step, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.time_step_input = QtWidgets.QLineEdit(self.gen_setup_box)
        self.time_step_input.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_step_input.sizePolicy().hasHeightForWidth())
        self.time_step_input.setSizePolicy(sizePolicy)
        self.time_step_input.setFrame(True)
        self.time_step_input.setObjectName("time_step_input")
        self.gridLayout_3.addWidget(self.time_step_input, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 4, 1, 1)
        self.restrictions_level = QtWidgets.QLabel(self.gen_setup_box)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.restrictions_level.setFont(font)
        self.restrictions_level.setObjectName("restrictions_level")
        self.gridLayout_3.addWidget(self.restrictions_level, 1, 0, 1, 1)
        self.restrictions_input = QtWidgets.QLineEdit(self.gen_setup_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restrictions_input.sizePolicy().hasHeightForWidth())
        self.restrictions_input.setSizePolicy(sizePolicy)
        self.restrictions_input.setObjectName("restrictions_input")
        self.gridLayout_3.addWidget(self.restrictions_input, 1, 2, 1, 1)
        self.hydro_coeff_label = QtWidgets.QLabel(self.gen_setup_box)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hydro_coeff_label.setFont(font)
        self.hydro_coeff_label.setObjectName("hydro_coeff_label")
        self.gridLayout_3.addWidget(self.hydro_coeff_label, 2, 0, 1, 1)
        self.hydro_coeff_input = QtWidgets.QLineEdit(self.gen_setup_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hydro_coeff_input.sizePolicy().hasHeightForWidth())
        self.hydro_coeff_input.setSizePolicy(sizePolicy)
        self.hydro_coeff_input.setObjectName("hydro_coeff_input")
        self.gridLayout_3.addWidget(self.hydro_coeff_input, 2, 2, 1, 1)
        self.gridLayout_14.addWidget(self.gen_setup_box, 0, 0, 1, 1)
        self.simulationbox = QtWidgets.QGroupBox(self.userDescription_tab)
        self.simulationbox.setObjectName("simulationbox")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.simulationbox)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.type_of_sim = QtWidgets.QLabel(self.simulationbox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.type_of_sim.setFont(font)
        self.type_of_sim.setObjectName("type_of_sim")
        self.gridLayout_17.addWidget(self.type_of_sim, 1, 0, 1, 1)
        self.sim_info_frame = QtWidgets.QGroupBox(self.simulationbox)
        self.sim_info_frame.setTitle("")
        self.sim_info_frame.setObjectName("sim_info_frame")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.sim_info_frame)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.num_years = QtWidgets.QLabel(self.sim_info_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_years.setFont(font)
        self.num_years.setObjectName("num_years")
        self.gridLayout_19.addWidget(self.num_years, 0, 0, 1, 1)
        self.year_input = QtWidgets.QLineEdit(self.sim_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_input.sizePolicy().hasHeightForWidth())
        self.year_input.setSizePolicy(sizePolicy)
        self.year_input.setObjectName("year_input")
        self.gridLayout_19.addWidget(self.year_input, 0, 2, 1, 1)
        self.ensem_input = QtWidgets.QLineEdit(self.sim_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ensem_input.sizePolicy().hasHeightForWidth())
        self.ensem_input.setSizePolicy(sizePolicy)
        self.ensem_input.setObjectName("ensem_input")
        self.gridLayout_19.addWidget(self.ensem_input, 1, 2, 1, 1)
        self.num_ensembles = QtWidgets.QLabel(self.sim_info_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.num_ensembles.setFont(font)
        self.num_ensembles.setObjectName("num_ensembles")
        self.gridLayout_19.addWidget(self.num_ensembles, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_17.addWidget(self.sim_info_frame, 2, 0, 1, 2)
        self.type_sim_combo = QtWidgets.QComboBox(self.simulationbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_sim_combo.sizePolicy().hasHeightForWidth())
        self.type_sim_combo.setSizePolicy(sizePolicy)
        self.type_sim_combo.setMinimumSize(QtCore.QSize(0, 0))
        self.type_sim_combo.setObjectName("type_sim_combo")
        self.type_sim_combo.addItem("")
        self.type_sim_combo.addItem("")
        self.type_sim_combo.addItem("")
        self.gridLayout_17.addWidget(self.type_sim_combo, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem4, 2, 2, 1, 1)
        self.gridLayout_14.addWidget(self.simulationbox, 1, 0, 1, 1)
        self.userDescription.addTab(self.userDescription_tab, "")
        self.forecast_tab = QtWidgets.QWidget()
        self.forecast_tab.setObjectName("forecast_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.forecast_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.analysis_option = QtWidgets.QGroupBox(self.forecast_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysis_option.sizePolicy().hasHeightForWidth())
        self.analysis_option.setSizePolicy(sizePolicy)
        self.analysis_option.setObjectName("analysis_option")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.analysis_option)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.retro_button = QtWidgets.QRadioButton(self.analysis_option)
        self.retro_button.setObjectName("retro_button")
        self.verticalLayout_7.addWidget(self.retro_button)
        self.adaptive_button = QtWidgets.QRadioButton(self.analysis_option)
        self.adaptive_button.setObjectName("adaptive_button")
        self.verticalLayout_7.addWidget(self.adaptive_button)
        self.verticalLayout.addWidget(self.analysis_option)
        self.adaptive_box = QtWidgets.QGroupBox(self.forecast_tab)
        self.adaptive_box.setObjectName("adaptive_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.adaptive_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.num_years_sim = QtWidgets.QLabel(self.adaptive_box)
        self.num_years_sim.setObjectName("num_years_sim")
        self.gridLayout_2.addWidget(self.num_years_sim, 0, 0, 1, 1)
        self.year_sim_input = QtWidgets.QLineEdit(self.adaptive_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_sim_input.sizePolicy().hasHeightForWidth())
        self.year_sim_input.setSizePolicy(sizePolicy)
        self.year_sim_input.setObjectName("year_sim_input")
        self.gridLayout_2.addWidget(self.year_sim_input, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 2, 1, 1)
        self.sim_input_table = QtWidgets.QTableWidget(self.adaptive_box)
        self.sim_input_table.setAutoFillBackground(False)
        self.sim_input_table.setRowCount(1)
        self.sim_input_table.setColumnCount(1)
        self.sim_input_table.setObjectName("sim_input_table")
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.sim_input_table.setItem(0, 0, item)
        self.sim_input_table.horizontalHeader().setVisible(False)
        self.sim_input_table.horizontalHeader().setCascadingSectionResizes(True)
        self.sim_input_table.horizontalHeader().setHighlightSections(True)
        self.sim_input_table.horizontalHeader().setSortIndicatorShown(True)
        self.sim_input_table.verticalHeader().setVisible(False)
        self.sim_input_table.verticalHeader().setHighlightSections(True)
        self.gridLayout_2.addWidget(self.sim_input_table, 2, 0, 1, 3)
        self.verticalLayout.addWidget(self.adaptive_box)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.userDescription.addTab(self.forecast_tab, "")
        self.gridLayout.addWidget(self.userDescription, 0, 0, 1, 1)

        self.retranslateUi(genSet_dialog)
        self.userDescription.setCurrentIndex(0)
        self.buttonBox.accepted.connect(genSet_dialog.accept)
        self.buttonBox.rejected.connect(genSet_dialog.reject)
        self.adaptive_button.toggled['bool'].connect(self.adaptive_box.setVisible)
        QtCore.QMetaObject.connectSlotsByName(genSet_dialog)
        genSet_dialog.setTabOrder(self.year_input, self.ensem_input)
        genSet_dialog.setTabOrder(self.ensem_input, self.retro_button)
        genSet_dialog.setTabOrder(self.retro_button, self.adaptive_button)
        genSet_dialog.setTabOrder(self.adaptive_button, self.year_sim_input)
        genSet_dialog.setTabOrder(self.year_sim_input, self.sim_input_table)
        genSet_dialog.setTabOrder(self.sim_input_table, self.buttonBox)
        genSet_dialog.setTabOrder(self.buttonBox, self.userDescription)

    def retranslateUi(self, genSet_dialog):
        _translate = QtCore.QCoreApplication.translate
        genSet_dialog.setWindowTitle(_translate("genSet_dialog", "General Setup"))
        self.gen_setup_box.setTitle(_translate("genSet_dialog", "General Setup"))
        self.time_step.setText(_translate("genSet_dialog", "Number of time steps"))
        self.restrictions_level.setText(_translate("genSet_dialog", "Number of restictions level"))
        self.hydro_coeff_label.setText(_translate("genSet_dialog", "Hydropower conversion coefficient"))
        self.simulationbox.setTitle(_translate("genSet_dialog", "Simulation"))
        self.type_of_sim.setText(_translate("genSet_dialog", "Type of Simulation"))
        self.num_years.setText(_translate("genSet_dialog", "Number of years"))
        self.num_ensembles.setText(_translate("genSet_dialog", "Number of ensembles"))
        self.type_sim_combo.setItemText(0, _translate("genSet_dialog", "Climatology"))
        self.type_sim_combo.setItemText(1, _translate("genSet_dialog", "Forecast"))
        self.type_sim_combo.setItemText(2, _translate("genSet_dialog", "Zero Flow"))
        self.userDescription.setTabText(self.userDescription.indexOf(self.userDescription_tab), _translate("genSet_dialog", "User Description"))
        self.analysis_option.setTitle(_translate("genSet_dialog", "Select Option"))
        self.retro_button.setText(_translate("genSet_dialog", "Restrospective Analysis"))
        self.adaptive_button.setText(_translate("genSet_dialog", "Adaptive Forecasts"))
        self.adaptive_box.setTitle(_translate("genSet_dialog", "Adaptive Forecasts"))
        self.num_years_sim.setText(_translate("genSet_dialog", "Number of years of simulations"))
        __sortingEnabled = self.sim_input_table.isSortingEnabled()
        self.sim_input_table.setSortingEnabled(False)
        self.sim_input_table.setSortingEnabled(__sortingEnabled)
        self.userDescription.setTabText(self.userDescription.indexOf(self.forecast_tab), _translate("genSet_dialog", "Forecast"))
