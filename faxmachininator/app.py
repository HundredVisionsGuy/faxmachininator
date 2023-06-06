import sys
from PyQt6 import (QtGui, QtWidgets)
from PyQt6.QtWidgets import (QLabel)
from PyQt6.QtGui import QPixmap, QColor
import controller

# make a tuple of colors so we can use indexing
colors = (
    "white", "black", "red", "darkRed", "green", 
    "darkGreen", "blue", "darkBlue", "cyan", "darkCyan", 
    "magenta", "darkMagenta", "yellow", "darkYellow", 
    "gray", "darkGray", "lightGray"
)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pixel_size = 50
        cols = 16
        rows = 16
        width = cols * self.pixel_size
        height = rows * self.pixel_size
        self.label = QLabel()
        canvas = QPixmap(width, height)
        canvas.fill(QColor(255, 255, 255))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_picture()

    def draw_picture(self, color="black"):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(40)
        controller.draw_picture(painter, pen, colors)

        # painter.drawPoint(225, 150)
        painter.end()
        self.label.setPixmap(canvas)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()