from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem, QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QWheelEvent

class CustomGraphicsScene (QGraphicsScene):
    def __init__(self, main_window):
        super().__init__()
        self.mainwindow = main_window

    def mouseDoubleClickEvent(self, event):
        # double click the mouse and remove the item
        item = self.itemAt(event.scenePos(), self.views()[0].transform())
        self.removeItem(item)

        super().mouseDoubleClickEvent(event)

    def wheelEvent (self, event):
        # going to caputrue any events with the wheel
        # only want to caputre if the control button is pressed
        if not event.modifiers() & Qt.ControlModifier:
            event.ignore()
            return
        
        # IF the control button IS pressed
        num_pixels = event.delta()
        if num_pixels > 0:
            self.mainwindow.zoom_in()
        if num_pixels < 0:
            self.mainwindow.zoom_out()

        event.accept() # this does not pass on the event