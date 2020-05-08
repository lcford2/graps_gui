
from PyQt5 import QtCore, QtGui, QtWidgets


class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(GraphicsView, self).__init__(parent)
        self.parent = parent

    def wheelEvent(self, event):
        super(GraphicsView, self).wheelEvent(event)
        if (event.type() == QtCore.QEvent.Wheel):
            button = QtCore.Qt.RightButton
            if button == 1:
                delta = event.angleDelta()
                y = delta.y()
                x = delta.x()
                if y > 0:
                    exp = 25
                elif y < 0:
                    exp = -25
                else:
                    exp = 0
                factor = 1.41 ** (exp / 240.0)
                self.scale(factor, factor)

    # def mousePressEvent(self, event):
    #     super(GraphicsView, self).mousePressEvent(event)
    #     if event.modifiers() == QtCore.Qt.ControlModifier:
    #         self.setDragMode(GraphicsView.ScrollHandDrag)
    #     return super().mousePressEvent(event)

    # def mouseReleaseEvent(self, event):
    #     super(GraphicsView, self).mouseReleaseEvent(event)
    #     self.setDragMode(GraphicsView.NoDrag)
    #     return super().mouseReleaseEvent(event)
