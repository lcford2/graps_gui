from builtins import str
from builtins import range
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import dictionaries as dlg_populate
import sys
import os
from IPython import embed as II
import pickle
block_dict = {'W': 'W.png', 'R': 'R.png', 'I': 'I.png',
              'U': 'U.png', 'S': 'S.png', 'J': 'J.png'}
print_dict = {'W': {}, 'R': {}, 'I': {}, 'U': {}, 'S': {}, 'J': {}, 'L': {}}


def open_file(self, filename):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    self.dialog_dict = data["info_dict"]
    self.gen_setup_dict = data["gs_dict"]
    items = data["items"]
    for line in items:
        ID, info = line.strip("\n").split(':')
        block = ID[0]
        block_num = ID[1:]
        if block != "L":
            trash, info = info.split('(')
            px, py = info.split(',')
            py = py.replace(')', '')
            pointy = float(py.strip()) + 68.0
            pointx = float(px.strip()) + 15.0
            pos = QPointF(pointx, pointy)
            self.createPixmapItem(
                block_dict[block], pos, value=block_num, block_ID=block)
        else:
            start, stop = info.split('-')
            print_dict['L'][block_num] = {}
            print_dict['L'][block_num]['ret_flows'] = {}
            num = block_num
            start = start.strip()
            stop = stop.strip()
            self.link_draw_fromSave(start, stop, num)
