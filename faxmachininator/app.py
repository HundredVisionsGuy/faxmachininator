import sys
from PyQt6 import (QtGui, QtWidgets)
from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout)
from PyQt6.QtGui import QPixmap, QColor
import controller

# make a tuple of colors so we can use indexing
colors = (
    "white", "black", "red", "darkRed", "green",
    "darkGreen", "blue", "darkBlue", "cyan", "darkCyan",
    "magenta", "darkMagenta", "yellow", "darkYellow",
    "gray", "darkGray", "lightGray", "#4782c9", "beige"
)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pixel_size = 45
        cols = 16
        rows = 16
        width = cols * self.pixel_size
        height = rows * self.pixel_size
        main_layout = QVBoxLayout()
        self.author_label = QLabel()
        self.author_label.setStyleSheet("font-size: 20px;")
        self.label = QLabel()
        canvas = QPixmap(width, height)
        canvas.fill(QColor(255, 255, 255))
        self.label.setPixmap(canvas)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.author_label)
        self.draw_picture()

        # Set main layout
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)

    def draw_picture(self, color="black"):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(40)
        author = controller.draw_picture(painter, pen, colors)
        # painter.drawPoint(225, 150)
        painter.end()
        self.label.setPixmap(canvas)
        credits = f"Image created by <b>{author.strip()}</b>"
        self.author_label.setText(credits)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
