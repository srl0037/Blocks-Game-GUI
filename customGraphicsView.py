from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QMainWindow, QGraphicsItem
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt
import random

class CustomGraphicsView (QGraphicsView):
    def __init__(self, main_window, scene,):
        super().__init__(scene)
        self.mainwindow = main_window
        # self.viewscene = scene

        # this ensure that the view can get keyboard focus
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()

    # this is the fucntion that will override the keyboard input
    def keyPressEvent(self, event: QKeyEvent):

        if event.key() == Qt.Key_Space:
            # add another square
            # make a list of pens and make a random function to pick
            color_picked = random.choice(self.mainwindow.all_colors)
            new_rect = self.mainwindow.scene.addRect(100, 100, 50, 50, color_picked)
            # make it able to move
            new_rect.setFlag(QGraphicsItem.ItemIsMovable)

        else:
            super().keyPressEvent(event)

    