
# game idea: ability to cmd+t and add a block, then can stack the block
# once the blocks are stacked they are stuck. can ctrl+click on the block to
# delete it. can also implement the zoom feature
# maybe a block counter too?
# maybe the ability to press a button and then it just implements a tower
# or like a pyramid of block or like input random number and then
# it spits out that # of blocks on the screen 

# it would be fun to next highlight the area and be able to delete

# need to add a random color feature for the squares and maybe
# increase addn/delete feats

# maybe like a clear all feat or like an add 10 feat

from PySide6.QtWidgets import QWidget, QMainWindow, QGraphicsView, QGraphicsItem, QGraphicsScene, QToolBar, QPushButton, QMessageBox, QComboBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPen, QBrush, QColor
from customGraphicsView import CustomGraphicsView
from customGraphicsScene import CustomGraphicsScene
import random

class MainWindow(QMainWindow):
    # intalize function
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blocks")

        self.x_cord = 800
        self.y_cord = 600

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
        self.add_combo_box.setCurrentIndex(-1)
        self.add_combo_box.activated.connect(self.on_add_combo_activation)

        toolbar.addWidget(self.add_combo_box)




    def clicked_instructions(self):
        ret = QMessageBox.information(self, "Blocks Instructions", 
            "Press space to add square. Double click to delete square. " 
            "Zoom in/out with ctrl+mouse scroll (cmd+mouse scroll for macOS users).", 
            QMessageBox.Ok)

    def zoom_in(self):
        self.view.scale(1.125,1.125) # the () is a scaling factor (2 times x and 2 times y)

    def zoom_out(self):
        self.view.scale(0.875, 0.875)

    def on_add_combo_activation(self, index):
        # color_picked = random.choice(self.mainwindow.all_colors)
        # new_rect = self.mainwindow.scene.addRect(100, 100, 50, 50, color_picked)
        # # make it able to move
        # new_rect.setFlag(QGraphicsItem.ItemIsMovable)

        # converting the index to int count
        count = 3
        if index == 0: count = 5
        elif index == 1: count = 10
        elif index == 2: count = 20
        elif index == 3: count = 50
        else: count = 100

        # for every index, make a new rect same size 
        # but in a different location
        # index_num = index
        for i in range(count):
            color_picked = random.choice(self.all_colors)
            x_cord_funct = random.randint(0, self.x_cord)
            y_cord_funct = random.randint(0, self.y_cord)

            new_rect = self.scene.addRect(x_cord_funct, y_cord_funct, 50, 50, color_picked)
            new_rect.setFlag(QGraphicsItem.ItemIsMovable)
            
        