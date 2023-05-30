"""This controller contains all the functions to draw the 'binary
image'."""

from pathlib import Path

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


# get the algorithm
algorithm = get_file_contents("data/", "sample.txt")
