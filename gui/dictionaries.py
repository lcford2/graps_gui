from builtins import str
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# gen setup


def GS(self, info_dict):
    self.dialog.ui.time_step_input.setText(str(info_dict['ntime_steps']))
    self.dialog.ui.restrictions_input.setText(str(info_dict['nrestric']))
    if info_dict['sim_type'] == 'Climatology':
        self.dialog.ui.type_sim_combo.setCurrentIndex(0)
    elif info_dict['sim_type'] == 'Forecast':
        self.dialog.ui.type_sim_combo.setCurrentIndex(1)
    elif info_dict['sim_type'] == 'Zero Flow':
        self.dialog.ui.type_sim_combo.setCurrentIndex(2)
    self.dialog.ui.year_input.setText(str(info_dict['nyears']))
    self.dialog.ui.ensem_input.setText(str(info_dict['nensembles']))
    if info_dict['forecast_option'] == 'Retrospective':
        self.dialog.ui.retro_button.setChecked(True)
    elif info_dict['forecast_option'] == 'Adaptive':
        self.dialog.ui.adaptive_button.setChecked(True)
    self.dialog.ui.year_sim_input.setText(info_dict['nyear_sim'])
    self.dialog.ui.sim_input_table.setColumnCount(int(info_dict['nyear_sim']))

    forecast_info = info_dict['forecast_info']
    for column, value in enumerate(forecast_info):
        item = QTableWidgetItem(value)
        self.dialog.ui.sim_input_table.setItem(0, column, item)


def WS(self, info_dict):
    self.dialog.ui.id_display.setText(str(info_dict['watershed_Name']))
    self.dialog.ui.drain_input.setText(str(info_dict['drain_Area']))
    self.dialog.ui.forecast_file_input.setText(str(info_dict['forecast_file']))
    self.dialog.ui.inflows_file_input.setText(str(info_dict['inflows_file']))


def RES(self, info_dict):
    self.dialog.ui.name_edit.setText(str(info_dict['reservoir_Name']))
    self.dialog.ui.latitude_edit.setText(str(info_dict['res_latitude']))
    self.dialog.ui.longitude_edit.setText(str(info_dict['res_longitude']))
    self.dialog.ui.min_elev_edit.setText(str(info_dict['res_min_elev']))
    self.dialog.ui.max_elev_edit.setText(str(info_dict['res_max_elev']))
    self.dialog.ui.min_stor_edit.setText(str(info_dict['res_min_storage']))
    self.dialog.ui.max_stor_label_2.setText(str(info_dict['res_max_storage']))
    self.dialog.ui.current_stor_edit.setText(
        str(info_dict['res_current_storage']))

    if 'evap_option' not in info_dict:
        info_dict['evap_option'] = 'Table'

    evap_option = info_dict['evap_option']
    if evap_option == 'Table':
        self.dialog.ui.evap_table.show()
        self.dialog.ui.evap_box.show()
        self.dialog.ui.evap_file_box.hide()
        self.dialog.ui.select_evap_file.hide()
        self.dialog.ui.evap_file_edit.hide()
        self.dialog.ui.table_radio_3.setChecked(True)
        evap_info = info_dict['evap_info']
        for column, value in enumerate(evap_info):
            item = QTableWidgetItem(value)
            self.dialog.ui.evap_table.setItem(0, column, item)

    else:
        self.dialog.ui.evap_table.hide()
        self.dialog.ui.evap_box.hide()
        self.dialog.ui.evap_file_box.show()
        self.dialog.ui.select_evap_file.show()
        self.dialog.ui.evap_file_edit.show()
        self.dialog.ui.evap_file_edit.setText(str(info_dict['evap_option']))
        self.dialog.ui.input_radio_2.setChecked(True)

    if info_dict['storage_option'] == 'Coefficient':
        self.dialog.ui.coeff_radio.setChecked(True)
    elif info_dict['storage_option'] == 'Table':
        self.dialog.ui.table_radio.setChecked(True)
    self.dialog.ui.elev_alpha_edit.setText(str(info_dict['elev_alpha']))
    self.dialog.ui.elev_beta_edit.setText(str(info_dict['elev_beta']))
    self.dialog.ui.elev__gamma_edit.setText(str(info_dict['elev_gamma']))
    self.dialog.ui.vol_alpha_edit.setText(str(info_dict['vol_alpha']))
    self.dialog.ui.vol_beta_edit.setText(str(info_dict['vol_beta']))
    self.dialog.ui.vol__gamma_edit.setText(str(info_dict['vol_gamma']))
    self.dialog.ui.select_file_field.setText(
        str(info_dict['lev_vol_area_file']))
    self.dialog.ui.tar_stor_edit.setText(str(info_dict['target_storage']))
    self.dialog.ui.stor_prob_edit.setText(
        str(info_dict['storage_probability']))

    if 'rule_curve_option' not in info_dict:
        info_dict['rule_curve_option'] = 'Table'

    rule_curve_option = info_dict['rule_curve_option']
    if rule_curve_option == 'Table':
        self.dialog.ui.rule_curve_table.show()
        self.dialog.ui.rule_curve_box.show()
        self.dialog.ui.curve_file_select.hide()
        self.dialog.ui.curve_file_edit.hide()
        self.dialog.ui.table_radio_2.setChecked(True)
        storage_rule = info_dict['storage_rule']
        for column, value in enumerate(storage_rule):
            item = QTableWidgetItem(value)
            self.dialog.ui.rule_curve_table.setItem(0, column, item)
    else:
        self.dialog.ui.rule_curve_table.hide()
        self.dialog.ui.rule_curve_box.show()
        self.dialog.ui.curve_file_select.show()
        self.dialog.ui.curve_file_edit.show()
        self.dialog.ui.input_radio.setChecked(True)
        self.dialog.ui.curve_file_edit.setText(str(rule_curve_option))

    """
	storage_constraint = info_dict['storage_constraint']
	for key in storage_constraint.keys():
		if storage_constraint[key] == 'No':
			column = int(key) - 1
			self.dialog.ui.rule_curve_table.item(1, column).setCheckState(Qt.Checked)
		else:
			column = int(key) - 1
			self.dialog.ui.rule_curve_table.item(1, column).setCheckState(Qt.Unchecked)

	flood_volume = info_dict['flood_volume']
	for key in flood_volume.keys():
		column = int(key)-1
		item = QTableWidgetItem(flood_volume[key])
		self.dialog.ui.rule_curve_table.setItem(2, column, item)
	flood_constraint = info_dict['flood_constraint']
	for key in flood_constraint.keys():
		if flood_constraint[key] == 'No':
			column = int(key) - 1
			self.dialog.ui.rule_curve_table.item(3, column).setCheckState(Qt.Checked)
		else:
			column = int(key) - 1
			self.dialog.ui.rule_curve_table.item(3, column).setCheckState(Qt.Unchecked)
	"""
    target_restrictions = info_dict['target_restrictions']
    for column, value in enumerate(target_restrictions):
        item = QTableWidgetItem(value)
        self.dialog.ui.target_rest_table.setItem(0, column, item)
    num_spillways = info_dict['num_spillways']
    self.dialog.ui.num_spill_edit.setText(str(num_spillways))
    self.dialog.ui.spillway_table.setRowCount(int(num_spillways))

    spillways = info_dict['spillways']

    for i, spillway_info in enumerate(spillways):
        for key, value in spillway_info.items():
            item = QTableWidgetItem(value)
            if key == 'spillway_type':
                self.dialog.ui.spillway_table.setItem(i, 0, item)
            elif key == 'crest_level':
                self.dialog.ui.spillway_table.setItem(i, 1, item)
            elif key == 'max_discharge':
                self.dialog.ui.spillway_table.setItem(i, 2, item)

    num_outlets = info_dict['num_outlets']
    self.dialog.ui.num_outlet_edit.setText(str(num_outlets))
    self.dialog.ui.outlet_table.setRowCount(int(num_outlets))

    outlets = info_dict['outlets']
    for i, outlet_info in enumerate(outlets):
        for key, value in outlet_info.items():
            item = QTableWidgetItem(value)
            if key == 'elevation':
                self.dialog.ui.outlet_table.setItem(i, 0, item)
            elif key == 'xsc_area':
                self.dialog.ui.outlet_table.setItem(i, 1, item)
            elif key == 'max_loss_coeff':
                self.dialog.ui.outlet_table.setItem(i, 2, item)
            elif key == 'min_loss_coeff':
                self.dialog.ui.outlet_table.setItem(i, 3, item)


def US(self, info_dict):
    self.dialog.ui.user_name_edit.setText(str(info_dict['user_Name']))
    self.dialog.ui.min_release_edit.setText(str(info_dict['min_release']))
    self.dialog.ui.max_release_edit.setText(str(info_dict['max_release']))
    self.dialog.ui.tariff_edit.setText(str(info_dict['tariff']))
    self.dialog.ui.penalty_edit.setText(str(info_dict['penalty']))
    self.dialog.ui.reliability_edit.setText(str(info_dict['reliability']))
    self.dialog.ui.contract_restict_edit.setText(
        str(info_dict['restrict_volume']))
    self.dialog.ui.penalty_comp_edit.setText(str(info_dict['penalty_comp']))
    # self.dialog.ui.name_edit.setText(info_dict['reservoir_Name'])
    if info_dict['user_type'] == 'Municipal':
        self.dialog.ui.user_type_combo.setCurrentIndex(0)
    elif info_dict['user_type'] == 'Industry':
        self.dialog.ui.user_type_combo.setCurrentIndex(1)
    elif info_dict['user_type'] == 'Agricultural':
        self.dialog.ui.user_type_combo.setCurrentIndex(2)
    elif info_dict['user_type'] == 'Hydropower':
        self.dialog.ui.user_type_combo.setCurrentIndex(3)
    elif info_dict['user_type'] == 'Environmental':
        self.dialog.ui.user_type_combo.setCurrentIndex(4)

    if 'demand_option' not in info_dict:
        info_dict['demand_option'] = 'Table'

    demand_option = info_dict['demand_option']
    if demand_option == 'Table':
        self.dialog.ui.demand_table.show()
        self.dialog.ui.demand_data_box.show()
        self.dialog.ui.demand_file_box.hide()
        self.dialog.ui.table_radio.setChecked(True)
        demand = info_dict['demand']
        for column, value in enumerate(demand):
            item = QTableWidgetItem(value)
            self.dialog.ui.demand_table.setItem(0, column, item)
    else:
        self.dialog.ui.demand_table.hide()
        self.dialog.ui.demand_data_box.hide()
        self.dialog.ui.demand_file_box.show()
        self.dialog.ui.file_radio.setChecked(True)
        self.dialog.ui.demand_file_edit.setText(str(demand_option))
    restric_comp = info_dict['restric_comp']
    for column, value in enumerate(restric_comp):
        item = QTableWidgetItem(value)
        self.dialog.ui.restrict_comp_table.setItem(0, column, item)
    restric_frac = info_dict['restric_frac']
    for column, value in enumerate(restric_frac):
        item = QTableWidgetItem(value)
        self.dialog.ui.restrict_frac_table.setItem(0, column, item)

    num_turbines = info_dict['num_turbines']
    self.dialog.ui.num_turbines_edit.setText(str(num_turbines))
    self.dialog.ui.hydro_table.setRowCount(int(num_turbines))

    turbines = info_dict['hydro']
    for num, turbine_info in enumerate(turbines):
        for key, value in turbine_info.items():
            item = QTableWidgetItem(value)
            if key == 'max_discharge':
                self.dialog.ui.hydro_table.setItem(num, 0, item)
            elif key == 'capacity':
                self.dialog.ui.hydro_table.setItem(num, 1, item)
            elif key == 'efficiency':
                self.dialog.ui.hydro_table.setItem(num, 2, item)
            elif key == 'energy_coeff_1':
                self.dialog.ui.hydro_table.setItem(num, 3, item)
            elif key == 'energy_coeff_2':
                self.dialog.ui.hydro_table.setItem(num, 4, item)
            elif key == 'energy_rate':
                self.dialog.ui.hydro_table.setItem(num, 5, item)
        num += 1

    if 'elev_option' not in info_dict:
        info_dict['elev_option'] = 'Table'

    elev_option = info_dict['elev_option']
    if elev_option == 'Table':
        self.dialog.ui.hydro_elev_table.show()
        self.dialog.ui.elev_file_edit.hide()
        self.dialog.ui.elev_file_button.hide()
        self.dialog.ui.table_radio_2.setChecked(True)
        turb_elev = info_dict['turbine_elevs']
        for column, value in enumerate(turb_elev):
            item = QTableWidgetItem(value)
            self.dialog.ui.hydro_elev_table.setItem(0, column, item)
    else:
        self.dialog.ui.hydro_elev_table.hide()
        self.dialog.ui.elev_file_edit.show()
        self.dialog.ui.elev_file_button.show()
        self.dialog.ui.file_radio_2.setChecked(True)
        self.dialog.ui.elev_file_edit.setText(str(elev_option))


def SINK(self, info_dict):
    self.dialog.ui.sink_name_edit.setText(str(info_dict['sink_Name']))
    self.dialog.ui.max_store_edit.setText(str(info_dict['max_storage']))


def JUN(self, info_dict):
    self.dialog.ui.flow_jun_node_edit.setText(str(info_dict['junction_Name']))


def IB(self, info_dict):
    self.dialog.ui.interbasin_name_edit.setText(
        str(info_dict['interbasin_Name']))
    self.dialog.ui.drainage_area_edit.setText(str(info_dict['drain_area']))

    if 'flow_option' not in info_dict:
        info_dict['flow_option'] = 'Table'

    flow_option = info_dict['flow_option']
    if flow_option == 'Table':
        self.dialog.ui.ave_flow_box.show()
        self.dialog.ui.flow_file_edit.hide()
        self.dialog.ui.file_button.hide()
        self.dialog.ui.ave_flows_table.show()
        self.dialog.ui.table_radio.setChecked(True)
        average_flows = info_dict['average_flows']
        for column, value in enumerate(average_flows):
            item = QTableWidgetItem(value)
            self.dialog.ui.ave_flows_table.setItem(0, column, item)
    else:
        self.dialog.ui.ave_flow_box.show()
        self.dialog.ui.flow_file_edit.show()
        self.dialog.ui.file_button.show()
        self.dialog.ui.ave_flows_table.hide()
        self.dialog.ui.file_radio.setChecked(True)
        self.dialog.ui.flow_file_edit.setText(str(flow_option))


def LINK(self, info_dict):
    self.dialog.ui.link_name_display.setText(str(info_dict['link_ID']))
    self.dialog.ui.link_name_edit_2.setText(str(info_dict['link_Name']))
    self.dialog.ui.type_start_display.setText(str(info_dict['start_node'][0]))
    self.dialog.ui.start_node_display.setText(str(info_dict['start_node'][1:]))
    self.dialog.ui.type_end_display.setText(str(info_dict['stop_node'][0]))
    self.dialog.ui.end_node_display.setText(str(info_dict['stop_node'][1:]))
    self.dialog.ui.min_disch_edit.setText(str(info_dict['min_discharge']))
    self.dialog.ui.max_disch_edit.setText(str(info_dict['max_discharge']))
    self.dialog.ui.loss_fact_edit.setText(str(info_dict['loss_factor']))
    if info_dict['return_flow'] == 'Yes':
        self.dialog.ui.yes_rad_button.setChecked(True)
    else:
        self.dialog.ui.no_rad_button.setChecked(True)
    self.dialog.ui.nlags_edit.setText(str(info_dict['nlags']))
    self.dialog.ui.return_flow_table.setColumnCount(int(info_dict['nlags']))
    return_flows = info_dict['ret_flows']
    for column, value in enumerate(return_flows):
        item = QTableWidgetItem(value)
        self.dialog.ui.return_flow_table.setItem(0, column, item)
