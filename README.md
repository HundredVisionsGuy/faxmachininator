# faxmachininator
A Python program to test fax machine algorithm from csunplugged's [Image Representation](https://www.csunplugged.org/en/topics/image-representation/) activity.

The program takes input in the form of a text file and uses the coded algorithm to draw the design.
## Installation
1. Clone or fork this project `git clone https://github.com/HundredVisionsGuy/faxmachininator.git`.
2. Download `poetry` from [python-poetry.org](https://python-poetry.org/docs/)
3. Make sure you have VSCode downloaded (or use your favorite text editor)
4. Open `generator.code-workspace`
5. Install the Python extension for Visual Studio Code.
6. In the terminal, type:
    * `poetry install`
    * `poetry shell`
7. Open Command Palette by either...
    * `CTRL` + `Shift` + `P`
    OR
    * View > Command Palette
8. From Command palette, 
    * choose Python: Select Interpreter
    * Look for an interpreter path with `Poetry` (in blue) on the far right.
    * Select that path.
    * If you don't see it, click the little refresh icon at the top (to the right of "Select Interpreter")
9. Place your image code as text files in the appropriate folder:
    * ***Using the Black and White Algorithm?*** put it in the `data/black_and_white` folder (use `bw_image_template.txt` as a guide)
    * ***Using the Color Algorithm?*** put it in the `data/color_projects` folder (use `color_image_template.txt` as a guide)

## Usage
1. Write the algorithm in a text file where each line is a row of pixels
2. Store the file in the `data` folder (`data/filename.txt`).
3. Run main: `python main.py`
