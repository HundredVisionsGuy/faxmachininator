import sys
from PyQt6 import (QtGui, QtWidgets)
from PyQt6.QtWidgets import (QLabel)
from PyQt6.QtGui import QPixmap, QColor

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

    def draw_picture(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(40)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.end()
        self.label.setPixmap(canvas)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()