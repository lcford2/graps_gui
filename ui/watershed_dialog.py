# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\watershed_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_watershed_dialog(object):
    def setupUi(self, watershed_dialog):
        watershed_dialog.setObjectName("watershed_dialog")
        watershed_dialog.resize(532, 380)
        watershed_dialog.setWindowOpacity(3.0)
        self.gridLayout = QtWidgets.QGridLayout(watershed_dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.inflows_file_box = QtWidgets.QGroupBox(watershed_dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inflows_file_box.sizePolicy().hasHeightForWidth())
        self.inflows_file_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.inflows_file_box.setFont(font)
        self.inflows_file_box.setObjectName("inflows_file_box")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.inflows_file_box)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.inflows_label = QtWidgets.QLabel(self.inflows_file_box)
        self.inflows_label.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.inflows_label.setObjectName("inflows_label")
        self.gridLayout_4.addWidget(self.inflows_label, 0, 1, 1, 1)
        self.select_inflow_file = QtWidgets.QPushButton(self.inflows_file_box)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.select_inflow_file.setFont(font)
        self.select_inflow_file.setObjectName("select_inflow_file")
        self.gridLayout_4.addWidget(self.select_inflow_file, 1, 0, 1, 1)
        self.inflows_file_input = QtWidgets.QLineEdit(self.inflows_file_box)
        self.inflows_file_input.setEnabled(False)
        self.inflows_file_input.setObjectName("inflows_file_input")
        self.gridLayout_4.addWidget(self.inflows_file_input, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.inflows_file_box, 2, 0, 1, 3)
        self.forecast_file_box = QtWidgets.QGroupBox(watershed_dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.forecast_file_box.sizePolicy().hasHeightForWidth())
        self.forecast_file_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.forecast_file_box.setFont(font)
        self.forecast_file_box.setObjectName("forecast_file_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.forecast_file_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.forecast_labe = QtWidgets.QLabel(self.forecast_file_box)
        self.forecast_labe.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.forecast_labe.setObjectName("forecast_labe")
        self.gridLayout_3.addWidget(self.forecast_labe, 3, 1, 1, 1)
        self.forecast_file_input = QtWidgets.QLineEdit(self.forecast_file_box)
        self.forecast_file_input.setEnabled(False)
        self.forecast_file_input.setObjectName("forecast_file_input")
        self.gridLayout_3.addWidget(self.forecast_file_input, 4, 1, 1, 1)
        self.select_forecast_file = QtWidgets.QPushButton(
            self.forecast_file_box)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.select_forecast_file.setFont(font)
        self.select_forecast_file.setObjectName("select_forecast_file")
        self.gridLayout_3.addWidget(self.select_forecast_file, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.forecast_file_box, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(watershed_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 1)
        self.display_wateshed_name = QtWidgets.QLineEdit(watershed_dialog)
        self.display_wateshed_name.setEnabled(False)
        self.display_wateshed_name.setObjectName("display_wateshed_name")
        self.gridLayout.addWidget(self.display_wateshed_name, 4, 0, 1, 1)
        self.descriptio_box = QtWidgets.QGroupBox(watershed_dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.descriptio_box.sizePolicy().hasHeightForWidth())
        self.descriptio_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.descriptio_box.setFont(font)
        self.descriptio_box.setObjectName("descriptio_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.descriptio_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.drain_area = QtWidgets.QLabel(self.descriptio_box)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.drain_area.setFont(font)
        self.drain_area.setObjectName("drain_area")
        self.gridLayout_2.addWidget(self.drain_area, 2, 0, 1, 1)
        self.watershed_id = QtWidgets.QLabel(self.descriptio_box)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.watershed_id.setFont(font)
        self.watershed_id.setObjectName("watershed_id")
        self.gridLayout_2.addWidget(self.watershed_id, 0, 0, 1, 2)
        self.watershed_name = QtWidgets.QLabel(self.descriptio_box)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.watershed_name.setFont(font)
        self.watershed_name.setObjectName("watershed_name")
        self.gridLayout_2.addWidget(self.watershed_name, 1, 0, 1, 2)
        self.drain_input = QtWidgets.QLineEdit(self.descriptio_box)
        self.drain_input.setObjectName("drain_input")
        self.gridLayout_2.addWidget(self.drain_input, 2, 3, 1, 1)
        self.id_display = QtWidgets.QLineEdit(self.descriptio_box)
        self.id_display.setObjectName("id_display")
        self.gridLayout_2.addWidget(self.id_display, 1, 3, 1, 1)
        self.watershed_id_display = QtWidgets.QLabel(self.descriptio_box)
        self.watershed_id_display.setObjectName("watershed_id_display")
        self.gridLayout_2.addWidget(self.watershed_id_display, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.descriptio_box, 0, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.inflows_label.setBuddy(self.inflows_file_input)
        self.forecast_labe.setBuddy(self.forecast_file_input)
        self.drain_area.setBuddy(self.drain_input)
        self.watershed_name.setBuddy(self.id_display)

        self.retranslateUi(watershed_dialog)
        self.buttonBox.accepted.connect(watershed_dialog.accept)
        self.buttonBox.rejected.connect(watershed_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(watershed_dialog)
        watershed_dialog.setTabOrder(self.id_display, self.drain_input)
        watershed_dialog.setTabOrder(
            self.drain_input, self.select_forecast_file)
        watershed_dialog.setTabOrder(
            self.select_forecast_file, self.forecast_file_input)
        watershed_dialog.setTabOrder(
            self.forecast_file_input, self.select_inflow_file)
        watershed_dialog.setTabOrder(
            self.select_inflow_file, self.inflows_file_input)
        watershed_dialog.setTabOrder(
            self.inflows_file_input, self.display_wateshed_name)
        watershed_dialog.setTabOrder(
            self.display_wateshed_name, self.buttonBox)

    def retranslateUi(self, watershed_dialog):
        _translate = QtCore.QCoreApplication.translate
        watershed_dialog.setWindowTitle(
            _translate("watershed_dialog", "Watershed"))
        self.inflows_file_box.setTitle(_translate(
            "watershed_dialog", "Observed Inflows File"))
        self.inflows_label.setText(_translate(
            "watershed_dialog", "<html><head/><body><p>Observed Inflows (mm<span style=\" vertical-align:super;\">3</span>/time)</p></body></html>"))
        self.select_inflow_file.setText(
            _translate("watershed_dialog", "Select"))
        self.forecast_file_box.setTitle(
            _translate("watershed_dialog", "Forecast File"))
        self.forecast_labe.setText(_translate(
            "watershed_dialog", "<html><head/><body><p>Forecast (mm<span style=\" vertical-align:super;\">3</span>/time)</p></body></html>"))
        self.select_forecast_file.setText(
            _translate("watershed_dialog", "Select"))
        self.descriptio_box.setTitle(
            _translate("watershed_dialog", "Description"))
        self.drain_area.setText(_translate(
            "watershed_dialog", "<html><head/><body><p>Drainage Area (Km<span style=\" vertical-align:super;\">2</span>)</p></body></html>"))
        self.watershed_id.setText(_translate(
            "watershed_dialog", "Watershed ID"))
        self.watershed_name.setText(_translate(
            "watershed_dialog", "Watershed Name"))
        self.watershed_id_display.setText(_translate("watershed_dialog", "1"))
