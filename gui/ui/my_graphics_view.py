
from PyQt5 import QtCore, QtGui, QtWidgets


class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(GraphicsView, self).__init__(parent)
        self.parent = parent

    def wheelEvent(self, event):
        if (event.type() == QtCore.QEvent.Wheel):
            if event.buttons() == QtCore.Qt.RightButton or event.modifiers() == QtCore.Qt.ControlModifier:
                delta = event.angleDelta()
                y = delta.y()
                x = delta.x()
                if y == 0:
                    exp = 0
                else:
                    exp = abs(y)/y * 25
                factor = 1.41 ** (exp / 240.0)
                self.scale(factor, factor)
            else:
                # this way we scroll if the right button is clicked or if
                # the control button is not pressed
                super(GraphicsView, self).wheelEvent(event)

    def keyPressEvent(self, event):
        super(GraphicsView, self).keyPressEvent(event)
        control_key = 0x01000021
        alt_key = 0x01000023
        up_key = 0x01000013
        down_key = 0x01000015
        if event.key() == control_key:
            self.setDragMode(GraphicsView.ScrollHandDrag)
        if event.key() == alt_key:
            self.setDragMode(GraphicsView.RubberBandDrag)
        return super().keyPressEvent(event)
    
    def keyReleaseEvent(self, event):
        super(GraphicsView, self).keyReleaseEvent(event)
        control_key = 0x01000021
        alt_key = 0x01000023
        key = event.key()
        if key == control_key or key == alt_key:
            self.setDragMode(GraphicsView.NoDrag)
        return super().keyReleaseEvent(event)