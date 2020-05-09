from PyQt5 import QtCore, QtGui, QtWidgets
from IPython import embed as II


class myPixmapItem(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, parent=None, itemid=None, owner=None):
        super(myPixmapItem, self).__init__(parent)
        self.parent = parent
        self.owner = owner
        self.parents = []
        self.children = []
        self.itemid = itemid
        self.block_type = itemid[0]
        self.block_index = itemid[1:]
    
    def mouseDoubleClickEvent(self, event):
        self.owner.open_dialogs()
        return super().mouseDoubleClickEvent(event)