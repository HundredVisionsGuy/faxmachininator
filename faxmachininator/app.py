import turtle
from pathlib import Path


def main():
    """selects a file from data folder and uses the algorithm to draw
    a pixel image."""

    # Initialize Turtle pen
    pen = turtle.Pen()
    print(pen.__str__)

    # get the algorithm
    algorithm = get_file_contents("data/", "sample.txt")

    # draw picture
    dimension = get_dimensions(algorithm)
    print(dimension)

def get_dimensions(algorithm: str) -> tuple:
    """Get the full algorithm text and return the width and height
    as a tuple"""

    return get_dimensions(algorithm)


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

if __name__ == "__main__":
    main()
