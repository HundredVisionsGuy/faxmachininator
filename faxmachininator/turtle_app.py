import turtle
import file_clerk.clerk as clerk
from pathlib import Path


def main():
    """selects a file from data folder and uses the algorithm to draw
    a pixel image."""

    # Initialize Turtle pen
    pen = turtle.Pen()
    pen.speed(0)

    # Set screen size and location to be in middle monitor
    # Comment out the lines below if you are not using a dual monitor.
    screen = turtle.Screen()
    screen.setup(800, 800, 2200, 100)

    draw_again = "y"
    while draw_again == "y":
        screen.clear()
        # get the algorithm
        file = choose_file()
        algorithm = clerk.file_to_string(file)

        # get setup data
        dimensions, name, width, pixel_width = get_setup_data(pen, algorithm)
        algorithm = clean_algorithm(algorithm)
        start_x, start_y = goto_start(pen, dimensions, pixel_width)
        draw_picture(pen, pixel_width, algorithm, start_x, width)
        show_credits(pen, name, width, pixel_width, start_x, start_y)
        draw_again = input("What to draw again? (y/n) ").lower().strip()[0]


def get_setup_data(pen, algorithm):
    dimensions = get_dimensions(algorithm)
    name = dimensions[2]
    width = dimensions[0]
    dimensions = dimensions[:2]
    pixel_width = get_pixel_width(dimensions, pen)
    return (dimensions, name, width, pixel_width)


def show_credits(pen, name, width, pixel_width, start_x, start_y):
    pen.up()
    pen.goto(start_x + pixel_width*width + pixel_width, start_y - 100)
    pen.down()
    msg = f"Created by:\n{name}"
    pen.write(msg, font=("Calibri", 14, "bold"))


def choose_file() -> str:
    """returns a folder and file name

    Opens up the folder and displays a list of all files and then
    has the user select which file to run (by number)

    Returns:
        file_data: a tuple containing the folder and the file
    """
    folder = "data/black_and_white/"
    file = ""
    files = clerk.get_all_files_of_type(folder, "txt")
    selection = None
    print("\nHere is a list of files:\n")
    while selection not in range(len(files)):
        for i in range(len(files)):
            print(str(i) + " - " + files[i])
        selection = input("\nChoose a file by its number: ")
        try:
            selection = int(selection)
        except TypeError:
            print("That is not an option.")
    file = files[selection]
    return file


def get_dimensions(contents: str) -> tuple:
    """Get the full algorithm text and return the width and height
    as a tuple

    To get the height, we just need the number of rows. To get the
    width, we will get the maximum width (the row with the highest
    number). That's because the algorithm doesn't specify the 'run'
    of white pixels at the end of a row (nothing to draw).

    Args:
        algorithm: this is a list of numbers, where the first number
            represents the "run" of white pixels, and every other number
            is alternating between runs of black and white respectively.

    Returns:
        dimensions: a tuple of integers (columns and rows)
    """

    width = 0
    max_width = 16
    algorithm = contents.split("\n")
    height = 0
    student_name = ""

    # loop through the rows to get the width
    for row in algorithm:
        if "Student:" in row or "Name:" in row:
            row_split = row.split(":")
            student_name = row_split[1].strip()
            continue
        if "Algorithm" in row:
            continue
        if not row:
            continue
        # split row into numbers
        numbers = row.strip().split(",")

        width = 0
        if numbers[0]:
            height += 1
            for num in numbers:
                width += int(num)

        # assume it's 16 pixels wide unless a particular row is wider
        if width > max_width:
            max_width = width

    return (max_width, height, student_name)


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


def get_pixel_width(dim: tuple, pen) -> int:
    """Returns the recommended width for each pixel in the
    drawing based on dimensions and screen width

    Args:
        dim: width and height of image.

        pen: turtle graphics pen from which we get the overall
            screen width and height.

    Returns:
        the width of the pixel size."""

    screen_width = pen.screen.canvheight
    screen_height = pen.screen.canvwidth
    x, y = dim
    width = int(screen_width / x)
    height = int(screen_height / y)
    if width > height:
        return height
    return height


def goto_start(pen, dim: tuple, pixel_width: int) -> None:
    """Put the pen at the upper-left region of the screen"""
    w, h = dim
    left = -w * pixel_width
    top = h * pixel_width
    pen.up()
    pen.goto(left, top)
    pen.down()
    return (left, top)


def draw_picture(pen, pixel_width: int, algorithm: list, left: int,
                 cols: int) -> None:
    """draw the picture using the algorithm

    Args:
        pen: this is the turtle graphic pen
        pixel_width: the length of the side of a pixel
        algorithm: a list of rows of pixel runs
        left: the left-side x position
        cols: the number of pixels per row
    """

    # a color of 0 is white (clear) 1 is black
    colors = ("white", "black")
    color_index = 0
    for row in algorithm:
        color_index = 0
        runs = row.strip().split(",")
        count = 0
        for run in runs:
            run = int(run)
            # 1st pixel is always white
            color = colors[color_index]
            pen.fillcolor(color)
            for pixels in range(run):
                count += 1
                pen.begin_fill()
                draw_pixel(pen, pixel_width)
                pen.end_fill()
                pen.up()
                pen.fd(pixel_width)
                pen.down()
            color_index += 1
            color_index %= 2
        remaining = cols - count
        color = "white"
        pen.fillcolor(color)
        for pixels in range(remaining):
            pen.begin_fill()
            draw_pixel(pen, pixel_width)
            pen.end_fill()
            pen.up()
            pen.fd(pixel_width)
            pen.down()

        goto_next_row(pen, pixel_width, left)


def clean_algorithm(algorithm):
    algorithm = algorithm.split("\n")
    cleaned_algorithm = []
    for row in algorithm:
        if "Name" in row or "Algorithm" in row or "Student" in row:
            continue
        if not row:
            continue
        cleaned_algorithm.append(row)
    algorithm = cleaned_algorithm
    return algorithm


def draw_pixel(pen, width: int) -> None:
    """draw a box with sides of length width

    Args:
        pen: A turtle graphics pen
        width: length of pixel side
    """
    for i in range(4):
        pen.fd(width)
        pen.right(90)


def goto_next_row(pen, width: int, left: int) -> None:
    """ Return to the left hand side and move down by pixel width"""
    pen.up()
    pen.setx(left)
    pen.right(90)
    pen.fd(width)
    pen.left(90)
    pen.down()


if __name__ == "__main__":
    main()
