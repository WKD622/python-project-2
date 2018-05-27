import sys

DEFAULT_HEIGHT = 500
DEFAULT_WIDTH = 500
DEFAULT_FG_COLOUR = 'black'
DEFAULT_BG_COLOUR = 'white'
SCREEN = "Screen"
PALETTE = "Palette"
WIDTH = "width"
HEIGHT = "height"
BG_COLOUR = "bg_color"
FG_COLOUR = "fg_color"
X = "x"
Y = "y"
FIGURES = "Figures"
TYPE = "type"
POINT = "point"
POLYGON = "polygon"
RECTANGLE = "rectangle"
SQUARE = "square"
CIRCLE = "circle"
RADIUS = "radius"
SIZE = "size"
COLOR = "color"
POINTS = "points"


def handle_error(message):
    """
    Prints message and exits program.
    :param message:
    :return:
    """
    print(message)
    sys.exit()
