# activate virtual enviroment: source coloring_venv/bin/activate

import sys
from PySide6.QtWidgets import QApplication, QWidget
from mainwindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

