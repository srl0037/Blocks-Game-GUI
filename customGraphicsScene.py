from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem, QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QWheelEvent
import random

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
            self.mainwindow.view.zoom_in()
        if num_pixels < 0:
            self.mainwindow.view.zoom_out()

        event.accept() # this makes sure the event is not passed on not

    def clear_all_squares(self):
        selected_items = self.items() # returns a list
        # for every item, delete
        for item in selected_items:
            self.mainwindow.scene.removeItem(item)
            

    def clear_half_squares(self):
        selected_items = self.items() # returns a list

        len_list = len(selected_items)
        for i in range (0, int(len_list/2)):
            item_to_remove = random.choice(selected_items)
            self.mainwindow.scene.removeItem(item_to_remove)
            selected_items.remove(item_to_remove)