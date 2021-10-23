from __future__ import print_function
import os
import re
import sys

from termcolor.enum import *

ATTRIBUTES = {
    ATTR_BOLD: 1,
    ATTR_DARK: 2,
    ATTR_UNDERLINE: 4,
    ATTR_BLINK: 5,
    ATTR_REVERSE: 7,
    ATTR_CONCEALED: 8,
}

ATTRIBUTES_RE = '\033\[(?:%s)m' % '|'.join(['%d' % v for v in ATTRIBUTES.values()])

HIGHLIGHTS = {
    ON_BLACK: 40,
    ON_GREY: 40,  # is actually black
    ON_RED: 41,
    ON_GREEN: 42,
    ON_YELLOW: 43,
    ON_BLUE: 44,
    ON_MAGENTA: 45,
    ON_CYAN: 46,
    ON_LIGHT_GREY: 47,
    ON_DARK_GREY: 100,
    ON_LIGHT_RED: 101,
    ON_LIGHT_GREEN: 102,
    ON_LIGHT_YELLOW: 103,
    ON_LIGHT_BLUE: 104,
    ON_LIGHT_MAGENTA: 105,
    ON_LIGHT_CYAN: 106,
    ON_WHITE: 107,
}

HIGHLIGHTS_RE = '\033\[(?:%s)m' % '|'.join(['%d' % v for v in HIGHLIGHTS.values()])

COLORS = {
    COLOR_BLACK: 30,
    COLOR_GREY: 30,  # is actually black
    COLOR_RED: 31,
    COLOR_GREEN: 32,
    COLOR_YELLOW: 33,
    COLOR_BLUE: 34,
    COLOR_MAGENTA: 35,
    COLOR_CYAN: 36,
    COLOR_LIGHT_GREY: 37,
    COLOR_DARK_GREY: 90,
    COLOR_LIGHT_RED: 91,
    COLOR_LIGHT_GREEN: 92,
    COLOR_LIGHT_YELLOW: 93,
    COLOR_LIGHT_BLUE: 94,
    COLOR_LIGHT_MAGENTA: 95,
    COLOR_LIGHT_CYAN: 96,
    COLOR_WHITE: 97,
}

COLORS_RE = '\033\[(?:%s)m' % '|'.join(['%d' % v for v in COLORS.values()])

RESET = '\033[0m'
RESET_RE = '\033\[0m'


def colored(text, color=None, on_color=None, attrs=None):
    """Colorize text, while stripping nested ANSI color sequences.
    Valid values for parameters are listed in termcolor.enum.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white, black, light_grey,
        dark_grey, light_red, light_green, light_yellow, light_blue,
        light_magenta, light_cyan. Additionally, if 256 colors are supported,
        any integer between 1 and 255 can be provided.

    Available text highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_black,
        on_white, on_light_grey, on_dark_grey, on_light_red, on_light_green,
        on_light_yellow, on_light_blue, on_light_magenta, light_cyan.
        Additionally, if 256 colors are supported, any integer between 1 and
        255 can be provided.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.

    Example:
        colored('Hello, World!', termcolor.COLOR_GREEN)
        colored('Hello, World!', 'red', 'on_black', ['bold', 'blink'])
        colored('Hello, World!', 191, 182)
    """
    if os.getenv('ANSI_COLORS_DISABLED') is None and sys.stdout.isatty():
        fmt16_str = '\033[%sm%s'
        fmt256_str = '\033[%d;5;%dm%s'

        if color is not None:
            text = re.sub(COLORS_RE + '(.*?)' + RESET_RE, r'\1', text)
            if color in COLORS:
                text = fmt16_str % (COLORS[color], text)
            elif isinstance(color, int):
                text = fmt256_str % (38, color, text)
        if on_color is not None:
            text = re.sub(HIGHLIGHTS_RE + '(.*?)' + RESET_RE, r'\1', text)
            if on_color in HIGHLIGHTS:
                text = fmt16_str % (HIGHLIGHTS[on_color], text)
            elif isinstance(on_color, int):
                text = fmt256_str % (48, on_color, text)
        if attrs is not None:
            text = re.sub(ATTRIBUTES_RE + '(.*?)' + RESET_RE, r'\1', text)
            for attr in [attrs] if isinstance(attrs, str) or isinstance(attrs, int) else attrs:
                if attr in ATTRIBUTES:
                    text = fmt16_str % (ATTRIBUTES[attr], text)
        return text + RESET
    else:
        return text


def cprint(text, color=None, on_color=None, attrs=None, **kwargs):
    """Print colorize text.

    It accepts arguments of print function.
    """

    print((colored(text, color, on_color, attrs)), **kwargs)
