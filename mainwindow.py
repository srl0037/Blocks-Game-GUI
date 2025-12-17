
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

from PySide6.QtWidgets import QWidget, QMainWindow, QGraphicsView, QGraphicsItem, QGraphicsScene, QToolBar, QPushButton, QMessageBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPen, QBrush, QColor
from customGraphicsView import CustomGraphicsView
from customGraphicsScene import CustomGraphicsScene

class MainWindow(QMainWindow):
    # intalize function
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blocks")

        self.setFixedSize(QSize(800, 600))
    

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


        # adding a dock widget to house instructions?

        # dock = QDockWidget()
        # self.addDockWidget(dock)

        # making a button to add a message box
        instructions_message = QPushButton("Instructions")
        instructions_message.clicked.connect(self.clicked_instructions)

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.addWidget(instructions_message)


    def clicked_instructions(self):
        ret = QMessageBox.information(self, "Blocks Instructions", 
            "Press space to add square. Double click to delete square. " 
            "Zoom in/out with ctrl+mouse scroll (cmd+mouse scroll for macOS users).", 
            QMessageBox.Ok)

    def zoom_in(self):
        self.view.scale(1.125,1.125) # the () is a scaling factor (2 times x and 2 times y)

    def zoom_out(self):
        self.view.scale(0.875, 0.875)