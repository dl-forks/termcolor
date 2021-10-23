from termcolor.fn import cprint, colored

VERSION = (1, 3, 1)
__version__ = '.'.join([str(v) for v in VERSION])

__all__ = (
    'colored',
    'cprint',

    'VERSION',
    '__version__'
)
