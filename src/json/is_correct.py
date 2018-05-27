import src.common as v
import src.drawing.colours as c


def check_if_colour_correct(colour, json):
    """
    Checks if colour is correct (even if it is from palette).
    :param colour:
    :param json:
    :return:
    """
    if c.is_dec(colour) or c.is_hex(colour):
        return True
    else:
        if json.get(v.PALETTE) is not None:
            value = json.get(v.PALETTE).get(colour)
            if value is not None:
                if c.is_dec(value) or c.is_hex(value):
                    return True
        else:
            v.handle_error("There is no palette.")


def check_if_fields_exists(figure, list_of_fields):
    """
    Takes list of fields which should be in json for choosen figure and checks if they are.
    :param figure:
    :param list_of_fields:
    :return:
    """
    for field in list_of_fields:
        if figure.get(field) is None:
            v.handle_error(
                "There is lack of {} in figure {} or there can be spelling mistake.".format(field, figure.get(v.TYPE)))


def check_if_coordinate_correct(coordinate):
    """
    Checks if coordinate (for example [a,b]) is correct. If a and b are ints and length of it is 2
    :param coordinate:
    :return:
    """
    if len(coordinate) == 2:
        check_if_int(coordinate[0], "Incorrect one of coordinates from list")
        check_if_int(coordinate[1], "Incorrect one of coordinates from list")
    else:
        v.handle_error("Incorrect length of one of coordinates")


def check_if_list_of_coordinates_correct(list_of_coordinates):
    """
    Checks if list of coordinates is correct
    :param list_of_coordinates:
    :return:
    """
    for coordinate in list_of_coordinates:
        check_if_coordinate_correct(coordinate)
    return True


def check_if_int(to_check, message):
    """
    Checks if to_check is int, if not writes message and ends program
    :param to_check:
    :param message:
    :return:
    """
    if to_check is not None:
        if not isinstance(to_check, int):
            v.handle_error(message)
    return True


def check_if_point_correct(point):
    """
    Checks if point from json has everything correct.
    :param point:
    :return:
    """
    check_if_fields_exists(point, [v.X, v.Y])
    if check_if_int(point.get(v.X), "Incorrect field x of figure point.") and \
            check_if_int(point.get(v.Y), "Incorrect field x of figure point."):
        return True


def check_if_polygon_correct(polygon):
    """
    Checks if polygon from json has everything correct.
    :param polygon:
    :return:
    """
    check_if_fields_exists(polygon, [v.POINTS])
    points = polygon.get(v.POINTS)
    if len(points) >= 3:
        check_if_list_of_coordinates_correct(points)
    else:
        v.handle_error("Polygon has to have 3 or more points to be created.")
    return True


def check_if_rectangle_correct(rectangle):
    """
    Checks if rectangle from json has everything correct. If not ends program and writes message.
    :param rectangle:
    :return:
    """
    check_if_fields_exists(rectangle, [v.X, v.Y, v.WIDTH, v.HEIGHT])
    if check_if_int(rectangle.get(v.X), "Incorrect field x of figure rectangle.") and \
            check_if_int(rectangle.get(v.Y), "Incorrect field y of figure rectangle.") and \
            check_if_int(rectangle.get(v.WIDTH), "Incorrect field width of figure rectangle") and \
            check_if_int(rectangle.get(v.HEIGHT), "Incorrect field height of figure rectangle"):
        return True


def check_if_square_correct(square):
    """
    Checks if square from json has everything correct. If not ends program and writes message.
    :param square:
    :return:
    """
    check_if_fields_exists(square, [v.X, v.Y, v.SIZE])
    if check_if_int(square.get(v.X), "Incorrect field x of figure square.") and \
            check_if_int(square.get(v.Y), "Incorrect field y of figure square.") and \
            check_if_int(square.get(v.SIZE), "Incorrect field size of figure square."):
        return True


def check_if_circle_correct(circle):
    """
    Checks if circle from json has everything correct. If not ends program and writes message.
    :param circle:
    :return:
    """
    check_if_fields_exists(circle, [v.X, v.Y, v.RADIUS])
    if check_if_int(circle.get(v.X), "Incorrect field x of figure circle.") and \
            check_if_int(circle.get(v.Y), "Incorrect field y of figure circle.") and \
            check_if_int(circle.get(v.RADIUS), "Incorrect field radius of figure circle."):
        return True


def check_if_figure_correct(figure):
    """
    Checks if given figure from json has everything correct. If not ends program and writes message.
    :param figure:
    :return:
    """
    figure_type = figure.get(v.TYPE)
    if figure_type == v.POINT:
        check_if_point_correct(figure)
    elif figure_type == v.POLYGON:
        check_if_polygon_correct(figure)
    elif figure_type == v.RECTANGLE:
        check_if_rectangle_correct(figure)
    elif figure_type == v.SQUARE:
        check_if_square_correct(figure)
    elif figure_type == v.CIRCLE:
        check_if_circle_correct(figure)
    else:
        v.handle_error("{} figure name is incorrect.".format(figure_type))


def check_if_figures_correct(figures):
    """
    Checks every figure from given figures list if it is correct.
    :param figures:
    :return:
    """
    for figure in figures:
        check_if_figure_correct(figure)
