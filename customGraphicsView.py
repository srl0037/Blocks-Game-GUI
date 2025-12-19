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
            
            # need to find the view of where you are and add the rect there
            # determine the area of the visible screen
            visible_scene_rect = self.mapToScene(self.viewport().rect()).boundingRect()
            x_cord_funct = random.uniform(visible_scene_rect.left(), visible_scene_rect.right() - 50)
            y_cord_funct = random.uniform(visible_scene_rect.top(), visible_scene_rect.bottom() - 50)           

            new_rect = self.mainwindow.scene.addRect(x_cord_funct, y_cord_funct, 50, 50, color_picked)
            # make it able to move
            new_rect.setFlag(QGraphicsItem.ItemIsMovable)

        else:
            super().keyPressEvent(event)

    def on_add_combo_activation(self, index):

        # converting the index to int count
        count = 3
        if index == 0: count = 5
        elif index == 1: count = 10
        elif index == 2: count = 20
        elif index == 3: count = 50
        elif index == 4: count = 100
        else: count = 1000


        # for the range you chose
        for i in range(count):
            # pick a range color
            color_picked = random.choice(self.mainwindow.all_colors)
            
            # determine the area of the visible screen
            visible_scene_rect = self.mapToScene(self.viewport().rect()).boundingRect()

            # determine where exactly your viewpoint is positioned
            x_cord_funct = random.uniform(visible_scene_rect.left(), visible_scene_rect.right() - 50)
            y_cord_funct = random.uniform(visible_scene_rect.top(), visible_scene_rect.bottom() - 50)

            # add this newly generated rect and make it moveable
            new_rect = self.mainwindow.scene.addRect(x_cord_funct, y_cord_funct, 50, 50, color_picked)
            new_rect.setFlag(QGraphicsItem.ItemIsMovable)

    