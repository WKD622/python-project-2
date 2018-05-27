import re

DEC_COLOUR_REGEX = '\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)\s*'
HEX_COLOUR_REGEX = '#[a-z\d]{6}'


def dec_to_hex(colour_dec):
    """
    Converts decimal colour to hexadecimal colour format.
    :param colour_dec:
    :return:
    """
    colour_dec = colour_dec.replace(" ", "")
    if re.match(DEC_COLOUR_REGEX, colour_dec):
        pattern = re.compile(DEC_COLOUR_REGEX)
        regular = pattern.match(colour_dec)
        r = int(regular.group(1))
        g = int(regular.group(2))
        b = int(regular.group(3))
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
    else:
        print("Decimal colour incorrect.")


def is_hex(colour):
    """
    Checks if given colour is in hexadecimal format.
    :param colour:
    :return:
    """
    return bool(re.match(HEX_COLOUR_REGEX, colour)) and len(colour) == 7


def is_dec(colour):
    """
    Checks if given colour is in decimal format.
    :param colour:
    :return:
    """
    return bool(re.match(DEC_COLOUR_REGEX, colour))
