"""This controller contains all the functions to draw the 'binary
image'."""

import file_clerk.clerk as clerk
from pathlib import Path
from PyQt6 import QtGui
from PyQt6.QtWidgets import QComboBox


def get_color_project() -> QComboBox:
    combo_box = QComboBox()
    files = clerk.get_all_files_of_type("data/color_projects/", "txt")
    bw_files = clerk.get_all_files_of_type("data/black_and_white", "txt")
    combo_box.addItems(files)
    combo_box.addItems(bw_files)
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
    if "black_and_white" in full_path:
        algorithm = get_file_contents("data/black_and_white/", filename)
        algorithm = convert_to_color(algorithm)
    else:
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
            if "color" not in directory:
                # Gotta convert black and white to color
                if "," in row:
                    pixel_run = row.split(",")
                    cur_color = 0
                    # alternate between white and black 0 and 1
                    row = ""
                    for i in pixel_run:
                        row += f"({i},{cur_color})"
                        cur_color += 1
                        cur_color = cur_color % 2
                else:
                    continue
            else:
                continue
        row = row.replace("),", ") ")
        row = row.replace(")  (", ") (")
        runs = row.strip().split(")")
        print(runs)
        for run in runs:
            if run:
                try:
                    pixels, color = run.split(",")
                except ValueError:
                    print(run)
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
    print("="*15)
    return author


def convert_to_color(algorithm: list) -> list:
    new_algo = []

    for row in algorithm:
        color = 0
        new_row = []
        if ("name" in row.lower() or "algorithm" in row.lower() or
                "student" in row.lower()):
            new_algo.append(row)
            continue
        else:
            runs = row.split(",")
            for run in runs:
                pixels = f"({run.strip()}, {color},)"
                new_row.append(pixels)
                color += 1
                color %= 2
            new_row = str(new_row)
            new_row = new_row.replace("'", "")
            new_row = new_row.replace("[", "")
            new_row = new_row.replace("]", "")
            new_row = new_row.replace(",)", ")")
            new_algo.append(new_row)
    return new_algo


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
