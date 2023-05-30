import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen, QFont, QPixmap
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(QColor(255, 255, 255))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(40)
        pen.setColor(QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()