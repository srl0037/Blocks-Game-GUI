from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QMainWindow, QGraphicsItem
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

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
            print ("Space key is pressed")
            # add another square
            new_rect = self.mainwindow.scene.addRect(100, 100, 50, 50, self.mainwindow.green_pen)
            # make it able to move
            new_rect.setFlag(QGraphicsItem.ItemIsMovable)

        else:
            super().keyPressEvent(event)

    