from builtins import str
from builtins import range
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import dictionaries as dlg_populate
from IPython import embed as II
import sys
import os
from collections import deque

num_of_items = {str(i): 0 for i in range(1, 14)}
item_types = {str(i): [] for i in range(1, 14)}
user_control_list = []

# GRAPS modeled blocks.
types = ['nwatershed', 'nnatural_flow', 'nres', 'nuser', 'nfnode',
         'ndir_inflows', 'nret_inflows', 'ndiversion', 'nspill_flow',
         'ninterbasin_flow', 'ndemand_release', 'nsink', 'ninterbasin']
# For simplicity on the users part, all links are represented as one type
# in the GUI and then their GRAPS type is determined when the output is written
type_map = {"W": 1, "R": 3, "U": 4, "J": 5, "S": 12, "I": 13}


def write_input(self, filename):
    gs_dict, info_dict = self.gen_setup_dict, self.dialog_dict
    items = list(self.ui.scene.items())
    # this portion goes through and counts the number of each type
    # of modeled object. The full types are listed above in `types`
    # The simplified types for the GUI are in `type_map`
    for item in items:
        if not getattr(item, "itemid", None):
            continue
        if item.item_type == "text":
            continue
        itype = item.block_type
        inum = item.block_index
        item_id = item.itemid
        if itype == 'W':
            num_of_items['1'] += 1
            item_types['1'].append(inum)
            item_types['1'].sort()
        elif itype == 'R':
            num_of_items['3'] += 1
            item_types['3'].append(inum)
            item_types['3'].sort()
        elif itype == 'U':
            item_types['4'].append(inum)
            item_types['4'].sort()
            num_of_items['4'] += 1
        elif itype == 'J':
            item_types['5'].append(inum)
            item_types['5'].sort()
            num_of_items['5'] += 1
        elif itype == 'L':
            start = item.start_node
            stop = item.stop_node
            # Links that start at watershed are natural flows
            if start[0] == 'W':
                if inum not in item_types['2']:
                    item_types['2'].append(inum)
                    item_types['2'].sort()
                    num_of_items['2'] += 1
            elif start[0] == 'J':
                # Links that start at junctions and end at sinks are diversions
                if stop[0] == 'S':
                    if inum not in item_types['8']:
                        item_types['8'].append(inum)
                        item_types['8'].sort()
                        num_of_items['8'] += 1
                elif stop[0] == "U":
                    if inum not in item_types['11']:
                        item_types['11'].append(inum)
                        item_types['11'].sort()
                        num_of_items['11'] += 1
            # Links that start at interbasin nodes are interbasin transfer links
            elif start[0] == 'I':
                if inum not in item_types['10']:
                    item_types['10'].append(inum)
                    item_types['10'].sort()
                    num_of_items['10'] += 1
            elif start[0] == 'R':
                if stop[0] == 'U':
                    if inum not in item_types['11']:
                        item_types['11'].append(inum)
                        item_types['11'].sort()
                        num_of_items['11'] += 1
                else:
                    if inum not in item_types['6']:
                        item_types['6'].append(inum)
                        item_types['6'].sort()
                        num_of_items['6'] += 1
            elif start[0] == 'U':
                if inum not in item_types['7']:
                    item_types['7'].append(inum)
                    item_types['7'].sort()
                    num_of_items['7'] += 1
        elif itype == 'S':
            item_types['12'].append(inum)
            item_types['12'].sort()
            num_of_items['12'] += 1
        elif itype == 'I':
            item_types['13'].append(inum)
            item_types['13'].sort()
            num_of_items['13'] += 1
    
    with open(filename, 'w') as f:
        f.write(f"{gs_dict['ntime_steps']}\t{gs_dict['nensembles']}\n")
        line2_nums = [str(num_of_items[str(i)]) for i in range(1, 14)]
        line2 = "  ".join(line2_nums) + "\n"
        f.write(line2)
        for key in sorted(list(item_types.keys()), key=int):
            system = item_types[key]
            string = "{}\t{}\n".format
            if key == '1':
                for block in system:
                    item_id = 'W' + block
                    name = info_dict[item_id]['watershed_Name']
                    f.write(string(key, name))
            elif key == '2':
                for block in system:
                    item_id = 'L' + block
                    name = info_dict[item_id]['link_Name']
                    f.write(string(key, name))
            elif key == '3':
                for block in system:
                    item_id = 'R' + block
                    name = info_dict[item_id]['reservoir_Name']
                    f.write(string(key, name))
            elif key == '4':
                for block in system:
                    item_id = 'U' + block
                    name = info_dict[item_id]['user_Name']
                    f.write(string(key, name))
            elif key == '5':
                for block in system:
                    item_id = 'J' + block
                    name = info_dict[item_id]['junction_Name']
                    f.write(string(key, name))
            elif key == '6':
                for block in system:
                    item_id = 'L' + block
                    name = info_dict[item_id]['link_Name']
                    f.write(string(key, name))
            elif key == '7':
                for block in system:
                    item_id = 'L' + block
                    name = info_dict[item_id]['link_Name']
                    f.write(string(key, name))
            elif key == '8':
                for block in system:
                    item_id = 'L' + block
                    name = info_dict[item_id]['link_Name']
                    f.write(string(key, name))
            elif key == '9':
                for block in system:
                    item_id = 'L' + block
                    name = info_dict[item_id]['link_Name']
                    f.write(string(key, name))
            elif key == '10':
                for block in system:
                    item_id = 'L' + block
                    name = info_dict[item_id]['link_Name']
                    f.write(string(key, name))
            elif key == '11':
                for block in system:
                    item_id = 'L' + block
                    name = info_dict[item_id]['link_Name']
                    f.write(string(key, name))
            elif key == '12':
                for block in system:
                    item_id = 'S' + block
                    name = info_dict[item_id]['sink_Name']
                    f.write(string(key, name))
            elif key == '13':
                for block in system:
                    item_id = 'I' + block
                    name = info_dict[item_id]['interbasin_Name']
                    f.write(string(key, name))


def write_ws_details(self, filename):
    gs_dict, info_dict = self.gen_setup_dict, self.dialog_dict
    with open(filename, 'w') as f:
        for item in item_types['1']:
            item_num = item
            item_name = str(
                info_dict[str('W' + item)]['watershed_Name'])
            drainage_area = str(
                info_dict[str('W' + item)]['drain_Area'])
            inflow_file = info_dict[str('W' + item)]['inflows_file']
            count = 1
            file = False
            while not file:
                character = inflow_file[-count]
                if character == '/':
                    inflow_file = inflow_file[(-count + 1):]
                    file = True
                else:
                    count += 1
            nchild = 0
            children = []
            gitem = self.block_objects[f'W{item_num}'][0]
            nchild = gitem.get_n_children()
            children = gitem.children
            f.write(item_num + '\n' + item_name + '\n' + item_num +
                    ' ' + str(nchild) + '  ' + drainage_area + '\n')
            for child in children:
                f.write(f'{type_map[child[0]]}  {child[1:]}\n')
            f.write(inflow_file)


def write_link_details(self, filename, link_type):
    gs_dict, info_dict = self.gen_setup_dict, self.dialog_dict
    link_types = {
        "nflow": "6",
        "dir_flow": "6",
        "ret_flow": "7",
        "diversion": "8",
        "spill": "9",
        "ibasin": "10",
        "demand": "11"
    }
    with open(filename, 'w') as f:
        for item in item_types[link_types[link_type]]:
            item_num = item
            item_id = 'L' + item_num
            gitem = self.block_objects[f'L{item_num}'][0]
            start = gitem.start_node
            stop = gitem.stop_node
            start_num = start[1:]
            item_name = str(info_dict[item_id]['link_Name'])
            start_node = str(info_dict[item_id]['start_node'])
            stop_node = str(info_dict[item_id]['stop_node'])
            min_disch = str(info_dict[item_id]['min_discharge'])
            max_disch = str(info_dict[item_id]['max_discharge'])
            f.write(item_num + '\n' + item_name + '\n')
            f.write(f'{type_map[start_node[0]]}  {start_node[1:]}\n')
            f.write(f'{type_map[stop_node[0]]}  {stop_node[1:]}\n')
            f.write(f'{min_disch}   {max_disch}\n')


def write_res_details(self, filename):
    gs_dict, info_dict = self.gen_setup_dict, self.dialog_dict
    with open(filename, 'w') as f:
        for item in item_types['3']:
            item_num = item
            item_id = 'R' + item_num
            item_name = str(info_dict[item_id]['reservoir_Name'])
            latitude = str(info_dict[item_id]['res_latitude'])
            longitude = str(info_dict[item_id]['res_longitude'])
            max_elev = str(info_dict[item_id]['res_max_elev'])
            min_elev = str(info_dict[item_id]['res_min_elev'])
            max_storage = str(info_dict[item_id]['res_max_storage'])
            min_storage = str(info_dict[item_id]['res_min_storage'])
            current_storage = str(info_dict[item_id]['res_current_storage'])
            elev_alpha = str(info_dict[item_id]['elev_alpha'])
            elev_beta = str(info_dict[item_id]['elev_beta'])
            elev_gamma = str(info_dict[item_id]['elev_gamma'])
            vol_alpha = str(info_dict[item_id]['vol_alpha'])
            vol_beta = str(info_dict[item_id]['vol_beta'])
            target_storage = str(info_dict[item_id]['target_storage'])
            storage_prob = str(info_dict[item_id]['storage_probability'])
            time_step = gs_dict['ntime_steps']
            nrestric = gs_dict['nrestric']
            nspillways = info_dict[item_id]['num_spillways']
            noutlets = info_dict[item_id]['num_outlets']
            gitem = self.block_objects[f'R{item_num}'][0]
            nchild = gitem.get_n_children()
            nparent = gitem.get_n_parents()
            children = gitem.children
            parents = gitem.parents
        
            f.write(f'{item_num}\n')
            f.write(f'{item_name}\n')
            f.write(f'{latitude}\t{longitude}\n')
            f.write(f'{max_elev}\t{min_elev}\n')
            f.write(f'{max_storage}\t{min_storage}\t{current_storage}\n')
            f.write(f'{elev_alpha}\t{elev_beta}\t{elev_gamma}\n')
            f.write(f'{vol_alpha}\t{vol_beta}\n')
            f.write(f'{nspillways}\t{noutlets}\n')
            f.write(f'{nrestric}\n')
            f.write(f'{nchild}\t{nparent}\n')
            spillways = info_dict[item_id]['spillways']
            for spillway in spillways:
                stype = spillway["spillway_type"]
                clevel = spillway["crest_level"]
                max_disch = spillway["max_discharge"]
                f.write(f'{stype}   {clevel}   {max_disch}\n')

            for child in children:
                f.write(f'{type_map[child[0]]}  {child[1:]}\n')

            for parent in parents:
                f.write(f'{type_map[parent[0]]}  {parent[1:]}\n')

            outlets = info_dict[item_id]['outlets']
            for outlet in outlets:
                elev, area = outlet['elevation'], outlet['xsc_area']
                max_coef, min_coef = outlet['max_loss_coeff'], outlet['min_loss_coeff']
                f.write(
                    f'{elev}  {area}  {max_coef}  {min_coef}  {target_storage}  {storage_prob}\n')
            rule_curve = info_dict[item_id]['storage_rule']
            for value in rule_curve:
                f.write(f'{value}  ')
            f.write('\n')
            evap_table = info_dict[item_id]['evap_info']
            for value in evap_table:
                f.write(f'{value}  ')
            f.write('\n')
            targ_restric = info_dict[item_id]['target_restrictions']
            for value in targ_restric:
                f.write(f'{value}  ')
            f.write('\n')


def write_user_details(self, filename):
    gs_dict, info_dict = self.gen_setup_dict, self.dialog_dict
    with open(filename, 'w') as f:
        for item in item_types['4']:
            item_num = item
            item_id = 'U' + item_num
            item_name = str(info_dict[item_id]['user_Name'])
            user_type_str = info_dict[item_id]['user_type']
            user_type = '1'
            if user_type_str == 'Industry':
                user_type = '2'
            elif user_type_str == 'Agricultural':
                user_type = '3'
            elif user_type_str == 'Hydropower':
                user_type = '4'
            elif user_type_str == 'Environmental':
                user_type = '5'
            nrestric = gs_dict['nrestric']
            gitem = self.block_objects[f'U{item_num}'][0]
            nchild = gitem.get_n_children()
            nparent = gitem.get_n_parents()
            children = gitem.children
            parents = gitem.parents
            
            reliability = str(info_dict[item_id]['reliability'])
            restric_vol = str(info_dict[item_id]['restrict_volume'])
            tariff = str(info_dict[item_id]['tariff'])
            penalty = str(info_dict[item_id]['penalty'])
            min_release = str(info_dict[item_id]['min_release'])
            max_release = str(info_dict[item_id]['max_release'])
            penalty_comp = str(info_dict[item_id]['penalty_comp'])
            f.write(f'{item_num}\n')
            f.write(f'{item_name}\n')
            f.write(f'{item_num}  {user_type}  {nchild}  {nparent}  {nrestric}\n')

            for child in children:
                f.write(f'{type_map[child[0]]}  {child[1:]}\n')

            for parent in parents:
                f.write(f'{type_map[parent[0]]}  {parent[1:]}\n')

            f.write(
                f'{reliability}  {restric_vol}  {tariff}  {penalty}  ' +
                f'{min_release}  {max_release}  {penalty_comp}\n'
            )

            demand = info_dict[item_id]['demand']
            for value in demand:
                f.write(f'{value}   ')
            f.write('\n')
            restric_frac = info_dict[item_id]['restric_frac']
            for value in restric_frac:
                f.write(f'{value}   ')
            f.write('\n')
            restric_comp = info_dict[item_id]['restric_comp']
            for value in restric_comp:
                f.write(f'{value}   ')
            f.write('\n')
            if user_type == '4':
                turbines = info_dict[item_id]['hydro']
                elevation_dict = info_dict[item_id]['turbine_elevs']
                if len(turbines) == 1:
                    turb_dict = turbines[0]
                    max_disch = turb_dict['max_discharge']
                    cap = turb_dict['capacity']
                    eff = turb_dict['efficiency']
                    coef1 = turb_dict['energy_coeff_1']
                    coef2 = turb_dict['energy_coeff_2']
                    erate = turb_dict['energy_rate']
                    f.write(
                        "  ".join([max_disch, cap, eff, coef1, coef2, erate]) + "\n")

                    # for value in elevation_dict:
                    #     f.write(f'{value}   ')
                    # f.write('\n')
                elif len(turbines) > 1:
                    pass
                    'Not sure if mutliple turbines are able to be considered'
            return_link = ''
            items = list(self.ui.scene.items())
            for link in items:
                if not getattr(link, "itemid", None):
                    continue
                if link.item_type == "line":
                    link_id = link.itemid
                    global user_control_list
                    start = link.start_node
                    item_id = 'U' + str(item_num)
                    if start == item_id:
                        if start not in user_control_list:
                            return_link = link_id
                            nlags = info_dict[link_id]['nlags']
                            f.write(nlags + '\n')
                            ret_flows = info_dict[link_id]['ret_flows']
                            if len(ret_flows) == 0:
                                f.write(str(0.01) + '\n')
                            else:
                                for value in sorted(ret_flows.values()):
                                    f.write(value + '  ')
                                f.write('\n')
                            user_control_list.append(start)



def write_jun_details(self, filename):
    gs_dict, info_dict = self.gen_setup_dict, self.dialog_dict
    with open(filename, 'w') as f:
        for item in item_types['5']:
            item_num = item
            item_id = 'J' + item_num
            item_name = str(info_dict[item_id]['junction_Name'])
            gitem = self.block_objects[f'J{item_num}'][0]
            nchild = gitem.get_n_children()
            nparent = gitem.get_n_parents()
            children = gitem.children
            parents = gitem.parents
            
            f.write(f'{item_num}\n')
            f.write(f'{item_name}\n')
            f.write(f'{item_num}  {nchild}  {nparent}\n')
            for child in children:
                f.write(f'{type_map[child[0]]}  {child[1:]}\n')

            for parent in parents:
                f.write(f'{type_map[parent[0]]}  {parent[1:]}\n')


def write_sink_details(self, filename):
    gs_dict, info_dict = self.gen_setup_dict, self.dialog_dict
    with open(filename, 'w') as f:
        for item in item_types['12']:
            item_num = item
            item_id = 'S' + item_num
            item_name = str(info_dict[item_id]['sink_Name'])
            max_storage = str(info_dict[item_id]['max_storage'])

            gitem = self.block_objects[f'S{item_num}'][0]
            nparent = gitem.get_n_parents()
            parents = gitem.parents

        
            f.write(f'{item_num}\n')
            f.write(f'{item_name}\n')
            f.write(f'{item_num}  {nparent}\n')
            for parent in parents:
                f.write(f'{type_map[parent[0]]}  {parent[1:]}\n')
            f.write(f'{max_storage}\n')


def write_ibasin_details(self, filename):
    gs_dict, info_dict = self.gen_setup_dict, self.dialog_dict
    with open(filename, 'w') as f:
        for item in item_types['13']:
            item_num = item
            item_id = 'I' + item
            item_name = str(info_dict[item_id]['interbasin_Name'])
            drainage_area = str(info_dict[item_id]['drain_Area'])
            inflow_file = info_dict[item_id]['inflows_file']
            gitem = self.block_objects[f'I{item_num}'][0]
            nchild = gitem.get_n_children()
            children = gitem.children
           
            f.write(f'{item_num}\n')
            f.write(f'{item_name}\n')
            f.write(f'{drainage_area}\n')
            f.write(f'{item_num}  {nchild}\n')
            for child in children:
                f.write(f'{type_map[child[0]]}  {child[1:]}\n')
            average_flows = info_dict[item_id]['average_flows']
            for info in average_flows:
                f.write(f'{info}  ')
            f.write('\n')


def write_dec_var_details(self, filename):
    gs_dict, info_dict = self.gen_setup_dict, self.dialog_dict
    #! I STILL NEED TO UPDATE THIS FUNCTION
    with open(filename, 'w') as f:
        num = int(num_of_items['4'])
        time_steps = int(gs_dict['ntime_steps'])
        ndesc_variables = num * time_steps
        for i in range(ndesc_variables):
            f.write('9\n')
