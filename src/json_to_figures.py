import src.json.operations as o
import src.drawing.draw as d
import src.common as c
import src.json.is_correct as ch

fg_colour = None
bg_colour = None
screen_width = None
screen_height = None


def json_to_figures(path):
    """
    Takes a path to json and draws all figures. This is main function in whole program.
    :param path:
    :return:
    """
    json = o.JsonOperations()

    if path is None:
        path = 'json/example/json_example.txt'
    json.parse(path)
    ch.check_if_figures_correct(json.data.get(c.FIGURES))
    # parse_screen_parameters(json.data)
    # draw_all_figures(json.data)


def parse_screen_parameters(json):
    """
    Parses screen parameters from given json and sets them. If they not exists
    this function sets them for default values which are in default_values module.
    :param json:
    :return:
    """
    global fg_colour, bg_colour, screen_width, screen_height

    if json.get('Screen') is not None:
        value = json.get(c.SCREEN).get(c.WIDTH)
        if value is not None:
            screen_width = value
        else:
            screen_width = c.DEFAULT_WIDTH

        value = json.get(c.SCREEN).get(c.HEIGHT)
        if value is not None:
            screen_height = value
        else:
            screen_height = c.DEFAULT_HEIGHT

        value = json.get(c.SCREEN).get(c.BG_COLOUR)
        if value is not None:
            bg_colour = value
        else:
            bg_colour = c.DEFAULT_BG_COLOUR

        value = json.get(c.SCREEN).get(c.WIDTH)
        if value is not None:
            fg_colour = value
        else:
            fg_colour = c.DEFAULT_FG_COLOUR
    else:
        screen_width = c.DEFAULT_WIDTH
        screen_height = c.DEFAULT_HEIGHT
        bg_colour = c.DEFAULT_BG_COLOUR
        fg_colour = c.DEFAULT_FG_COLOUR


def take_colour_from_palette(json, colour):
    """
    This method takes json and given colour name and finds it in Palette.
    :param colour:
    :param json:
    :return: colour
    """
    return json.get(c.PALETTE).get(colour)


def draw_all_figures(json):
    """
    Draws all figures from json.
    :param json:
    :return:
    """
    global fg_colour
    Draw = d.Draw()
    figures = json.get(c.FIGURES)
    if figures is not None:
        print(c.FIGURES)

    else:
        c.handle_error("There are no figures to draw! Add some :-).")


json_to_figures(None)
