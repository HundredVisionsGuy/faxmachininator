"""This controller contains all the functions to draw the 'binary
image'."""

import file_clerk.clerk as clerk
from pathlib import Path
from PyQt6 import QtGui
from PyQt6.QtWidgets import QComboBox


def get_color_project() -> QComboBox:
    combo_box = QComboBox()
    files = clerk.get_all_files_of_type("data/color_projects/", "txt")
    combo_box.addItems(files)
    return combo_box


def get_file_contents(path: str, filename: str) -> list:
    """Returns the contents of the file in the path.

    Args:
        path: the relative folder path should end with a forward slash
        filename: the name of the file with extension

    Returns:
        contents: a string of the file contents"""

    folder = Path(path)
    file_to_open = folder / filename
    f = open(file_to_open, 'r')
    rows = f.readlines()
    f.close()
    return rows


def draw_picture(full_path: str, painter: QtGui.QPainter, pen: QtGui.QPen,
                 colors: tuple) -> None:
    # get the algorithm
    filename = clerk.get_file_name(full_path)
    algorithm = get_file_contents("data/color_projects/", filename)
    x = 40
    y = 50
    author = ""
    for row in algorithm:
        row = row.strip()
        if "name" in row.lower():
            if ":" in row:
                author = row.split(":")[1]
            else:
                author = row.strip()
            continue
        if not row.strip() or "(" not in row:
            continue
        row = row.replace("),", ") ")
        runs = row.strip().split(")")
        for run in runs:
            if run:
                pixels, color = run.split(",")
                pixels = pixels.strip()
                color = color.strip()
                start = pixels.index("(")
                pixels = int(pixels[start+1:])
                color = int(color)
                pen.setColor(QtGui.QColor(colors[color]))
                painter.setPen(pen)
                for pix in range(pixels):
                    x += 40
                    painter.drawPoint(x, y)
        y += 40
        x = 40
    return author


def clear_screen(painter: QtGui.QPainter, pen: QtGui.QPen,
                 colors: tuple) -> None:
    x = 40
    y = 50
    width = 26
    for row in range(width):
        pixels, color = (width, 0)
        color = int(color)
        pen.setColor(QtGui.QColor(colors[color]))
        painter.setPen(pen)
        for pix in range(pixels):
            x += 40
            painter.drawPoint(x, y)
        y += 40
        x = 40
