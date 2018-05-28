from copy import deepcopy

import src.json.operations as o
import src.drawing.draw as d
import src.common as cm
import src.json.is_correct as cr

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
    draw = d.Draw()

    if path is None:
        path = 'json/example/json_example.txt'
    json.parse(path)
    cr.check_json(json.data)
    parse_screen_parameters(json.data, draw)
    draw_all_figures(json.data, draw)


def parse_screen_parameters(json, draw):
    """
    Parses screen parameters from given json and sets them. If they not exists
    this function sets them for default values which are in default_values module.
    :param draw:
    :param json:
    :return:
    """
    global fg_colour, bg_colour, screen_width, screen_height

    if json.get('Screen') is not None:
        value = json.get(cm.SCREEN).get(cm.WIDTH)
        if value is not None:
            screen_width = value
        else:
            screen_width = cm.DEFAULT_WIDTH

        value = json.get(cm.SCREEN).get(cm.HEIGHT)
        if value is not None:
            screen_height = value
        else:
            screen_height = cm.DEFAULT_HEIGHT

        value = json.get(cm.SCREEN).get(cm.BG_COLOUR)
        if value is not None:
            value_copy = deepcopy(value)
            if json.get(cm.PALETTE) is not None:
                value = json.get(cm.PALETTE).get(value)
                if value is None:
                    bg_colour = value_copy
                else:
                    bg_colour = value
            else:
                bg_colour = value_copy
        else:
            bg_colour = cm.DEFAULT_BG_COLOUR

        value = json.get(cm.SCREEN).get(cm.FG_COLOUR)
        if value is not None:
            value_copy = deepcopy(value)
            if json.get(cm.PALETTE) is not None:
                value = json.get(cm.PALETTE).get(value)
                if value is None:
                    fg_colour = value_copy
                else:
                    fg_colour = value
            else:
                fg_colour = value_copy
        else:
            fg_colour = cm.DEFAULT_FG_COLOUR
    else:
        screen_width = cm.DEFAULT_WIDTH
        screen_height = cm.DEFAULT_HEIGHT
        bg_colour = cm.DEFAULT_BG_COLOUR
        fg_colour = cm.DEFAULT_FG_COLOUR
    draw.preparation(screen_width, screen_height, bg_colour)


def take_colour_from_palette(palette, colour):
    """
    This method takes json and given colour name and finds it in palette.
    :param palette:
    :param colour:
    :return: colour
    """
    return palette.get(colour.strip())


def draw_figure(figure, palette, draw):
    """
    Takes figure to draw, palette of colours and class Draw to draw given figure.
    :param figure:
    :param palette:
    :param draw:
    :return:
    """
    global fg_colour
    figure_type = figure.get(cm.TYPE)
    colour = figure.get(cm.COLOR)
    colour_copy = deepcopy(colour)
    if colour is None:
        colour = fg_colour
    else:
        if palette is not None:
            colour = take_colour_from_palette(palette, colour)
            if colour is None:
                colour = colour_copy
        else:
            colour = colour_copy

    if figure_type == cm.POINT:
        draw.point(figure.get(cm.X), figure.get(cm.Y), colour.strip())
    elif figure_type == cm.POLYGON:
        draw.polygon(figure.get(cm.POINTS), colour.strip())
    elif figure_type == cm.RECTANGLE:
        draw.rectangle(figure.get(cm.X), figure.get(cm.Y), figure.get(cm.WIDTH), figure.get(cm.HEIGHT), colour.strip())
    elif figure_type == cm.SQUARE:
        draw.square(figure.get(cm.X), figure.get(cm.Y), figure.get(cm.SIZE), colour.strip())
    elif figure_type == cm.CIRCLE:
        draw.circle(figure.get(cm.X), figure.get(cm.Y), figure.get(cm.RADIUS), colour.strip())


def draw_all_figures(json, draw):
    """
    Draws all figures from json.
    :param draw:
    :param json:
    :return:
    """
    global fg_colour
    figures = json.get(cm.FIGURES)
    for figure in figures:
        draw_figure(figure, json.get(cm.PALETTE), draw)
    draw.end()