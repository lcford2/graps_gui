from __future__ import division
from builtins import str
from past.utils import old_div
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import dictionaries as dlg_populate
import sys
import pickle
from IPython import embed as II


def save_view(self, filename, gs_dict, info_dict):
    items = list(self.ui.scene.items())
    output_items = []
    for item in items:
        item_type = str(type(item))
        if item_type[-12:] == "PixmapItem'>":
            block_name = item.data(1)
            block_num = item.data(2)
            output_items.append(f"{block_name}{block_num}:{item.pos()}")
        if item_type[-10:] == "LineItem'>":
            block_name = item.data(1)
            block_num = item.data(2)
            start = item.data(3)
            stop = item.data(4)
            output_items.append(f"{block_name}{block_num}:{start}-{stop}")
    output = {"gs_dict": gs_dict,
              "items": output_items, "info_dict": info_dict}
    with open(filename, "wb") as f:
        pickle.dump(output, f)
