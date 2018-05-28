import src.common as cm
import src.drawing.colours as cl

json = None


def prepare_for_checking(json_, figures):
    """
    Prepares for checking. Checks if figures list is empty or exists.
    :param figures:
    :param json_:
    :return:
    """
    global json
    json = json_
    if figures is None:
        cm.handle_error("There is no figures list.")
    elif len(figures) == 0:
        cm.handle_error("Figures list is empty. Nothing to draw. :-(")


def check_if_screen_correct(screen):
    """
    Checks if whole screen is correct written in json.
    :param screen:
    :return:
    """
    if screen is not None:
        check_if_colour_correct(screen.get(cm.FG_COLOUR))
        check_if_colour_correct(screen.get(cm.BG_COLOUR))


def check_if_colour_correct(colour):
    """
    Checks if colour is correct (even if it is from palette).
    :param colour:
    :return:
    """
    global json
    if colour is not None:
        if cl.is_dec(colour.strip()) or cl.is_hex(colour.strip()):
            return True
        else:
            if json.get(cm.PALETTE) is not None:
                value = json.get(cm.PALETTE).get(colour)
                if value is not None:
                    if cl.is_dec(value) or cl.is_hex(value):
                        return True
                    else:
                        cm.handle_error("Color {}: {} in palette has incorrect value.".format(colour, value))
                else:
                    if colour not in cm.BASIC_COLOURS:
                        cm.handle_error("Colour `{}` is incorrect. Add it to palette or correct it.".format(colour))
            elif colour not in cm.BASIC_COLOURS:
                cm.handle_error("Colour `{}` is incorrect. Add it to palette or correct it.".format(colour))
    return True


def check_if_fields_exists(figure, list_of_fields):
    """
    Takes list of fields which should be in json for choosen figure and checks if they are.
    :param figure:
    :param list_of_fields:
    :return:
    """
    for field in list_of_fields:
        if figure.get(field) is None:
            cm.handle_error(
                "There is lack of {} in figure {} or there can be spelling mistake.".format(field, figure.get(cm.TYPE)))


def check_if_coordinate_correct(coordinate):
    """
    Checks if coordinate (for example [a,b]) is correct. If a and b are ints and length of it is 2.
    :param coordinate:
    :return:
    """
    if len(coordinate) == 2:
        check_if_int(coordinate[0], "Incorrect one of coordinates from list")
        check_if_int(coordinate[1], "Incorrect one of coordinates from list")
    else:
        cm.handle_error("Incorrect length of one of coordinates")


def check_if_list_of_coordinates_correct(list_of_coordinates):
    """
    Checks if list of coordinates is correct.
    :param list_of_coordinates:
    :return:
    """
    for coordinate in list_of_coordinates:
        check_if_coordinate_correct(coordinate)
    return True


def check_if_int(to_check, message):
    """
    Checks if to_check is int, if not writes message and ends program.
    :param to_check:
    :param message:
    :return:
    """
    if to_check is not None:
        if not isinstance(to_check, int):
            cm.handle_error(message)
    return True


def check_if_point_correct(point):
    """
    Checks if point from json has everything correct.
    :param point:
    :return:
    """
    check_if_colour_correct(point.get(cm.COLOR))
    check_if_fields_exists(point, [cm.X, cm.Y])
    if check_if_int(point.get(cm.X), "Incorrect field x of figure point. Type may be wrong.") and \
            check_if_int(point.get(cm.Y), "Incorrect field x of figure point. Type may be wrong."):
        return True


def check_if_polygon_correct(polygon):
    """
    Checks if polygon from json has everything correct.
    :param polygon:
    :return:
    """
    check_if_fields_exists(polygon, [cm.POINTS])
    points = polygon.get(cm.POINTS)
    if len(points) >= 3:
        check_if_list_of_coordinates_correct(points)
        check_if_colour_correct(polygon.get(cm.COLOR))
    else:
        cm.handle_error("Polygon has to have 3 or more points to be created.")
    return True


def check_if_rectangle_correct(rectangle):
    """
    Checks if rectangle from json has everything correct. If not ends program and writes message.
    :param rectangle:
    :return:
    """
    check_if_fields_exists(rectangle, [cm.X, cm.Y, cm.WIDTH, cm.HEIGHT])
    if check_if_int(rectangle.get(cm.X), "Incorrect field x of figure rectangle. Type may be wrong.") and \
            check_if_int(rectangle.get(cm.Y), "Incorrect field y of figure rectangle. Type may be wrong.") and \
            check_if_int(rectangle.get(cm.WIDTH), "Incorrect field width of figure rectangle. Type may be wrong.") and \
            check_if_int(rectangle.get(cm.HEIGHT), "Incorrect field height of figure rectangle. Type may be wrong.") and \
            check_if_colour_correct(rectangle.get(cm.COLOR)):
        return True


def check_if_square_correct(square):
    """
    Checks if square from json has everything correct. If not ends program and writes message.
    :param square:
    :return:
    """
    check_if_fields_exists(square, [cm.X, cm.Y, cm.SIZE])
    if check_if_int(square.get(cm.X), "Incorrect field x of figure square. Type may be wrong.") and \
            check_if_int(square.get(cm.Y), "Incorrect field y of figure square. Type may be wrong.") and \
            check_if_int(square.get(cm.SIZE), "Incorrect field size of figure square. Type may be wrong.") and \
            check_if_colour_correct(square.get(cm.COLOR)):
        return True


def check_if_circle_correct(circle):
    """
    Checks if circle from json has everything correct. If not ends program and writes message.
    :param circle:
    :return:
    """
    check_if_fields_exists(circle, [cm.X, cm.Y, cm.RADIUS])
    if check_if_int(circle.get(cm.X), "Incorrect field x of figure circle. Type may be wrong.") and \
            check_if_int(circle.get(cm.Y), "Incorrect field y of figure circle. Type may be wrong.") and \
            check_if_int(circle.get(cm.RADIUS), "Incorrect field radius of figure circle. Type may be wrong.") and \
            check_if_colour_correct(circle.get(cm.COLOR)):
        return True


def check_if_figure_correct(figure):
    """
    Checks if given figure from json has everything correct. If not ends program and writes message.
    :param figure:
    :return:
    """
    figure_type = figure.get(cm.TYPE)
    if figure_type == cm.POINT:
        check_if_point_correct(figure)
    elif figure_type == cm.POLYGON:
        check_if_polygon_correct(figure)
    elif figure_type == cm.RECTANGLE:
        check_if_rectangle_correct(figure)
    elif figure_type == cm.SQUARE:
        check_if_square_correct(figure)
    elif figure_type == cm.CIRCLE:
        check_if_circle_correct(figure)
    else:
        cm.handle_error("`{}` figure name is incorrect.".format(figure_type))


def check_if_figures_correct(json):
    """
    Checks every figure from given figures list if it is correct.
    :param json:
    :return:
    """
    figures = json.get(cm.FIGURES)
    prepare_for_checking(json, figures)
    for figure in figures:
        check_if_figure_correct(figure)


def check_json(json):
    """
    Main in is_correct module.
    :param json:
    :return:
    """
    check_if_figures_correct(json)
    check_if_screen_correct(json.get(cm.SCREEN))
    print("Check ends successfully. Json is correct.")
