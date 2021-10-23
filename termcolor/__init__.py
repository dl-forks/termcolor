from termcolor.fn import cprint, colored
from termcolor.enum import *

VERSION = (1, 3, 2)
__version__ = '.'.join([str(v) for v in VERSION])

__all__ = (
    'colored',
    'cprint',

    'COLOR_BLACK', 'COLOR_GREY', 'COLOR_RED', 'COLOR_GREEN',
    'COLOR_YELLOW', 'COLOR_BLUE', 'COLOR_MAGENTA', 'COLOR_CYAN', 'COLOR_LIGHT_GREY',
    'COLOR_DARK_GREY', 'COLOR_LIGHT_RED', 'COLOR_LIGHT_GREEN', 'COLOR_LIGHT_YELLOW',
    'COLOR_LIGHT_BLUE', 'COLOR_LIGHT_MAGENTA', 'COLOR_LIGHT_CYAN', 'COLOR_WHITE',

    'ON_BLACK', 'ON_GREY', 'ON_RED', 'ON_GREEN',
    'ON_YELLOW', 'ON_BLUE', 'ON_MAGENTA', 'ON_CYAN',
    'ON_LIGHT_GREY', 'ON_DARK_GREY', 'ON_LIGHT_RED',
    'ON_LIGHT_GREEN', 'ON_LIGHT_YELLOW', 'ON_LIGHT_BLUE',
    'ON_LIGHT_MAGENTA', 'ON_LIGHT_CYAN', 'ON_WHITE',

    'ATTR_BOLD', 'ATTR_DARK', 'ATTR_UNDERLINE',
    'ATTR_BLINK', 'ATTR_REVERSE', 'ATTR_CONCEALED',

    'VERSION',
    '__version__'
)
