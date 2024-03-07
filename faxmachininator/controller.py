"""This controller contains all the functions to draw the 'binary
image'."""

from pathlib import Path
from PyQt6 import QtGui


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


def draw_picture(painter, pen, colors):
    x = 40
    y = 50
    author = ""
    for row in algorithm:
        if "name" in row.lower():
            if ":" in row:
                author = row.split(":")[1]
            else:
                author = row.strip()
        if not row.strip() or "(" not in row:
            continue
        row = row.replace("),", ") ")
        runs = row.strip().split(")")
        for run in runs:
            if run:
                pixels, color = run.split(",")
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


# get the algorithm
algorithm = get_file_contents("data/", "MarkL_color_image.txt")
