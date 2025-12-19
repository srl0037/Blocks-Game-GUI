from PySide6.QtWidgets import QWidget, QMainWindow, QGraphicsView, QGraphicsItem, QGraphicsScene, QToolBar, QPushButton, QMessageBox, QComboBox, QGraphicsRectItem
from PySide6.QtCore import QSize, Qt, QPointF, QRectF
from PySide6.QtGui import QPen, QBrush, QColor
from customGraphicsView import CustomGraphicsView
from customGraphicsScene import CustomGraphicsScene
import random

class MainWindow(QMainWindow):
    # intalize function
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blocks")

        self.x_cord = 800 # width
        self.y_cord = 600 # height

        self.max_point = (self.x_cord, self.y_cord)

        self.setFixedSize(QSize(self.x_cord, self.y_cord))
    

        # create QGraphic Scene and View
        self.scene = CustomGraphicsScene(self)
        self.view = CustomGraphicsView(self, self.scene)

        # add view to main window
        self.setCentralWidget(self.view)

        # add some pens
        self.pink_pen = QPen(QColor(255, 0, 243))
        self.orange_pen = QPen(QColor(255, 165, 0)) 
        self.yellow_pen = QPen(Qt.yellow)
        self.green_pen = QPen(Qt.green)
        self.blue_pen = QPen(QColor(0, 203, 255))
        self.purple_pen = QPen(QColor(171, 0, 255))
        
        # set pen width
        self.pink_pen.setWidth(6)
        self.orange_pen.setWidth(6)
        self.yellow_pen.setWidth(6)
        self.green_pen.setWidth(6)
        self.blue_pen.setWidth(6)
        self.purple_pen.setWidth(6)

        # in case i want to have brush
        green_brush = QBrush(Qt.green)

        # make a list of the colors
        self.all_colors = [self.pink_pen, self.orange_pen, self.yellow_pen, self.green_pen,
            self.blue_pen, self.purple_pen]

        # add a rect
        rect1 = self.scene.addRect(50, 50, 50, 50, self.green_pen)

        # make rect group and add the rect
        rect_group = self.scene
        
        # make moveable
        rect1.setFlag(QGraphicsItem.ItemIsMovable)
        rect1.setFlag(QGraphicsItem.ItemIsSelectable)

        # making a toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # making a button to add a message box
        instructions_message = QPushButton("Instructions")
        instructions_message.clicked.connect(self.clicked_instructions)
        # adding button to toolbar
        toolbar.addWidget(instructions_message)

        # making an "add x number of blocks button"
        self.add_combo_box = QComboBox()
        self.add_combo_box.setPlaceholderText("Add Lots of Squares")
        self.add_combo_box.addItem("5 squares", userData=5)
        self.add_combo_box.addItem("10 squares", userData=10)
        self.add_combo_box.addItem("20 squares", userData=20)
        self.add_combo_box.addItem("50 squares", userData=50)
        self.add_combo_box.addItem("100 squares", userData=100)
        self.add_combo_box.addItem("1000 squares", userData=1000)
        self.add_combo_box.setCurrentIndex(-1)
        self.add_combo_box.activated.connect(self.view.on_add_combo_activation)

        toolbar.addWidget(self.add_combo_box)

        # making a clear all squares button
        # self.remove_combo_box = QComboBox()
        remove_button = QPushButton("Clear All Squares")
        remove_button.clicked.connect(self.scene.clear_all_squares)
        toolbar.addWidget(remove_button)

        remove_half_button = QPushButton("Clear Half of Squares")
        remove_half_button.clicked.connect(self.scene.clear_half_squares)
        toolbar.addWidget(remove_half_button)


    def clicked_instructions(self):
        ret = QMessageBox.information(self, "Blocks Instructions", 
            "Press space to add square. Double click to delete square. " 
            "Zoom in/out with ctrl+mouse scroll (cmd+mouse scroll for macOS users). "
            "Drag mouse to delete multiple specific blocks.", 
            QMessageBox.Ok)

  
