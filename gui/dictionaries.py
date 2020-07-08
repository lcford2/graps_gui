from builtins import str
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# gen setup



def GS(self, info_dict):
    self.dialog.ui.time_step_input.setText(str(info_dict.get('ntime_steps', "")))
    self.dialog.ui.restrictions_input.setText(str(info_dict.get('nrestric', "")))
    sim_type = info_dict.get('sim_type', "")
    if sim_type == 'Climatology':
        self.dialog.ui.type_sim_combo.setCurrentIndex(0)
    elif sim_type == 'Forecast':
        self.dialog.ui.type_sim_combo.setCurrentIndex(1)
    elif sim_type == 'Zero Flow':
        self.dialog.ui.type_sim_combo.setCurrentIndex(2)
    self.dialog.ui.year_input.setText(str(info_dict.get('nyears', "")))
    self.dialog.ui.ensem_input.setText(str(info_dict.get('nensembles', "")))
    forecast_option = info_dict.get('forecast_option', "")
    if forecast_option == 'Retrospective':
        self.dialog.ui.retro_button.setChecked(True)
    elif forecast_option == 'Adaptive':
        self.dialog.ui.adaptive_button.setChecked(True)
        self.dialog.ui.year_sim_input.setText(info_dict.get('nyear_sim', ""))
        if info_dict.get("nyear_sim", ""):
            self.dialog.ui.sim_input_table.setColumnCount(int(info_dict['nyear_sim']))

    forecast_info = info_dict.get('forecast_info', "")
    if hasattr(forecast_info, '__iter__'):
        for column, value in enumerate(forecast_info):
            item = QTableWidgetItem(value)
            self.dialog.ui.sim_input_table.setItem(0, column, item)


def WS(self, info_dict):
    self.dialog.ui.id_display.setText(str(info_dict.get('watershed_Name', "")))
    self.dialog.ui.drain_input.setText(str(info_dict.get('drain_Area', "")))
    self.dialog.ui.forecast_file_input.setText(str(info_dict.get('forecast_file', "")))
    self.dialog.ui.inflows_file_input.setText(str(info_dict.get('inflows_file', "")))


def RES(self, info_dict):
    self.dialog.ui.name_edit.setText(str(info_dict.get('reservoir_Name', "")))
    self.dialog.ui.latitude_edit.setText(str(info_dict.get('res_latitude', "")))
    self.dialog.ui.longitude_edit.setText(str(info_dict.get('res_longitude', "")))
    self.dialog.ui.min_elev_edit.setText(str(info_dict.get('res_min_elev', "")))
    self.dialog.ui.max_elev_edit.setText(str(info_dict.get('res_max_elev', "")))
    self.dialog.ui.min_stor_edit.setText(str(info_dict.get('res_min_storage', "")))
    self.dialog.ui.max_stor_label_2.setText(str(info_dict.get('res_max_storage', "")))
    self.dialog.ui.current_stor_edit.setText(
        str(info_dict.get('res_current_storage', "")))

    if 'evap_option' not in info_dict:
        info_dict['evap_option'] = 'Table'

    evap_option = info_dict.get('evap_option', "")
    if evap_option == 'Table':
        self.dialog.ui.evap_table.show()
        self.dialog.ui.evap_box.show()
        self.dialog.ui.evap_file_box.hide()
        self.dialog.ui.select_evap_file.hide()
        self.dialog.ui.evap_file_edit.hide()
        self.dialog.ui.evap_depth_table_radio.setChecked(True)
        evap_info = info_dict.get('evap_info', "")
        if hasattr(evap_info, '__iter__'):
            for column, value in enumerate(evap_info):
                item = QTableWidgetItem(value)
                self.dialog.ui.evap_table.setItem(0, column, item)

    else:
        self.dialog.ui.evap_table.hide()
        self.dialog.ui.evap_box.hide()
        self.dialog.ui.evap_file_box.show()
        self.dialog.ui.select_evap_file.show()
        self.dialog.ui.evap_file_edit.show()
        self.dialog.ui.evap_file_edit.setText(str(info_dict.get('evap_option', "")))
        self.dialog.ui.evap_depth_file_radio.setChecked(True)
    
    self.dialog.ui.elev_alpha_edit.setText(str(info_dict.get('elev_alpha', "")))
    self.dialog.ui.elev_beta_edit.setText(str(info_dict.get('elev_beta', "")))
    self.dialog.ui.elev_gamma_edit.setText(str(info_dict.get('elev_gamma', "")))
    self.dialog.ui.vol_alpha_edit.setText(str(info_dict.get('vol_alpha', "")))
    self.dialog.ui.vol_beta_edit.setText(str(info_dict.get('vol_beta', "")))
    self.dialog.ui.vol_gamma_edit.setText(str(info_dict.get('vol_gamma', "")))

    self.dialog.ui.tar_stor_edit.setText(str(info_dict.get('target_storage', "")))
    self.dialog.ui.stor_prob_edit.setText(
        str(info_dict.get('storage_probability', "")))

    if 'rule_curve_option' not in info_dict:
        info_dict['rule_curve_option'] = 'Table'

    rule_curve_option = info_dict.get('rule_curve_option', "")
    if rule_curve_option == 'Table':
        self.dialog.ui.rule_curve_table.show()
        self.dialog.ui.rule_curve_box.show()
        self.dialog.ui.curve_file_select.hide()
        self.dialog.ui.curve_file_edit.hide()
        self.dialog.ui.rule_curve_table_radio.setChecked(True)
        storage_rule = info_dict.get('storage_rule', "")
        flood_rule = info_dict.get('flood_rule', "")
        if hasattr(storage_rule, '__iter__'):
            for column, value in enumerate(storage_rule):
                item = QTableWidgetItem(value)
                self.dialog.ui.rule_curve_table.setItem(0, column, item)
        
        if hasattr(flood_rule, '__iter__'):
            for column, value in enumerate(flood_rule):
                item = QTableWidgetItem(value)
                self.dialog.ui.rule_curve_table.setItem(1, column, item)
    else:
        self.dialog.ui.rule_curve_table.hide()
        self.dialog.ui.rule_curve_box.show()
        self.dialog.ui.curve_file_select.show()
        self.dialog.ui.curve_file_edit.show()
        self.dialog.ui.rule_curve_file_radio.setChecked(True)
        self.dialog.ui.curve_file_edit.setText(str(rule_curve_option))

    target_restrictions = info_dict.get('target_restrictions', "")
    for column, value in enumerate(target_restrictions):
        item = QTableWidgetItem(value)
        self.dialog.ui.target_rest_table.setItem(0, column, item)
    num_spillways = info_dict.get('num_spillways', "")
    self.dialog.ui.num_spill_edit.setText(str(num_spillways))
    self.dialog.ui.spillway_table.setRowCount(int(num_spillways))

    spillways = info_dict.get('spillways', "")
    if hasattr(spillways, '__iter__'):
        for i, spillway_info in enumerate(spillways):
            for key, value in spillway_info.items():
                item = QTableWidgetItem(value)
                if key == 'spillway_type':
                    self.dialog.ui.spillway_table.setItem(i, 0, item)
                elif key == 'crest_level':
                    self.dialog.ui.spillway_table.setItem(i, 1, item)
                elif key == 'max_discharge':
                    self.dialog.ui.spillway_table.setItem(i, 2, item)

    num_outlets = info_dict.get('num_outlets', "")
    self.dialog.ui.num_outlet_edit.setText(str(num_outlets))
    self.dialog.ui.outlet_table.setRowCount(int(num_outlets))

    outlets = info_dict.get('outlets', "")
    if hasattr(outlets, '__iter__'):
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
    self.dialog.ui.user_name_edit.setText(str(info_dict.get('user_Name', "")))
    self.dialog.ui.min_release_edit.setText(str(info_dict.get('min_release', "")))
    self.dialog.ui.max_release_edit.setText(str(info_dict.get('max_release', "")))
    self.dialog.ui.tariff_edit.setText(str(info_dict.get('tariff', "")))
    self.dialog.ui.penalty_edit.setText(str(info_dict.get('penalty', "")))
    self.dialog.ui.reliability_edit.setText(str(info_dict.get('reliability', "")))
    self.dialog.ui.contract_restict_edit.setText(
        str(info_dict.get('restrict_volume', "")))
    self.dialog.ui.penalty_comp_edit.setText(str(info_dict.get('penalty_comp', "")))
    user_type = info_dict.get('user_type', "")
    if user_type == 'Municipal':
        self.dialog.ui.user_type_combo.setCurrentIndex(0)
    elif user_type == 'Industry':
        self.dialog.ui.user_type_combo.setCurrentIndex(1)
    elif user_type == 'Agricultural':
        self.dialog.ui.user_type_combo.setCurrentIndex(2)
    elif user_type == 'Hydropower':
        self.dialog.ui.user_type_combo.setCurrentIndex(3)
    elif user_type == 'Environmental':
        self.dialog.ui.user_type_combo.setCurrentIndex(4)

    if 'demand_option' not in info_dict:
        info_dict['demand_option'] = 'Table'

    demand_option = info_dict.get('demand_option', "")
    if demand_option == 'Table':
        self.dialog.ui.demand_table.show()
        self.dialog.ui.demand_data_box.show()
        self.dialog.ui.demand_file_box.hide()
        self.dialog.ui.table_radio.setChecked(True)
        demand = info_dict.get('demand', "")
        if hasattr(demand, '__iter__'):
            for column, value in enumerate(demand):
                item = QTableWidgetItem(value)
                self.dialog.ui.demand_table.setItem(0, column, item)
    else:
        self.dialog.ui.demand_table.hide()
        self.dialog.ui.demand_data_box.hide()
        self.dialog.ui.demand_file_box.show()
        self.dialog.ui.file_radio.setChecked(True)
        self.dialog.ui.demand_file_edit.setText(str(demand_option))
    restric_comp = info_dict.get('restric_comp', "")
    if hasattr(restric_comp, '__iter__'):
        for column, value in enumerate(restric_comp):
            item = QTableWidgetItem(value)
            self.dialog.ui.restrict_comp_table.setItem(0, column, item)
    restric_frac = info_dict.get('restric_frac', "")
    if hasattr(restric_frac, '__iter__'):
        for column, value in enumerate(restric_frac):
            item = QTableWidgetItem(value)
            self.dialog.ui.restrict_frac_table.setItem(0, column, item)

    num_turbines = info_dict.get('num_turbines', "")
    self.dialog.ui.num_turbines_edit.setText(str(num_turbines))
    self.dialog.ui.hydro_table.setRowCount(int(num_turbines))

    turbines = info_dict.get('hydro', "")
    if hasattr(turbines, '__iter__'):
        for num, turbine_info in enumerate(turbines):
            self.dialog.ui.hydro_table.setItem(num, 0, QTableWidgetItem(turbine_info['max_discharge']))
            self.dialog.ui.hydro_table.setItem(num, 1, QTableWidgetItem(turbine_info['capacity']))
            self.dialog.ui.hydro_table.setItem(num, 2, QTableWidgetItem(turbine_info['efficiency']))
            self.dialog.ui.hydro_table.setItem(num, 3, QTableWidgetItem(turbine_info['energy_coeff_1']))
            self.dialog.ui.hydro_table.setItem(num, 4, QTableWidgetItem(turbine_info['energy_coeff_2']))
            self.dialog.ui.hydro_table.setItem(num, 5, QTableWidgetItem(turbine_info['energy_rate']))
            

    if 'elev_option' not in info_dict:
        info_dict['elev_option'] = 'Table'

    elev_option = info_dict.get('elev_option', "")
    if elev_option == 'Table':
        self.dialog.ui.hydro_elev_table.show()
        self.dialog.ui.elev_file_edit.hide()
        self.dialog.ui.elev_file_button.hide()
        self.dialog.ui.table_radio_2.setChecked(True)
        turb_elev = info_dict.get('turbine_elevs', "")
        if hasattr(turb_elev, '__iter__'):
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
    self.dialog.ui.sink_name_edit.setText(str(info_dict.get('sink_Name', "")))
    self.dialog.ui.max_store_edit.setText(str(info_dict.get('max_storage', "")))


def JUN(self, info_dict):
    self.dialog.ui.flow_jun_node_edit.setText(str(info_dict.get('junction_Name', "")))


def IB(self, info_dict):
    self.dialog.ui.interbasin_name_edit.setText(
        str(info_dict.get('interbasin_Name', "")))
    self.dialog.ui.drainage_area_edit.setText(str(info_dict.get('drain_area', "")))

    if 'flow_option' not in info_dict:
        info_dict['flow_option'] = 'Table'

    flow_option = info_dict.get('flow_option', "")
    if flow_option == 'Table':
        self.dialog.ui.ave_flow_box.show()
        self.dialog.ui.flow_file_edit.hide()
        self.dialog.ui.file_button.hide()
        self.dialog.ui.ave_flows_table.show()
        self.dialog.ui.table_radio.setChecked(True)
        average_flows = info_dict.get('average_flows', "")
        if hasattr(average_flows, '__iter__'):
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
    self.dialog.ui.link_name_display.setText(str(info_dict.get('link_ID', "")))
    self.dialog.ui.link_name_edit_2.setText(str(info_dict.get('link_Name', "")))
    self.dialog.ui.type_start_display.setText(str(info_dict.get('start_node', "")[0]))
    self.dialog.ui.start_node_display.setText(str(info_dict.get('start_node', "")[1:]))
    self.dialog.ui.type_end_display.setText(str(info_dict.get('stop_node', "")[0]))
    self.dialog.ui.end_node_display.setText(str(info_dict.get('stop_node', "")[1:]))
    self.dialog.ui.min_disch_edit.setText(str(info_dict.get('min_discharge', "")))
    self.dialog.ui.max_disch_edit.setText(str(info_dict.get('max_discharge', "")))
    self.dialog.ui.loss_fact_edit.setText(str(info_dict.get('loss_factor', "")))
    if info_dict.get('return_flow', "") == 'Yes':
        self.dialog.ui.yes_rad_button.setChecked(True)
    else:
        self.dialog.ui.no_rad_button.setChecked(True)
    self.dialog.ui.nlags_edit.setText(str(info_dict.get('nlags', "")))
    self.dialog.ui.return_flow_table.setColumnCount(int(info_dict.get('nlags', "")))
    return_flows = info_dict.get('ret_flows', "")
    if hasattr(return_flows, '__iter__'):
        for column, value in enumerate(return_flows):
            item = QTableWidgetItem(value)
            self.dialog.ui.return_flow_table.setItem(0, column, item)
