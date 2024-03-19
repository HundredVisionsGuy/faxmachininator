import sys
import file_clerk.clerk as clerk
from PyQt6 import (QtGui, QtWidgets)
from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QComboBox)
from PyQt6.QtGui import QPixmap, QColor
import controller


# make a tuple of colors so we can use indexing
colors = (
    "white", "black", "red", "darkRed", "green",
    "darkGreen", "blue", "darkBlue", "cyan", "darkCyan",
    "magenta", "darkMagenta", "yellow", "darkYellow",
    "gray", "darkGray", "lightGray", "#4782c9", "beige",
    "bisque", "chocolate", "#944E63", "#bdc0c9", "#435B66",
    "#A76F6F", "CornflowerBlue", "SandyBrown", "LightPink",
    "PaleVioletRed"
)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pixel_size = 45
        cols = 23
        rows = 30
        width = cols * self.pixel_size
        height = rows * self.pixel_size
        main_layout = QVBoxLayout()

        self.author_label = QLabel()
        self.author_label.setStyleSheet("font-size: 20px;")
        self.label = QLabel()

        canvas = QPixmap(width, height)
        canvas.fill(QColor(255, 255, 255))
        self.label.setPixmap(canvas)

        self.projects_combo = QComboBox
        self.projects_combo = controller.get_color_project()
        self.file_stuff = self.projects_combo.currentText

        main_layout.addWidget(self.projects_combo)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.author_label)
        self.projects_combo.currentTextChanged.connect(self.filename_changed)

        # Set main layout
        self.gui = QWidget()
        self.gui.setAutoFillBackground(True)
        self.gui.setLayout(main_layout)
        self.setCentralWidget(self.gui)

        self.draw_picture()

    def filename_changed(self, s):
        self.draw_picture(s)

    def draw_picture(self, file_path="", color="black"):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(40)
        if not file_path:
            file_path = clerk.get_all_files_of_type("data/color_projects/",
                                                    "txt")[0]
        controller.clear_screen(painter, pen, colors)
        author = controller.draw_picture(file_path, painter, pen,
                                         colors)
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
