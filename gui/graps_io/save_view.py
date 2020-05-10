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
        if not getattr(item, 'block_type', None):
            continue
        item_type = item.item_type
        if item_type == "pixmap":
            itemid = item.itemid
            output_items.append(f"{itemid}:{item.pos()}")
        if item_type == "line":
            itemid = item.itemid
            start = item.start_node
            stop = item.stop_node
            output_items.append(f"{itemid}:{start}-{stop}")
    output = {"gs_dict": gs_dict,
              "items": output_items, "info_dict": info_dict}
    with open(filename, "wb") as f:
        pickle.dump(output, f)
