from __future__ import print_function
from __future__ import division
from builtins import str
from builtins import range
from past.utils import old_div
from PyQt5 import (QtCore as core,
                   QtGui as gui,
                   QtWidgets as widgets,
                   QtPrintSupport as printsupp,
                   QtWebEngineWidgets as webwidgets)
from matplotlib.backends.backend_qt5agg import (
            FigureCanvasQTAgg as FigureCanvas,
            NavigationToolbar2QT as NavToolbar)
from matplotlib.figure import Figure
import matplotlib  
import sys
import os
import platform
# imports main window user interface
from ui.graps_graphics import Ui_GRAPSInterface
# importing various dialogs
from ui.gen_setup_dialog import Ui_genSet_dialog
from ui.watershed_dialog import Ui_watershed_dialog
from ui.user_dialog import Ui_user_dialog
from ui.sink_dialog import Ui_sink_dialog
from ui.reservoir_dialog import Ui_reservoirDialog
from ui.link_dialog import Ui_link_dialog
from ui.junction_dialog import Ui_junction_dialog
from ui.interbasin_dialog import Ui_interbasin_dialog
from ui.error_dialog import Ui_ErrorDialog
from ui.draw_link_dialog import Ui_linkDraw_dialog as ld
from ui.not_saved_dialog import Ui_NotSavedDialog
from ui.plot_display_dialog import Ui_plot_display_dialog
from ui.multi_edit_dialog import Ui_multi_edit_dialog
from ui.help_dialog import Ui_help_dialog
# import my graphics with overloaded signals
from graphics_items import myPixmapItem, myGraphicsTextItem, myGraphicsLineItem
# repopulates dialogs on file open
import dictionaries as dlg_populate
# saves the graphics created by the user
from graps_io.save_view import save_view as sv
# open file dialog
from graps_io.open_file import open_file
# writes the output files needed to run the model
from graps_io.write_multireservoir import (write_input, write_ws_details,
                                           write_res_details, write_user_details,
                                           write_jun_details, write_ibasin_details,
                                           write_sink_details, write_link_details,
                                           write_dec_var_details, get_item_dict,
                                           make_file_system, write_runflag,
                                           write_model_params, write_hydro_coeff)
from IPython import embed as II


class MyMainScreen(widgets.QMainWindow):
    def __init__(self, thread_pool, parent=None, screen_res=None):
        # initialize the main window
        super().__init__(parent)

        # load and setup the interface via ui file
        self.ui = Ui_GRAPSInterface()
        self.ui.setupUi(self)
        self.setWindowIcon(gui.QIcon("./gui/icons/app_icon.png"))
        
        # provide access to the thread pool
        self.pool = thread_pool

        # setup containers
        self.gen_setup_dict = {}
        self.dialog_dict = {}
        # will contain tuples of image objects and their labels with keys of the block ID
        # e.g. self.block_objects["R1"] = (image object, label object)
        # should be useful when removing objects by ID or creating links
        self.block_objects = {}
        self.link_objects = {}
        self.block_indices = {
            "W": 1,
            "R": 1,
            "S": 1,
            "J": 1,
            "I": 1,
            "L": 1,
            "U": 1
        }
        # setup drawing parameters
        self.block_ID = ''
        self.block = 0
        self.dlg = 'dlg_closed'
        self.bitmap_width = 35
        self.bitmap_height = 32

        # self.filename=core.QString()
        self.filename = str
        self.ui.pasteOffset = 5
        self.ui.prevPoint = core.QPoint()
        self.ui.addOffset = 5
        # Setup the view. Using a graphics scene and view
        # as the canvas which the user will create system on
        self.ui.view = self.ui.graphicsView
        self.ui.scene = widgets.QGraphicsScene(self)
        self.ui.scene.setSceneRect(0, 0, 10000, 10000)
        # self.ui.view.setCursor(gui.QCursor("CrossCursor"))

        # save indicator
        self.dirty = False
        self.save_file_name = ""

        self.ui.view.setScene(self.ui.scene)

        # add help menu
        self.ui.actionHelp = widgets.QAction(self)
        self.ui.actionHelp.setObjectName("actionHelp")
        self.ui.actionHelp.setText("Help File")
        self.ui.actionHelp.setToolTip("Open Help File for the Interface")
        self.ui.menuHelp.addAction(self.ui.actionHelp)
        self.ui.actionHelp.triggered.connect(self.open_help_dialog)

        # connecting toolbar actions to functions that open dialogs
        # or perform actions like exporting data files
        self.ui.menuGen_Setup.triggered.connect(self.open_dataDialog)
        self.ui.actionGS.triggered.connect(self.open_dataDialog)
        self.ui.actionSave.triggered.connect(self.save_screen)
        self.ui.actionSave_As.triggered.connect(self.save_screen_as)
        self.ui.actionSave_2.triggered.connect(self.save_screen)
        self.ui.actionOpen.triggered.connect(self.file_open)
        self.ui.actionOpen_2.triggered.connect(self.file_open)
        self.ui.actionNew_File.triggered.connect(self.new_scene)
        self.ui.actionNew.triggered.connect(self.new_scene)
        self.ui.actionE.triggered.connect(self.export)
        self.ui.actionPrint.triggered.connect(self.print_scene)
        self.ui.actionMenuPrint.triggered.connect(self.print_scene)
        self.ui.actionCenter_View.triggered.connect(self.center_scene)
        self.ui.actionPrintPreview.triggered.connect(self.print_preview)
        self.ui.actionRun_Model.triggered.connect(self.start_model_thread)
        self.ui.actionMulti_Edit.triggered.connect(self.open_multi_edit_dialog)

        # connecting user block selections to the block handling functions
        self.ui.actionWatershed.triggered.connect(self.toolbar_interaction)
        self.ui.actionReservoir.triggered.connect(self.toolbar_interaction)
        self.ui.actionInterBT.triggered.connect(self.toolbar_interaction)
        self.ui.actionJunction.triggered.connect(self.toolbar_interaction)
        self.ui.actionUser.triggered.connect(self.toolbar_interaction)
        self.ui.actionSink.triggered.connect(self.toolbar_interaction)
        self.ui.actionN.triggered.connect(self.toolbar_interaction)
        self.ui.actionLink.triggered.connect(self.draw_line)

        self.ui.toolBar.setToolButtonStyle(core.Qt.ToolButtonIconOnly)

        # attribute selectors for multi-edit
        self.attribute_dict = {
            "R":{
                "Name":"reservoir_Name","Latitude":"res_latitude","Longitude":"res_longitude",
                "Min. Elevation":"res_min_elev","Max. Elevation":"res_max_elev","Min. Storage":"res_min_storage",
                "Max. Storage":"res_max_storage","Current Storage":"res_current_storage",
                "Target Storage":"target_storage","Storage Reliability":"storage_probability"
            },
            "U":{
                "Name":"user_Name","Min. Release":"min_release","Max. Release":"max_release",
                "Tariff":"tariff", "Penalty":"penalty","Reliability":"reliability",
                "Restriction Volume":"restrict_volume","Penalty Compensation":"penalty_comp",
                "User Type":"user_type"
            },
            "W":{
                "Name":"watershed_Name","Drainage Area":"drain_Area", "Inflows File":"inflows_file"
            },
            "J":{
                "Name":"junction_Name"
            },
            "I":{
                "Name":"interbasin_Name", "Drainage Area":"drain_area"
            }
        }

    def toolbar_interaction(self):
        tools = {
            self.ui.actionWatershed: "W",
            self.ui.actionReservoir: "R",
            self.ui.actionInterBT: "I",
            self.ui.actionJunction: "J",
            self.ui.actionUser: "U",
            self.ui.actionSink: "S",
            self.ui.actionN: "N"
        }
        block_map = {
            "W": "W.png",
            "R": "R.png",
            "I": "I.png",
            "J": "J.png",
            "U": "U.png",
            "S": "S.png",
            "N": 0
        }
        sender = self.sender()
        if sender.isChecked():
            self.block_ID = tools[sender]
            self.block = block_map[self.block_ID]
            for tool in tools.keys():
                if tool != sender:
                    tool.setChecked(False)
        else:
            self.block = 0
            self.ui.actionN.setChecked(True)

    def draw_line(self):
        self.dlg = 'dlg_open'
        # block = 1
        self.block_ID = 'L'
        # self.link_select()
        # creating a dialog for drawing links
        self.dialog = widgets.QDialog(self)  # initialize dialog
        self.dialog.ui = ld()  # load dialog properties from ui file
        self.dialog.ui.setupUi(self.dialog)  # setup dialog
        # Next line ensures the dialog is deleted from memory when it is closed
        # this makes sure it does not hang up the application
        self.dialog.setAttribute(core.Qt.WA_DeleteOnClose)
        # connecting user actions to responses
        self.dialog.ui.buttonBox.accepted.connect(self.linkdraw)
        # Apply allows the user to place multple links without closing the dialog
        btn = self.dialog.ui.buttonBox.button(widgets.QDialogButtonBox.Apply)
        btn.clicked.connect(self.linkdraw)
        self.dialog.ui.buttonBox.accepted.connect(self.dlg_close)
        self.dialog.ui.buttonBox.rejected.connect(self.dlg_close)
        # get all items in scene
        # if a item is selected when the dialog opens
        # this automatically populates that item in the
        # link start text box in the dialog and sets the focus
        # to the link stop text box
        self.dialog.ui.start_edit.setFocus(True)
        sel_items = list(self.ui.scene.selectedItems())
        for item in sel_items:
            item_ID = self.get_item_id(item)
            self.dialog.ui.start_edit.setText(item_ID)
            self.dialog.ui.stop_edit.setFocus()
        self.dialog.show()


    # Creates pixmap items to be placed on the screen
    # called when a user has a block selected and clicks on the screen
    # Places block near cursor and labels it based on other blocks of that type
    def createPixmapItem(self, pixmap, position, **kwargs):
        if kwargs:  # if there are kwargs passed use those instead
            for key, value in kwargs.items():
                if key == "value":
                    label_value = value
                if key == 'block_ID':
                    self.block_ID = value
            if int(label_value) >= self.block_indices[self.block_ID]:
                self.block_indices[self.block_ID] = int(label_value) + 1
        else:
            label_value = self.block_indices[self.block_ID]
            self.block_indices[self.block_ID] += 1
        block_id = f'{self.block_ID}{label_value}'
        pix_item = gui.QPixmap(os.path.join("gui", "icons", pixmap))
        item = myPixmapItem(parent=pix_item, itemid=block_id, owner=self)
        item.setFlags(widgets.QGraphicsItem.ItemIsSelectable)

        position.setX(position.x() - self.bitmap_width / 2)
        position.setY(position.y() - self.bitmap_height / 2)

        item.setPos(position)
        # item.setMatrix(matrix)
        item.setZValue(1)
        # making sure there is not another Item selected
        self.ui.scene.clearSelection()
        self.ui.scene.addItem(item)
        # Unselecting the item
        item.setSelected(False)

        # creating and placing a label for the block
        g_label = self.create_label(label_value, self.block_ID, position, item)
        # add item and label to block container
        self.block_objects[f"{self.block_ID}{label_value}"] = (item, g_label)
        item.label_item = g_label

        if not kwargs:
            self.dirty = True

    # creates labels for nodes
    def create_label(self, value, b_ID, position, qtItem):
        item = ''
        block_num = str(value)
        item_id = str(b_ID) + block_num
        x = item_id in self.dialog_dict
        if x:
            item_dict = self.dialog_dict[item_id]
            name_tag = ''
            for key in list(item_dict.keys()):
                if key[-4:] == 'Name':
                    name_tag = key
            item = myGraphicsTextItem(item_dict[name_tag], item_id, self)
        else:
            item = myGraphicsTextItem(block_num, item_id, self)
        position.setY(position.y() - 20)
        position.setX(position.x() - 18)
        item.setPos(position)
        item.setZValue(2)
        font = gui.QFont(self.font())
        font.setBold(True)
        item.setFont(font)
        self.ui.scene.addItem(item)
        return item

    # allows user to clear scene and start over

    def new_scene(self):
        items = list(self.ui.scene.items())
        for item in items:
            if str(type(item)) != "<class 'PyQt5.QtWidgets.QGraphicsRectItem'>":
                self.ui.scene.removeItem(item)
        self.gen_setup_dict.clear()
        self.dialog_dict.clear()
        self.block_objects = {}
        self.link_objects = {}
        self.block_indices = {
            "W": 1,
            "R": 1,
            "S": 1,
            "J": 1,
            "I": 1,
            "L": 1,
            "U": 1
        }
        self.dirty = False

    # changes the label of items in the scene if the name is updated via dialog
    def change_label(self, *args, **kwargs):
        if kwargs:
            name_tag = kwargs['name_tag']
            item_id = kwargs['item_id']
            if name_tag != '' and item_id.item_type == 'text':
                item_id.setPlainText(name_tag)
                item_id.text = name_tag
        else:
            items = list(self.ui.scene.items())
            for item in items:
                if item.type() == 8:
                    relation = item.itemid
                    if relation in self.dialog_dict:
                        item_dict = self.dialog_dict[relation]
                        name_tag = ''
                        for key in list(item_dict.keys()):
                            if key[-4:] == 'Name':
                                name_tag = key
                        item_name = item_dict[name_tag]
                        item.setPlainText(item_name)
    @staticmethod
    def get_save_dir(directory="."):
        save_folder = widgets.QFileDialog.getExistingDirectory(directory=directory)
        return save_folder

    # This will eventually be the run model that is used
    def run_model_devel(self):
        save_folder = self.get_save_dir()
        # self.export(save_folder)
        nuser = 0
        for block in self.block_objects.keys():
            if block[0] == "U":
                nuser += 1
        ntime = self.gen_setup_dict.get('ntime_steps', None)
        if not ntime:
            nparam = 84
        else:
            nparam = int(ntime)*int(nuser)
        output_path = os.path.join(save_folder, "output")
        model = ReservoirModel(nparam, save_folder, output_path)
        model.InitializeModel()
        model.Simulate()

    def start_model_thread(self):
        model_worker = Worker(self.run_model)
        self.pool.start(model_worker)

    def run_model(self):
        import platform
        import shutil
        import glob
        import subprocess
        run_folder = str(widgets.QFileDialog.getExistingDirectory(
            directory="graps_export"))
        if run_folder == '':
            pass
        else:
            curdir = os.getcwd()
            op_sys = platform.system()
            if op_sys == "Windows":
                for file in glob.glob("../GRAPS/windows/*"):
                    if not os.path.exists(os.path.join(run_folder, os.path.split(file)[-1])):
                        shutil.copy(file, run_folder)
                os.chdir(run_folder)
                subprocess.call(["multireservoir.exe"])
                os.chdir(curdir)
            elif op_sys == "Linux":
                for file in glob.glob("../GRAPS/linux/*"):
                    if not os.path.exists(os.path.join(run_folder, os.path.split(file)[-1])):
                        shutil.copy(file, run_folder)
                os.chdir(run_folder)
                subprocess.call(["multireservoir"])
                os.chdir(curdir)
    
    def graph_network(self):
        import networkx as nx
        graph = nx.DiGraph()
        pos = {}
        color_map = {"W":"red", "R":"blue",
                     "U":"green", "J":"yellow",
                     "S":"purple", "I":"cyan"}
        for nodes, item in self.link_objects.items():
            start, stop = nodes
            graph.add_node(start, color=color_map[start[0]])
            graph.add_node(stop, color=color_map[stop[0]])
            graph.add_edge(*nodes)
            pos[nodes[0]] = self.block_objects[nodes[0]][0].pos()
            pos[nodes[1]] = self.block_objects[nodes[1]][0].pos()
        lab_pos = {key:(value.x()/100, -value.y()/100) for key, value in pos.items()}
        pos = {key:(value.x()/100, -value.y()/100) for key, value in pos.items()}
        
        colors = [graph.nodes.data()[i]["color"] for i in graph.nodes()]
        figure = Figure()
        ax = figure.add_subplot(111)
        nx.draw_networkx_nodes(graph, ax=ax, pos=pos, node_color=colors, node_size=700, node_shape="v")
        nx.draw_networkx_edges(graph, ax=ax, pos=pos, connectionstyle="arc3,rad=0.3")
        nx.draw_networkx_labels(graph, ax=ax, pos=lab_pos)
        self.plot_dialog(figure)        

    def check_gen_setup(self):
        # check if crucial information from the general setup menu has been added
        time_steps = self.gen_setup_dict.get("ntime_steps", None)
        num_restric = self.gen_setup_dict.get("nrestric", None)
        return (time_steps and num_restric)

    def export(self):
        if not self.check_gen_setup():
            errormsg = "Error: You have not entered the required information.\nPlease finish the network before exporting."
            self.open_error_dialog(errormsg)
            return 
        if not os.path.isdir("graps_export"):
            os.mkdir("graps_export")
        save_folder = str(widgets.QFileDialog.getExistingDirectory(
            directory="graps_export"))
        if save_folder == '':
            pass
        else:
            export_worker = Worker(self.write_export, save_folder)
            self.pool.start(export_worker)

    # exports files needed to run the fortran code
    def write_export(self, save_folder):
        self.user_control_list = []
        self.num_of_items = {str(i): 0 for i in range(1, 14)}
        self.item_types = {str(i): [] for i in range(1, 14)}
        get_item_dict(self)
        make_file_system(self, save_folder)
        write_input(self, save_folder, 'input.dat')
        write_ws_details(self, save_folder, 'watershed_details.dat')
        write_res_details(self, save_folder, 'reservoir_details.dat')
        write_user_details(self, save_folder, 'user_details.dat')
        write_jun_details(self, save_folder, 'node_details.dat')
        write_link_details(self, save_folder, 'nflow_details.dat', "nflow")
        write_link_details(self, save_folder, 'dir_flow_details.dat', "dir_flow")
        write_link_details(self, save_folder, 'ret_flow_details.dat', "ret_flow")
        write_link_details(self, save_folder, 'diversions_details.dat', "diversion")
        write_link_details(self, save_folder, 'spill_flow_details.dat', "spill")
        write_link_details(self, save_folder, 'ibasin_flow_details.dat', "ibasin")
        write_link_details(self, save_folder, 'demand_flow_details.dat', "demand")
        write_sink_details(self, save_folder, 'sink_details.dat')
        write_ibasin_details(self, save_folder, 'interbasin_details.dat')
        write_dec_var_details(self, save_folder, 'decisionvar_details.dat')
        write_runflag(self, save_folder, "runflag.dat")
        write_model_params(self, save_folder, "model_para.dat")
        write_hydro_coeff(self, save_folder, "hydropower_conversion.dat")
    
    # controls placement of items
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == 1:
            if self.block != 0:
                point = self.ui.view.mapFromGlobal(gui.QCursor.pos())
                pos = self.ui.view.mapToScene(point)
                self.createPixmapItem(self.block, pos)

    # if a radio button is toggled in a dialog this controls the action connected to it
    def button_toggled(self):
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == 'yes_rad_button':
            if self.dialog.ui.yes_rad_button.isChecked():
                self.dialog.ui.return_flow_box.show()
            else:
                self.dialog.ui.return_flow_box.hide()

    def interbasin_button(self):
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == 'table_radio':
            self.dialog.ui.ave_flow_box.show()
            self.dialog.ui.flow_file_edit.hide()
            self.dialog.ui.file_button.hide()
            self.dialog.ui.ave_flows_table.show()
        elif sender_name == 'file_radio':
            self.dialog.ui.ave_flow_box.show()
            self.dialog.ui.flow_file_edit.show()
            self.dialog.ui.file_button.show()
            self.dialog.ui.ave_flows_table.hide()

    def reservoir_button(self):
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == 'evap_depth_table_radio':
            self.dialog.ui.evap_table.show()
            self.dialog.ui.evap_box.show()
            self.dialog.ui.evap_file_box.hide()
            self.dialog.ui.select_evap_file.hide()
            self.dialog.ui.evap_file_edit.hide()
        elif sender_name == 'evap_depth_file_radio':
            self.dialog.ui.evap_table.hide()
            self.dialog.ui.evap_box.hide()
            self.dialog.ui.evap_file_box.show()
            self.dialog.ui.select_evap_file.show()
            self.dialog.ui.evap_file_edit.show()
        elif sender_name == 'rule_curve_table_radio':
            self.dialog.ui.rule_curve_table.show()
            self.dialog.ui.rule_curve_box.show()
            self.dialog.ui.curve_file_select.hide()
            self.dialog.ui.curve_file_edit.hide()
        elif sender_name == 'rule_curve_file_radio':
            self.dialog.ui.rule_curve_table.hide()
            self.dialog.ui.rule_curve_box.show()
            self.dialog.ui.curve_file_select.show()
            self.dialog.ui.curve_file_edit.show()

    def user_button(self):
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == 'table_radio':
            self.dialog.ui.demand_table.show()
            self.dialog.ui.demand_data_box.show()
            self.dialog.ui.demand_file_box.hide()
        elif sender_name == 'file_radio':
            self.dialog.ui.demand_table.hide()
            self.dialog.ui.demand_data_box.hide()
            self.dialog.ui.demand_file_box.show()
        elif sender_name == 'table_radio_2':
            self.dialog.ui.hydro_elev_table.show()
            self.dialog.ui.elev_file_edit.hide()
            self.dialog.ui.elev_file_button.hide()
        elif sender_name == 'file_radio_2':
            self.dialog.ui.hydro_elev_table.hide()
            self.dialog.ui.elev_file_edit.show()
            self.dialog.ui.elev_file_button.show()

    # controls dialog opening and closing to prevent errors
    def dlg_close(self):
        self.dlg = "dlg_closed"

    def get_item_id(self, item):
        return item.itemid

    def center_bold_stack(self, text_items):
        front = "<html><head/><body>"
        back = "</body></html>"
        prepend = "<p align=\"center\"><span style=\" font-weight:600;\">"
        postpend = "</span></p>"
        fixed_items = [f"{prepend}{item}{postpend}" for item in text_items]
        body = "".join(fixed_items)
        return f"{front}{body}{back}"

    def open_error_dialog(self, text=None):
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_ErrorDialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.setAttribute(
            core.Qt.WA_DeleteOnClose)
        
        if text:
            text_items = text.split("\n")
            display_text = self.center_bold_stack(text_items)
            self.dialog.ui.label.setText(display_text)
        
        self.dialog.exec_()
        self.dialog = None

    def open_not_saved_dialog(self):
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_NotSavedDialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.setAttribute(
            core.Qt.WA_DeleteOnClose)
        self.dialog.ui.buttonBox.accepted.connect(self.save_screen)
        self.dialog.exec_()
        self.dialog = None

    def open_watershed_dialog(self, item):
        item_type = item.block_type
        item_num = item.block_index
        key = item.itemid
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_watershed_dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.watershed_id_display.setText(key)
        self.dialog.ui.display_wateshed_name.setText(key)
        self.dialog.ui.select_inflow_file.clicked.connect(
            self.get_file_name)
        self.dialog.ui.buttonBox.accepted.connect(
            self.get_info_watershed)
        self.dialog.setAttribute(core.Qt.WA_DeleteOnClose)
        item_dict = self.dialog_dict.get(key, None)
        # if an entry exists for this dialog, populate it
        if item_dict:
            dlg_populate.WS(self, item_dict)
        self.dialog.exec_()
        self.dialog = None

    def open_reservoir_dialog(self, item):
        item_type = item.block_type
        item_num = item.block_index
        key = item.itemid
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_reservoirDialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.ident_reservoir.setText(key)
        self.dialog.ui.reservoir_id_display.setText(key)
        self.dialog.ui.spillway_table.resizeColumnsToContents()
        self.dialog.ui.outlet_table.resizeColumnsToContents()
        self.dialog.ui.num_spill_edit.textEdited.connect(
            self.table_set_row)
        self.dialog.ui.num_outlet_edit.textEdited.connect(
            self.table_set_row)
        self.dialog.ui.evap_depth_table_radio.toggled.connect(
            self.reservoir_button)
        self.dialog.ui.evap_depth_file_radio.toggled.connect(
            self.reservoir_button)
        self.dialog.ui.rule_curve_table_radio.toggled.connect(
            self.reservoir_button)
        self.dialog.ui.rule_curve_file_radio.toggled.connect(
            self.reservoir_button)
        self.dialog.ui.curve_file_select.clicked.connect(
            self.get_file_name)
        self.dialog.ui.select_evap_file.clicked.connect(
            self.get_file_name)
        self.dialog.ui.select_evap_file.hide()
        self.dialog.ui.evap_file_edit.hide()
        self.dialog.ui.evap_table.hide()
        self.dialog.ui.curve_file_select.hide()
        self.dialog.ui.curve_file_edit.hide()
        self.dialog.ui.rule_curve_table.hide()
        self.dialog.ui.evap_file_box.hide()
        self.dialog.ui.evap_box.hide()
        self.dialog.ui.rule_curve_box.hide()
        self.dialog.ui.vol_gamma_edit.setEnabled(False)
        if not self.check_gen_setup():
            errormsg = "You must complete the general setup menu before editing reservoirs."
            self.open_error_dialog(f"Error: {errormsg}")
            return 

        time_steps = self.gen_setup_dict['ntime_steps']
        num_restric = self.gen_setup_dict['nrestric']

        self.dialog.ui.target_rest_table.setRowCount(1)
        self.dialog.ui.target_rest_table.setColumnCount(int(num_restric))
        self.dialog.ui.rule_curve_table.setColumnCount(int(time_steps))
        self.dialog.ui.evap_table.setColumnCount(
            int(time_steps))

        self.dialog.ui.buttonBox.accepted.connect(
            self.get_info_reservoir)
        self.dialog.setAttribute(
            core.Qt.WA_DeleteOnClose)
        item_dict = self.dialog_dict.get(key, None)
        # if an entry exists for this dialog, populate it
        if item_dict:
            dlg_populate.RES(self, item_dict)
        self.dialog.exec_()
        self.dialog = None

    def open_user_dialog(self, item):
        item_type = item.block_type
        item_num = item.block_index
        key = item.itemid
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_user_dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.user_name_display.setText(key)
        self.dialog.ui.user_id_display.setText(key)
        self.dialog.ui.user_dia_tab.setTabEnabled(3, False)
        self.dialog.ui.user_dia_tab.setStyleSheet(
            "QTabBar::tab::disabled {width: 0; height:0; margin:0; padding:0; border: none;}")
        if not self.check_gen_setup():
            errormsg = "You must complete the general setup menu before editing users."
            self.open_error_dialog(f"Error: {errormsg}")
            return 

        time_steps = self.gen_setup_dict['ntime_steps']
        num_restric = self.gen_setup_dict['nrestric']

        self.dialog.ui.demand_table.setColumnCount(
            int(time_steps))
        self.dialog.ui.hydro_table.resizeColumnsToContents()
        self.dialog.ui.hydro_elev_table.setRowCount(1)
        self.dialog.ui.hydro_elev_table.setColumnCount(
            int(time_steps))
        self.dialog.ui.restrict_frac_table.setColumnCount(
            int(num_restric))
        self.dialog.ui.restrict_comp_table.setColumnCount(
            int(num_restric))
        self.dialog.ui.table_radio.toggled.connect(
            self.user_button)
        self.dialog.ui.table_radio_2.toggled.connect(
            self.user_button)
        self.dialog.ui.file_radio.toggled.connect(
            self.user_button)
        self.dialog.ui.file_radio_2.toggled.connect(
            self.user_button)
        self.dialog.ui.demand_file_button.clicked.connect(
            self.get_file_name)
        self.dialog.ui.elev_file_button.clicked.connect(
            self.get_file_name)
        self.dialog.ui.demand_file_box.hide()
        self.dialog.ui.demand_table.hide()
        self.dialog.ui.elev_file_edit.hide()
        self.dialog.ui.elev_file_button.hide()
        self.dialog.ui.hydro_elev_table.hide()
        self.dialog.ui.demand_data_box.hide()
        self.dialog.ui.num_turbines_edit.textEdited.connect(
            self.table_set_row)
        self.dialog.ui.buttonBox.accepted.connect(
            self.get_info_user)
        self.dialog.ui.user_type_combo.currentIndexChanged.connect(
            self.hydro_tab_show)
        self.dialog.setAttribute(core.Qt.WA_DeleteOnClose)
        item_dict = self.dialog_dict.get(key, None)
        # if an entry exists for this dialog, populate it
        if item_dict:
            dlg_populate.US(self, item_dict)
        self.dialog.exec_()
        self.dialog = None

    def open_sink_dialog(self, item):
        item_type = item.block_type
        item_num = item.block_index
        key = item.itemid
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_sink_dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.sink_id_display.setText(key)
        self.dialog.ui.lineEdit.setText(key)
        self.dialog.ui.buttonBox.accepted.connect(
            self.get_info_sink)
        self.dialog.setAttribute(core.Qt.WA_DeleteOnClose)
        item_dict = self.dialog_dict.get(key, None)
        # if an entry exists for this dialog, populate it
        if item_dict:
            dlg_populate.SINK(self, item_dict)
        self.dialog.exec_()
        self.dialog = None

    def open_link_dialog(self, item):
        item_num = item.block_index
        key = item.itemid
        start_node = item.start_node
        stop_node = item.stop_node
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_link_dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.link_name_display.setText(key)
        self.dialog.ui.link_id_display.setText(item_num)
        self.dialog.ui.type_start_display.setText(start_node[0])
        self.dialog.ui.type_end_display.setText(stop_node[0])
        self.dialog.ui.start_node_display.setText(start_node[1:])
        self.dialog.ui.end_node_display.setText(stop_node[1:])
        self.dialog.ui.return_flow_box.hide()
        self.dialog.ui.yes_rad_button.toggled.connect(
            self.button_toggled)
        self.dialog.ui.nlags_edit.textEdited.connect(
            self.table_set_column)
        self.dialog.ui.buttonBox.accepted.connect(
            self.get_info_link)
        self.dialog.setAttribute(core.Qt.WA_DeleteOnClose)
        item_dict = self.dialog_dict.get(key, None)
        # if an entry exists for this dialog, populate it
        if item_dict:
            dlg_populate.LINK(self, item_dict)
        self.dialog.exec_()
        self.dialog = None

    def open_junction_dialog(self, item):
        item_type = item.block_type
        item_num = item.block_index
        key = item.itemid
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_junction_dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.flow_jun_name_display.setText(key)
        self.dialog.ui.flow_jun_id_display.setText(key)
        self.dialog.ui.buttonBox.accepted.connect(
            self.get_info_junction)
        self.dialog.setAttribute(core.Qt.WA_DeleteOnClose)
        item_dict = self.dialog_dict.get(key, None)
        # if an entry exists for this dialog, populate it
        if item_dict:
            dlg_populate.JUN(self, item_dict)
        self.dialog.exec_()
        self.dialog = None

    def open_interbasin_dialog(self, item):
        item_type = item.block_type
        item_num = item.block_index
        key = item.itemid
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_interbasin_dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.int_basin_name_display.setText(key)
        self.dialog.ui.interbasin_id_display.setText(key)
        self.dialog.ui.file_radio.toggled.connect(
            self.interbasin_button)
        self.dialog.ui.table_radio.toggled.connect(
            self.interbasin_button)
        self.dialog.ui.file_button.clicked.connect(
            self.get_file_name)
        self.dialog.ui.flow_file_edit.hide()
        self.dialog.ui.file_button.hide()
        self.dialog.ui.ave_flows_table.hide()
        self.dialog.ui.ave_flow_box.hide()
        if not self.check_gen_setup():
            errormsg = "You must complete the general setup menu before editing interbasin transfers."
            self.open_error_dialog(f"Error: {errormsg}")
            return 

        time_steps = self.gen_setup_dict['ntime_steps']

        self.dialog.ui.ave_flows_table.setColumnCount(
            int(time_steps))
        self.dialog.ui.buttonBox.accepted.connect(
            self.get_info_interbasin)
        self.dialog.setAttribute(
            core.Qt.WA_DeleteOnClose)
        item_dict = self.dialog_dict.get(key, None)
        # if an entry exists for this dialog, populate it
        if item_dict:
            dlg_populate.IB(self, item_dict)
        self.dialog.exec_()
        self.dialog = None
    
    def open_multi_edit_dialog(self):
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_multi_edit_dialog()
        self.dialog.ui.setupUi(self.dialog)
        # Items:
        # block_type_combo : select Reservoir, User, etc..
        # attribute_selector : choose what attributes to edit (different for each block)
        # attribute_editor : table widget for editing and displaying attributes
        # self.dialog.ui.block_type_combo.set
        self.medit_combo_slot()
        self.dialog.ui.block_type_combo.currentIndexChanged.connect(
            self.medit_combo_slot)
        self.dialog.ui.attribute_selector.clicked.connect(
            self.medit_att_selector_slot)
        self.dialog.ui.buttonBox.accepted.connect(
            self.get_info_medit)
        btn = self.dialog.ui.buttonBox.button(widgets.QDialogButtonBox.Apply)
        btn.clicked.connect(self.get_info_medit)
        self.dialog.setAttribute(core.Qt.WA_DeleteOnClose)
        
        self.dialog.exec_()
        self.dialog = None
    
    def open_help_dialog(self):
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_help_dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.setAttribute(core.Qt.WA_DeleteOnClose)
        doc_file = os.path.join(os.getcwd(), "docs", "html", "doc.html")
        self.dialog.ui.help_view.load(core.QUrl().fromLocalFile(doc_file))
        self.dialog.exec_()
        self.dialog = None

    def medit_combo_slot(self):
        table = self.dialog.ui.attribute_editor
        selector = self.dialog.ui.attribute_selector
        block_type = self.dialog.ui.block_type_combo.currentText()
        rows = []
        btype = block_type[0]
        name_map = {
            "R":"reservoir_Name",
            "U":"user_Name",
            "W":"watershed_Name",
            "J":"junction_Name",
            "I":"interbasin_Name",
        }
        for bid, (block, label) in self.block_objects.items():
            if bid[0] == btype:
                block_dict = self.dialog_dict.get(bid, None)
                if block_dict:
                    name = block_dict.get(name_map[btype], bid)
                    rows.append((bid,name))
                else:
                    rows.append((bid,bid))
        rows.sort(key=lambda x: int(x[0][1:]))
        if len(rows) != 0:
            row_ids, row_labels = zip(*rows)
        else:
            row_ids, row_labels = [], []

        self.row_map = {row_labels[i]:row_ids[i] for i in range(len(row_labels))}
        table.setRowCount(len(row_labels))
        table.setVerticalHeaderLabels(row_labels)
        
        list_items = self.attribute_dict[btype].keys()
        selector.clear()
        selector.addItems(list_items)
        self.medit_att_selector_slot()

    def medit_att_selector_slot(self):
        table = self.dialog.ui.attribute_editor
        selector = self.dialog.ui.attribute_selector
        block_type = self.dialog.ui.block_type_combo.currentText()
        attribute_choice = selector.currentItem()
        if attribute_choice:
            att_text = attribute_choice.text()
        else:
            att_text = "Select Attribute"
        table.setHorizontalHeaderLabels([att_text])
        self.populate_medit_table()

    def populate_medit_table(self):
        block_type = self.dialog.ui.block_type_combo.currentText()
        btype = block_type[0]
        table = self.dialog.ui.attribute_editor
        table.clearContents()
        attribute = table.horizontalHeaderItem(0).text()
        rows = [table.verticalHeaderItem(i).text() for i in range(table.rowCount())]
        if attribute != "Select Attribute":
            dict_key = self.attribute_dict[btype][attribute]
            for i, row in enumerate(rows):
                info_key = self.row_map[row]
                data_dict = self.dialog_dict.get(info_key, None)
                if data_dict:
                    data = data_dict.get(dict_key, None)
                    if data:
                        table_item = widgets.QTableWidgetItem(data)
                        table.setItem(i, 0, table_item)

    def get_info_medit(self):
        block_type = self.dialog.ui.block_type_combo.currentText()
        btype = block_type[0]
        table = self.dialog.ui.attribute_editor
        attribute = table.horizontalHeaderItem(0).text()
        rows = [table.verticalHeaderItem(i).text() for i in range(table.rowCount())]
        if attribute != "Select Attribute":
            dict_key = self.attribute_dict[btype][attribute]
            for i, row in enumerate(rows):
                table_item = table.item(i, 0)
                if table_item:
                    text = table_item.text()
                    info_key = self.row_map[row]
                    if info_key not in self.dialog_dict:
                        self.dialog_dict[info_key] = {}
                    self.dialog_dict[info_key][dict_key] = text
                    if attribute == "Name":
                        self.change_label(item_id=self.block_objects[info_key][1], name_tag=text)
        
                

    def link_draw_interface(self, enter=False):
        sel_items = list(self.ui.scene.selectedItems())
        item_id = ''
        for item in sel_items:
            item_id = self.get_item_id(item)
            start = str(
                self.dialog.ui.start_edit.text())
            stop = str(self.dialog.ui.stop_edit.text())
            if start == '':
                self.dialog.ui.start_edit.setText(item_id)
            elif stop == '':
                self.dialog.ui.stop_edit.setText(item_id)
            else:
                if enter:
                    self.linkdraw()

    def plot_dialog(self, figure):
        plot_dialog = widgets.QDialog(self)
        plot_dialog.ui = Ui_plot_display_dialog()
        plot_dialog.ui.setupUi(plot_dialog)

        canvas = FigureCanvas(figure)

        plot_dialog.ui.display_vert_layout.addWidget(canvas)
        plot_dialog.exec_()

    def open_dialogs(self, enter=False):
        sel_items = list(self.ui.scene.selectedItems())
        if self.dlg == 'dlg_closed':
            pass
        else:
            self.dlg = self.dialog.objectName()
        if self.dlg == 'linkDraw_dialog':
            self.link_draw_interface(enter)
        else:
            dialog_map = {
                "W": self.open_watershed_dialog,
                "R": self.open_reservoir_dialog,
                "U": self.open_user_dialog,
                "J": self.open_junction_dialog,
                "S": self.open_sink_dialog,
                "L": self.open_link_dialog,
                "I": self.open_interbasin_dialog
            }
            for item in sel_items:
                item_type = item.block_type
                item_id = item.itemid
                pre_dict = self.dialog_dict.get(item_id, None)
                dialog_map[item_type](item)
                if self.dialog_dict.get(item_id, None) != pre_dict:
                    self.dirty = True
                

    # delete items and labels associated with those items
    def keyPressEvent(self, QKeyEvent):
        delete_key = 0x01000007
        return_key = 0x01000004
        enter_key = 0x01000005
        if QKeyEvent.key() == delete_key:
            sel_items = self.ui.scene.selectedItems()
            if len(sel_items) == 0:
                pass
            elif len(sel_items) > 1:
                for item in sel_items:
                    item_id = self.get_item_id(item)
                    if item_id in self.dialog_dict:
                        self.dialog_dict.pop(item_id)
                    remove_items = self.block_objects[item_id]
                    if item.block_type == "L":
                        link_item = {'link': remove_items[0],
                                     'label': remove_items[1]}
                        del self.link_objects[(item.start_node,item.stop_node)]

                    for remove_item in remove_items:
                        if remove_item:
                            self.ui.scene.removeItem(remove_item)
                    self.block_objects[item_id] = None
            else:
                item = sel_items[0]
                item_id = self.get_item_id(item)
                if item_id in self.dialog_dict:
                    self.dialog_dict.pop(item_id)
                if self.block_objects.get(item_id, None):
                    remove_items = self.block_objects[item_id]
                    for remove_item in remove_items:
                        if remove_item.scene():
                            self.ui.scene.removeItem(remove_item)
                    del self.block_objects[item_id]
                remove_ids = []
                for i, (blocks, link_item) in enumerate(self.link_objects.items()):
                    lstart, lstop = blocks
                    if lstart == item_id or lstop == item_id:
                        self.ui.scene.removeItem(link_item["link"])
                        self.ui.scene.removeItem(link_item["label"])
                        remove_ids.append(blocks)
                for i in remove_ids[::-1]:
                    del self.link_objects[i]

        if QKeyEvent.key() == return_key or QKeyEvent.key() == enter_key:
            self.open_dialogs(enter=True)

    def closeEvent(self, event):
        if self.dirty:
            self.open_not_saved_dialog()

    # opens dialog to allow file saving

    def save_screen(self):
        if not self.save_file_name:
            self.save_screen_as()()
        else:
            sv(self, self.save_file_name)
            self.dirty = False
    
    def save_screen_as(self):
        if not os.path.isdir("graps_graphics"):
            os.mkdir("graps_graphics")
        self.save_file_name = widgets.QFileDialog.getSaveFileName(
                        directory="graps_graphics", filter="*.graps")[0]
        # if the user exits the file dialog without selecting a file
        # self.save_file_name will be an empty string
        # This will be the equivalent of cancelling the save action
        if not self.save_file_name:
            pass
        else:
            sv(self, self.save_file_name)
            self.dirty = False
        

    # opens files for editing
    def file_open(self):
        if not os.path.isdir("graps_graphics"):
            os.mkdir("graps_graphics")
        open_file_name = widgets.QFileDialog.getOpenFileName(
            directory="graps_graphics", filter="*.graps")[0]
        if open_file_name == '':
            pass
        else:
            open_file(self, open_file_name)
            self.change_label()
            self.center_scene()
            self.save_file_name = open_file_name

    def center_scene(self):
        bounds = self.ui.scene.itemsBoundingRect()
        center_x = bounds.x() + bounds.width()/2
        center_y = bounds.y() + bounds.height()/2
        self.ui.view.centerOn(center_x, center_y)

    # Draw links between nodes on the Scene
    def link_draw_fromSave(self, start, stop, num):
        link_start = ''
        link_stop = ''
        items = list(self.ui.scene.items())
        for item in items:
            if item.type() == 7:
                item_name = self.get_item_id(item)
                if start == item_name:
                    link_start = item
                if stop == item_name:
                    link_stop = item
        pen = gui.QPen(core.Qt.black, 1, core.Qt.SolidLine)
        line = core.QLineF()
        startpos = link_start.pos()
        stoppos = link_stop.pos()
        startpos.setY(startpos.y() + self.bitmap_height / 2)
        startpos.setX(startpos.x() + self.bitmap_width / 2)
        stoppos.setY(stoppos.y() + self.bitmap_height / 2)
        stoppos.setX(stoppos.x() + self.bitmap_width / 2)
        line.setPoints(startpos, stoppos)
        link = myGraphicsLineItem(line, f'L{num}', self)
        link.setPen(pen)
        self.ui.scene.addItem(link)

        link_start.children.append(stop)
        link_stop.parents.append(start)

        link_id = str(start) + '->' + str(stop)
        link_item = myGraphicsTextItem(link_id, f'L{num}', self)
        link_item.start_node = link_start.itemid
        link_item.stop_node = link_stop.itemid
        x_pos = (startpos.x() + stoppos.x()) / 2
        y_pos = (startpos.y() + stoppos.y()) / 2
        link_item.setPos(x_pos, y_pos)
        link_item.setZValue(2)
        font = gui.QFont(self.font())
        font.setBold(True)
        link_item.setFont(font)
        link_item.setFlags(widgets.QGraphicsItem.ItemIsSelectable |
                           widgets.QGraphicsItem.ItemIsMovable)
        link.label_item = link_item

        self.ui.scene.addItem(link_item)
        self.link_objects[(link_start.itemid, link_stop.itemid)] = {'link': link, 'label': link_item}
        self.block_objects[f'L{num}'] = (link, link_item)

        name = 'L:' + num
        link.start_node = start
        link.stop_node = stop
        link_item.start_node = start
        link_item.stop_node = stop

        self.ui.scene.clearSelection()
        # self.dirty = True

    # checks if the link being drawn is valid
    def check_link(self, start, stop):
        if len(start) == 0 or len(stop) == 0:
            return False
        else:
            errormsg = "Error: Invalid link."
            if start[0] in ['W', 'I', 'U']:
                good = ['R', 'J', 'S']
                if stop[0] not in good:
                    self.dialog.done(1)
                    self.open_error_dialog(text=errormsg)
                    return False
            if start[0] == 'R':
                good = ['J', 'U', 'S', 'R']
                if stop[0] not in good:
                    self.dialog.done(1)
                    self.open_error_dialog(text=errormsg)
                    return False
            if start[0] == 'J':
                good = ['R', 'U', 'S']
                if stop[0] not in good:
                    self.dialog.done(1)
                    self.open_error_dialog(text=errormsg)
                    return False
            if start[0] == 'S':
                self.dialog.done(1)
                self.open_error_dialog(text=errormsg)
                return False
            return True

    # controls link generation from user interaction
    def linkdraw(self):
        items = list(self.ui.scene.items())
        first_go = 0
        start = str(self.dialog.ui.start_edit.text())
        stop = str(self.dialog.ui.stop_edit.text())
        b_ID_local_start = start.capitalize()
        b_ID_local_stop = stop.capitalize()
        self.dialog.ui.start_edit.setText('')
        self.dialog.ui.stop_edit.setText('')
        self.dialog.ui.start_edit.setFocus()
        check = self.check_link(start, stop)
        if check:
            for item in items:
                if item.type() == 7:
                    item_id = self.get_item_id(item)
                    if item_id == b_ID_local_start:
                        startpos = item.pos()
                    if item_id == b_ID_local_stop:
                        stoppos = item.pos()

            value = self.block_indices[self.block_ID]
            self.block_indices[self.block_ID] += 1

            pen = gui.QPen(core.Qt.black, 1, core.Qt.SolidLine)
            line = core.QLineF()
            startpos.setY(startpos.y() + self.bitmap_height / 2)
            startpos.setX(startpos.x() + self.bitmap_width / 2)
            stoppos.setY(stoppos.y() + self.bitmap_height / 2)
            stoppos.setX(stoppos.x() + self.bitmap_width / 2)
            line.setPoints(startpos, stoppos)
            link = myGraphicsLineItem(line, f'L{value}', self)
            linedraw_go = False
            link.setPen(pen)
            self.ui.scene.addItem(link)

            link_id = f"{b_ID_local_start}->{b_ID_local_stop}"
            link_item = myGraphicsTextItem(link_id, f'L{value}', self)
            link_item_h = link_item.shape().boundingRect().size().height()
            link_item_w = link_item.shape().boundingRect().size().width()
            link_item.start_node = b_ID_local_start
            link_item.stop_node = b_ID_local_stop
            x_pos = (startpos.x() + stoppos.x()) / 2 - link_item_w / 2
            y_pos = (startpos.y() + stoppos.y()) / 2 - link_item_h / 2

            link_item.setPos(x_pos, y_pos)
            link_item.setZValue(2)
            font = gui.QFont(self.font())
            font.setBold(True)
            link_item.setFont(font)
            link_item.setFlags(widgets.QGraphicsItem.ItemIsSelectable |
                               widgets.QGraphicsItem.ItemIsMovable)
            link.label_item = link_item
            self.ui.scene.addItem(link_item)
            self.link_objects[(b_ID_local_start, b_ID_local_stop)] = {'link': link,'label': link_item}

            self.block_objects[f'L{value}'] = (link, link_item)
            name = 'L:' + link_id

            link.start_node = b_ID_local_start
            link.stop_node = b_ID_local_stop
            link_item.start_node = b_ID_local_start
            link_item.stop_node = b_ID_local_stop

            self.ui.scene.clearSelection()

            link_start = self.block_objects[b_ID_local_start][0]
            link_stop = self.block_objects[b_ID_local_stop][0]
            link_start.children.append(stop)
            link_stop.parents.append(start)
            self.dirty = True

    @staticmethod
    def setup_printer():
        printer = printsupp.QPrinter(printsupp.QPrinter.HighResolution)
        printer.setOrientation(printsupp.QPrinter.Landscape)
        return printer

    def paint_scene(self, printer):
        self.ui.scene.render(gui.QPainter(printer))

    # allows user to print scene
    def print_scene(self):
        printer = self.setup_printer()
        dialog = printsupp.QPrintDialog(printer)
        bounds = self.ui.scene.itemsBoundingRect()
        rect = self.ui.scene.sceneRect()
        self.ui.scene.setSceneRect(bounds)
        if dialog.exec_():
            self.ui.scene.clearSelection()
            self.paint_scene(printer)
        self.ui.scene.setSceneRect(rect)
        self.center_scene()

    def print_preview(self):
        printer = self.setup_printer() 
        bounds = self.ui.scene.itemsBoundingRect()
        rect = self.ui.scene.sceneRect()
        self.ui.scene.setSceneRect(bounds)
        dialog = printsupp.QPrintPreviewDialog(printer)
        dialog.paintRequested.connect(self.paint_scene)
        dialog.exec_()
        self.ui.scene.setSceneRect(rect)
        self.center_scene()

    # Controls zoom on gui.QGraphicsScene
    def wheelEvent(self, event: gui.QWheelEvent):
        if event.modifiers() == core.Qt.ControlModifier:
            delta = event.angleDelta()
            y = delta.y()
            x = delta.x()
            exp = 25*abs(y)/y
            factor = 1.41 ** (exp / 240.0)
            self.ui.view.setTransformationAnchor(
                widgets.QGraphicsView.AnchorUnderMouse)
            self.ui.view.setResizeAnchor(
                widgets.QGraphicsView.AnchorUnderMouse)
            self.ui.view.scale(factor, factor)


    # controls what is visible in the general setup menu based on the user selection for the simulation type
    def sim_type_change(self):
        text = str(
            self.dialog.ui.type_sim_combo.currentText())
        if text == 'Forecast':
            self.dialog.ui.sim_info_frame.setVisible(True)
            self.dialog.ui.ensem_input.setVisible(True)
            self.dialog.ui.num_ensembles.setVisible(True)
            self.dialog.ui.analysis_option.setVisible(True)
        elif text == 'Climatology':
            self.dialog.ui.sim_info_frame.setVisible(True)
            self.dialog.ui.ensem_input.setVisible(False)
            self.dialog.ui.num_ensembles.setVisible(False)
            self.dialog.ui.analysis_option.setVisible(False)
            self.dialog.ui.adaptive_box.setVisible(False)
        else:
            self.dialog.ui.sim_info_frame.setVisible(False)
            self.dialog.ui.analysis_option.setVisible(False)
            self.dialog.ui.adaptive_box.setVisible(False)

    # also controls what is visible in the general setup menu based on the user selection for the forecast option
    def forecast_option_change(self):
        if self.dialog.ui.retro_button.isChecked():
            self.dialog.ui.adaptive_box.setVisible(False)
        if self.dialog.ui.adaptive_button.isChecked():
            self.dialog.ui.adaptive_box.setVisible(True)
        if self.dialog.ui.type_sim_combo.currentText() != "Forecast":
            self.dialog.ui.adaptive_box.setVisible(False)

    # opens general setup menu
    def open_dataDialog(self):
        self.dialog = widgets.QDialog(self)
        self.dialog.ui = Ui_genSet_dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.adaptive_box.show()
        self.dialog.setAttribute(core.Qt.WA_DeleteOnClose)
        self.dialog.ui.sim_info_frame.setVisible(False)
        self.dialog.ui.buttonBox.accepted.connect(self.get_info_gs)
        self.dialog.ui.type_sim_combo.setCurrentIndex(4)
        self.dialog.ui.adaptive_button.toggled.connect(
            self.forecast_option_change)
        self.dialog.ui.retro_button.toggled.connect(
            self.forecast_option_change)
        self.dialog.ui.type_sim_combo.currentIndexChanged.connect(
            self.forecast_option_change)
        self.dialog.ui.analysis_option.setVisible(False)
        self.dialog.ui.adaptive_box.setVisible(False)
        self.dialog.ui.type_sim_combo.currentIndexChanged.connect(
            self.sim_type_change)
        self.dialog.ui.year_sim_input.textEdited.connect(self.table_set_column)
        if len(self.gen_setup_dict) != 0:
            dlg_populate.GS(self, self.gen_setup_dict)
        self.dialog.exec_()

    # changes the number of columns in tables in certain dialogs
    def table_set_column(self):
        sender = self.sender()
        sending_object = sender.objectName()
        if sending_object == 'year_sim_input':
            number = str(self.dialog.ui.year_sim_input.text())
            number = number
            if number != '':
                number = int(number)
                self.dialog.ui.sim_input_table.setColumnCount(number)
                header_labels = []
                for num in range(number):
                    if num == 0:
                        'do nothing'
                    else:
                        header_labels.append(str(num))
                self.dialog.ui.sim_input_table.setHorizontalHeaderLabels(
                    header_labels)
        elif sending_object == 'nlags_edit':
            number = str(self.dialog.ui.nlags_edit.text())
            if number != '':
                number = int(number)
                self.dialog.ui.return_flow_table.setColumnCount(number)
                header_labels = []
                for num in range(number):
                    if num == 0:
                        pass
                    else:
                        header_labels.append(str(num))
                self.dialog.ui.return_flow_table.setHorizontalHeaderLabels(
                    header_labels)

    # changes the number of rows in tables in certain dialogs
    def table_set_row(self):
        sender = self.sender()
        sending_object = sender.objectName()
        if sending_object == 'num_spill_edit':
            number = str(self.dialog.ui.num_spill_edit.text())
            if number != '':
                number = int(number)
                self.dialog.ui.spillway_table.setRowCount(number)
                self.dialog.ui.spillway_table.resizeColumnsToContents()
        elif sending_object == 'num_outlet_edit':
            number = str(self.dialog.ui.num_outlet_edit.text())
            if number != '':
                number = int(number)
                self.dialog.ui.outlet_table.setRowCount(number)
                self.dialog.ui.outlet_table.resizeColumnsToContents()

        elif sending_object == 'num_turbines_edit':
            number = str(self.dialog.ui.num_turbines_edit.text())
            if number != '':
                number = int(number)
                self.dialog.ui.hydro_table.setRowCount(number)
                self.dialog.ui.hydro_table.resizeColumnsToContents()

    def hydro_tab_show(self):
        sender = self.sender()
        if sender.currentText() == "Hydropower":
            self.dialog.ui.user_dia_tab.setTabEnabled(3, True)
            self.dialog.ui.user_dia_tab.setStyleSheet(
            "QTabBar::tab::enabled {}")
        else:
            self.dialog.ui.user_dia_tab.setTabEnabled(3, False)
            self.dialog.ui.user_dia_tab.setStyleSheet(
            "QTabBar::tab::disabled {width: 0; height:0; margin:0; padding:0; border: none;}")

    def read_space_delim_file(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                lst = lines[0].strip("\r\n").split()
                return lst
        except FileNotFoundError as e:
            return []

            

    # gets the file name for certain fields in dialog boxes
    def get_file_name(self):
        sending_button = self.sender()
        sending_object = sending_button.objectName()
        filename = widgets.QFileDialog.getOpenFileName()[0]
        # watershed
        if sending_object == 'select_forecast_file':
            self.dialog.ui.forecast_file_input.setText(filename)
        elif sending_object == 'select_inflow_file':
            self.dialog.ui.inflows_file_input.setText(filename)
        # reservoir
        elif sending_object == 'select_evap_file':
            self.dialog.ui.evap_file_edit.setText(filename)
        elif sending_object == 'curve_file_select':
            self.dialog.ui.curve_file_edit.setText(filename)
        # user
        elif sending_object == 'elev_file_button':
            self.dialog.ui.elev_file_edit.setText(filename)
        elif sending_object == 'demand_file_button':
            self.dialog.ui.demand_file_edit.setText(filename)
        # interbasin
        elif sending_object == 'file_button':
            self.dialog.ui.flow_file_edit.setText(filename)

    # gets the info from the general setup menu and stores it in the self.gen_setup_dict
    def get_info_gs(self):
        ntime_steps = str(self.dialog.ui.time_step_input.text())
        nrestric = str(self.dialog.ui.restrictions_input.text())
        hydro_coeff = str(self.dialog.ui.hydro_coeff_input.text())
        sim_type = str(self.dialog.ui.type_sim_combo.currentText())
        nyears = str(self.dialog.ui.year_input.text())
        nensembles = str(self.dialog.ui.ensem_input.text())
        if nensembles == "":
            nensembles = "1"
        if self.dialog.ui.retro_button.isChecked():
            forecast_option = 'Retrospective'
        elif self.dialog.ui.adaptive_button.isChecked():
            forecast_option = 'Adaptive'
        else:
            forecast_option = 'Null'
        forecast_info = []
        nyear_sim = ''
        if sim_type == "Forecast" and forecast_option == "Adaptive":
            nyear_sim = self.dialog.ui.year_sim_input.text()
            if nyear_sim:
                for int_variable in range(int(nyear_sim)):
                    try:
                        current_item = self.dialog.ui.sim_input_table.item(
                            0, int_variable)
                        user_input = str(current_item.text())
                        forecast_info.append(user_input)
                    except:
                        continue
        self.gen_setup_dict['ntime_steps'] = ntime_steps
        self.gen_setup_dict['nrestric'] = nrestric
        self.gen_setup_dict['hydro_coeff'] = hydro_coeff
        self.gen_setup_dict['sim_type'] = sim_type
        self.gen_setup_dict['nyears'] = nyears
        self.gen_setup_dict['nensembles'] = nensembles
        self.gen_setup_dict['forecast_option'] = forecast_option
        self.gen_setup_dict['forecast_info'] = forecast_info
        self.gen_setup_dict['nyear_sim'] = nyear_sim

    # gets info from the watershed dialog and stores it in the self.dialog_dict
    def get_info_watershed(self):
        watershed_ID = str(self.dialog.ui.watershed_id_display.text())
        watershed_Name = str(self.dialog.ui.id_display.text())
        drain_Area = str(self.dialog.ui.drain_input.text())
        inflows_file = str(self.dialog.ui.inflows_file_input.text())
        watershed_dict = {}
        watershed_dict['watershed_Name'] = watershed_Name
        watershed_dict['drain_Area'] = drain_Area
        watershed_dict['inflows_file'] = inflows_file
        self.dialog_dict[watershed_ID] = watershed_dict
        label_item = self.block_objects[watershed_ID][1]
        self.change_label(item_id=label_item, name_tag=watershed_Name)

    def get_info_reservoir(self):
        reservoir_dict = {}
        # reservoir description tab
        reservoir_ID = str(self.dialog.ui.reservoir_id_display.text())
        reservoir_Name = str(self.dialog.ui.name_edit.text())
        res_latitude = str(self.dialog.ui.latitude_edit.text())
        res_longitude = str(self.dialog.ui.longitude_edit.text())
        res_min_elev = str(self.dialog.ui.min_elev_edit.text())
        res_max_elev = str(self.dialog.ui.max_elev_edit.text())
        res_min_storage = str(self.dialog.ui.min_stor_edit.text())
        res_max_storage = str(self.dialog.ui.max_stor_label_2.text())
        res_current_storage = str(self.dialog.ui.current_stor_edit.text())
        reservoir_dict['reservoir_Name'] = reservoir_Name
        reservoir_dict['res_latitude'] = res_latitude
        reservoir_dict['res_longitude'] = res_longitude
        reservoir_dict['res_min_elev'] = res_min_elev
        reservoir_dict['res_max_elev'] = res_max_elev
        reservoir_dict['res_min_storage'] = res_min_storage
        reservoir_dict['res_max_storage'] = res_max_storage
        reservoir_dict['res_current_storage'] = res_current_storage
        time_steps = int(self.gen_setup_dict['ntime_steps'])
        evap_option = 0
        if self.dialog.ui.evap_depth_table_radio.isChecked():
            evap_option = 'Table'
        elif self.dialog.ui.evap_depth_file_radio.isChecked():
            evap_option = str(
                self.dialog.ui.evap_file_edit.text())
      
        
        # Evaporation Tab
        int_variable = 0

        evap_info = []
        if evap_option:
            if evap_option == 'Table':
                for int_variable in range(time_steps):
                    current_item = self.dialog.ui.evap_table.item(
                            0, int_variable
                    )
                    try:                    
                        user_input = str(current_item.text())
                    except:
                        user_input = "0"
                    evap_info.append(user_input)
            else:
                evap_info = self.read_space_delim_file(evap_option)

        reservoir_dict['evap_info'] = evap_info
        reservoir_dict['evap_option'] = evap_option

        # Storage Elevation Tab
        elev_alpha = str(self.dialog.ui.elev_alpha_edit.text())
        elev_beta = str(self.dialog.ui.elev_beta_edit.text())
        elev_gamma = str(self.dialog.ui.elev_gamma_edit.text())
        vol_alpha = str(self.dialog.ui.vol_alpha_edit.text())
        vol_beta = str(self.dialog.ui.vol_beta_edit.text())
        vol_gamma = str(self.dialog.ui.vol_gamma_edit.text())

        reservoir_dict['elev_alpha'] = elev_alpha
        reservoir_dict['elev_beta'] = elev_beta
        reservoir_dict['elev_gamma'] = elev_gamma
        reservoir_dict['vol_alpha'] = vol_alpha
        reservoir_dict['vol_beta'] = vol_beta
        reservoir_dict['vol_gamma'] = vol_gamma

        # Operational Information Tab
        target_storage = str(self.dialog.ui.tar_stor_edit.text())
        storage_probability = str(self.dialog.ui.stor_prob_edit.text())
        reservoir_dict['target_storage'] = target_storage
        reservoir_dict['storage_probability'] = storage_probability

        # Rule Curve Table in Op Info Tab
        rule_curve_option = 0
        if self.dialog.ui.rule_curve_table_radio.isChecked():
            rule_curve_option = 'Table'
        elif self.dialog.ui.rule_curve_file_radio.isChecked():
            rule_curve_option = str(
                self.dialog.ui.curve_file_edit.text())

        lower_rule = []
        upper_rule = []
        if rule_curve_option:
            if rule_curve_option == 'Table':
                for column in range(time_steps):
                    try:
                        lower_item = self.dialog.ui.rule_curve_table.item(
                            0, column).text()
                        upper_item = self.dialog.ui.rule_curve_table.item(
                            1, column).text()
                        lower_rule.append(str(lower_item))
                        upper_rule.append(str(upper_item))
                    except:
                        continue
            else:
                try:
                    with open(rule_curve_option, 'r') as f:
                        data = f.readlines()
                        lower_rule = data[0].split()
                        upper_rule = data[1].split()
                except FileNotFoundError as e:
                    lower_rule = []
                    upper_rule = []

        reservoir_dict['rule_curve_option'] = rule_curve_option
        reservoir_dict['storage_rule'] = lower_rule
        reservoir_dict['flood_rule'] = upper_rule

        # Target Restriction Level Table in Op Info Tab
        column = 0
        target_restrictions = []
        restric_level = int(self.gen_setup_dict['nrestric'])
        for column in range(restric_level):
            try:
                current_item = self.dialog.ui.target_rest_table.item(0, column)
                user_input = str(current_item.text())
                target_restrictions.append(user_input)
            except:
                continue
        reservoir_dict['target_restrictions'] = target_restrictions

        # Spillway/Outlets Tab
        # spillways
        num_spillways = str(
            self.dialog.ui.num_spill_edit.text())

        if num_spillways == '':
            num_spillways = '0'
        num_spillways = int(num_spillways)
        spillways = []
        for row in range(num_spillways):
            spillway_info = {}
            try:
                table_item = self.dialog.ui.spillway_table.item(row, 0)
                spillway_type = str(table_item.text())
                table_item = self.dialog.ui.spillway_table.item(row, 1)
                crest_level = str(table_item.text())
                table_item = self.dialog.ui.spillway_table.item(row, 2)
                max_discharge = str(table_item.text())
                spillway_info['spillway_type'] = spillway_type
                spillway_info['crest_level'] = crest_level
                spillway_info['max_discharge'] = max_discharge
                spillways.append(spillway_info)
            except:
                continue
        reservoir_dict['spillways'] = spillways
        reservoir_dict['num_spillways'] = str(num_spillways)

        # outlets
        num_outlets = str(self.dialog.ui.num_outlet_edit.text())
        if num_outlets == '':
            num_outlets = '0'
        num_outlets = int(num_outlets)
        outlets = []
        for row in range(num_outlets):
            outlet_info = {}
            try:
                table_item = self.dialog.ui.outlet_table.item(row, 0)
                elevation = str(table_item.text())
                table_item = self.dialog.ui.outlet_table.item(row, 1)
                xsc_area = str(table_item.text())
                table_item = self.dialog.ui.outlet_table.item(row, 2)
                max_loss_coeff = str(table_item.text())
                table_item = self.dialog.ui.outlet_table.item(row, 3)
                min_loss_coeff = str(table_item.text())
                outlet_info['elevation'] = elevation
                outlet_info['xsc_area'] = xsc_area
                outlet_info['max_loss_coeff'] = max_loss_coeff
                outlet_info['min_loss_coeff'] = min_loss_coeff
                outlets.append(outlet_info)
            except:
                continue
        reservoir_dict['outlets'] = outlets
        reservoir_dict['num_outlets'] = str(num_outlets)
        self.dialog_dict[reservoir_ID] = reservoir_dict
        label_item = self.block_objects[reservoir_ID][1]
        self.change_label(item_id=label_item, name_tag=reservoir_Name)

    def get_info_user(self):
        user_dict = {}
        # User Description Tab
        user_ID = str(self.dialog.ui.user_id_display.text())
        user_Name = str(self.dialog.ui.user_name_edit.text())
        min_release = str(self.dialog.ui.min_release_edit.text())
        max_release = str(self.dialog.ui.max_release_edit.text())
        tariff = str(self.dialog.ui.tariff_edit.text())
        penalty = str(self.dialog.ui.penalty_edit.text())
        reliability = str(self.dialog.ui.reliability_edit.text())
        restrict_volume = str(self.dialog.ui.contract_restict_edit.text())
        user_type = str(self.dialog.ui.user_type_combo.currentText())
        penalty_comp = str(
            self.dialog.ui.penalty_comp_edit.text())

        user_dict['user_Name'] = user_Name
        user_dict['min_release'] = min_release
        user_dict['max_release'] = max_release
        user_dict['tariff'] = tariff
        user_dict['penalty'] = penalty
        user_dict['reliability'] = reliability
        user_dict['restrict_volume'] = restrict_volume
        user_dict['user_type'] = user_type
        user_dict['penalty_comp'] = penalty_comp

        # Demand Fraction Tab
        # Need to determine # of time steps for demand fraction
        time_steps = self.gen_setup_dict['ntime_steps']
        demand_option = 0
        if self.dialog.ui.table_radio.isChecked():
            demand_option = 'Table'
        elif self.dialog.ui.file_radio.isChecked():
            demand_option = str(
                self.dialog.ui.demand_file_edit.text())

        column = 0
        demand = []
        if demand_option:
            if demand_option == 'Table':
                for column in range(int(time_steps)):
                    try:
                        current_item = self.dialog.ui.demand_table.item(
                            0, column)
                        demand_t = str(current_item.text())
                        demand.append(demand_t)
                    except:
                        continue
            else:
                demand = self.read_space_delim_file(demand_option)
                
        # Restriction Compensation Tab
        restric_num = self.gen_setup_dict['nrestric']
        restric_comp = []
        for column in range(int(restric_num)):
            try:
                current_item = self.dialog.ui.restrict_comp_table.item(
                    0, column)
                compensation = str(current_item.text())
                restric_comp.append(compensation)
            except:
                continue
        restric_frac = []
        for column in range(int(restric_num)):
            try:
                current_item = self.dialog.ui.restrict_frac_table.item(
                    0, column)
                fraction = str(current_item.text())
                restric_frac.append(fraction)
            except:
                continue
        user_dict['demand_option'] = demand_option
        user_dict['demand'] = demand
        user_dict['restric_comp'] = restric_comp
        user_dict['restric_frac'] = restric_frac

        # Hydropower Tab
        if user_type == "Hydropower":
            num_turbines = str(
                self.dialog.ui.num_turbines_edit.text())
            if num_turbines == '':
                num_turbines = '0'

            hydro = []
            for row in range(int(num_turbines)):
                turbine_dict = {}
                current_item = self.dialog.ui.hydro_table.item(row, 0)
                max_discharge = str(current_item.text())
                current_item = self.dialog.ui.hydro_table.item(row, 1)
                capacity = str(current_item.text())
                current_item = self.dialog.ui.hydro_table.item(row, 2)
                efficiency = str(current_item.text())
                current_item = self.dialog.ui.hydro_table.item(row, 3)
                energy_coeff_1 = str(current_item.text())
                current_item = self.dialog.ui.hydro_table.item(row, 4)
                energy_coeff_2 = str(current_item.text())
                current_item = self.dialog.ui.hydro_table.item(row, 5)
                energy_rate = str(current_item.text())
                turbine_dict['max_discharge'] = max_discharge
                turbine_dict['capacity'] = capacity
                turbine_dict['efficiency'] = efficiency
                turbine_dict['energy_coeff_1'] = energy_coeff_1
                turbine_dict['energy_coeff_2'] = energy_coeff_2
                turbine_dict['energy_rate'] = energy_rate
                hydro.append(turbine_dict)

            elev_option = 0
            if self.dialog.ui.table_radio_2.isChecked():
                elev_option = 'Table'
            elif self.dialog.ui.file_radio_2.isChecked():
                elev_option = str(
                    self.dialog.ui.elev_file_edit.text())

            turb_elev = []
            if elev_option:
                if elev_option == 'Table':
                    for column in range(int(time_steps)):
                        try:
                            current_item = self.dialog.ui.hydro_elev_table.item(
                                0, column)
                            elevation = str(current_item.text())
                            turb_elev.append(elevation)
                        except:
                            continue
                else:
                    turb_elev = self.read_space_delim_file(elev_option)
        else:
            elev_option = "0"
            num_turbines = "0"
            turb_elev = []
            hydro = []
            

        user_dict['elev_option'] = elev_option
        user_dict['num_turbines'] = num_turbines
        user_dict['turbine_elevs'] = turb_elev
        user_dict['hydro'] = hydro
        self.dialog_dict[user_ID] = user_dict
        label_item = self.block_objects[user_ID][1]
        self.change_label(item_id=label_item, name_tag=user_Name)

    def get_info_interbasin(self):
        time_steps = self.gen_setup_dict['ntime_steps']
        interbasin_dict = {}
        interbasin_ID = str(
            self.dialog.ui.interbasin_id_display.text())
        interbasin_Name = str(
            self.dialog.ui.interbasin_name_edit.text())
        drain_area = str(
            self.dialog.ui.drainage_area_edit.text())
        flow_option = 0
        if self.dialog.ui.table_radio.isChecked():
            flow_option = 'Table'
        elif self.dialog.ui.file_radio.isChecked():
            flow_option = str(
                self.dialog.ui.flow_file_edit.text())
        column = 0
        average_flows = []
        if flow_option:
            if flow_option == "Table":
                for column in range(int(time_steps)):
                    try:
                        current_item = self.dialog.ui.ave_flows_table.item(0, column)
                        flow = str(current_item.text())
                        average_flows.append(flow)
                    except:
                        continue
            else:
                average_flows = self.read_space_delim_file(flow_option)

        interbasin_dict['flow_option'] = flow_option
        interbasin_dict['interbasin_Name'] = interbasin_Name
        interbasin_dict['drain_area'] = drain_area
        interbasin_dict['average_flows'] = average_flows
        self.dialog_dict[interbasin_ID] = interbasin_dict
        label_item = self.block_objects[interbasin_ID][1]
        self.change_label(item_id=label_item, name_tag=interbasin_Name)

    def get_info_junction(self):
        junction_dict = {}
        junction_ID = str(
            self.dialog.ui.flow_jun_id_display.text())
        junction_Name = str(
            self.dialog.ui.flow_jun_node_edit.text())
        junction_dict['junction_Name'] = junction_Name
        self.dialog_dict[junction_ID] = junction_dict
        label_item = self.block_objects[junction_ID][1]
        self.change_label(item_id=label_item, name_tag=junction_Name)

    def get_info_sink(self):
        sink_dict = {}
        sink_ID = str(
            self.dialog.ui.sink_id_display.text())
        sink_Name = str(
            self.dialog.ui.sink_name_edit.text())
        max_storage = str(
            self.dialog.ui.max_store_edit.text())
        sink_dict['sink_Name'] = sink_Name
        sink_dict['max_storage'] = max_storage
        self.dialog_dict[sink_ID] = sink_dict
        label_item = self.block_objects[sink_ID][1]
        self.change_label(item_id=label_item, name_tag=sink_Name)

    def get_info_link(self):
        link_dict = {}
        link_ID = str(
            self.dialog.ui.link_name_display.text())
        link_Name = str(
            self.dialog.ui.link_name_edit_2.text())
        start_node = f"{self.dialog.ui.type_start_display.text()}{self.dialog.ui.start_node_display.text()}"
        stop_node = f"{self.dialog.ui.type_end_display.text()}{self.dialog.ui.end_node_display.text()}"
        min_discharge = str(
            self.dialog.ui.min_disch_edit.text())
        max_discharge = str(
            self.dialog.ui.max_disch_edit.text())
        loss_factor = str(
            self.dialog.ui.loss_fact_edit.text())
        return_flow = ''
        if self.dialog.ui.yes_rad_button.isChecked():
            return_flow = 'Yes'
        else:
            return_flow = 'No'
        nlags = str(self.dialog.ui.nlags_edit.text())
        if nlags == '':
            nlags = '0'
        column = 0

        ret_flows = []
        for column in range(int(nlags)):
            try:
                current_item = self.dialog.ui.return_flow_table.item(0, column)
                flow = str(current_item.text())
                ret_flows.append(flow)
            except:
                continue
        link_dict['link_ID'] = link_ID
        link_dict['link_Name'] = link_Name
        link_dict['start_node'] = start_node
        link_dict['stop_node'] = stop_node
        link_dict['min_discharge'] = min_discharge
        link_dict['max_discharge'] = max_discharge
        link_dict['loss_factor'] = loss_factor
        link_dict['return_flow'] = return_flow
        link_dict['nlags'] = nlags
        link_dict['ret_flows'] = ret_flows
        self.dialog_dict[link_ID] = link_dict
        label_item = self.link_objects[(start_node, stop_node)]["label"]
        self.change_label(item_id=label_item, name_tag=link_Name)


class Worker(core.QRunnable):
    def __init__(self, func, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    @core.pyqtSlot()
    def run(self):
        self.func(*self.args, **self.kwargs)

def main():
    op_sys = platform.system()
    pool = core.QThreadPool()

    if hasattr(core.Qt, "AA_EnableHighDpiScaling"):
        widgets.QApplication.setAttribute(core.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(core.Qt, "AA_UseHighDpiPixmaps"):
        widgets.QApplication.setAttribute(core.Qt.AA_UseHighDpiPixmaps, True)
    app = widgets.QApplication(sys.argv)
    
    if op_sys == "Windows":
        app.setStyle("Fusion")
    
    screen_res = app.desktop().screenGeometry()
    
    mainscreen = MyMainScreen(pool, screen_res=screen_res)
    mainscreen.showMaximized()
    app.exec_()

if __name__ == "__main__":
    main()
