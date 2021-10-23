# coding: utf-8
# Copyright (c) 2008-2011 Volvox Development Team
# License: /COPYING.txt
# Author: Konstantin Lepa <konstantin.lepa@gmail.com>

"""ANSII Color formatting for output in terminal."""

import os

import termcolor
from termcolor import cprint, COLOR_BLACK, COLOR_RED, ON_BLACK, ON_RED

print('Current terminal type: %s' % os.getenv('TERM'))
print('Test colors:')
cprint('Black color', COLOR_BLACK)
cprint('Red color', COLOR_RED)
cprint('Green color', termcolor.COLOR_GREEN)
cprint('Yellow color', termcolor.COLOR_CYAN)
cprint('Blue color', 'blue')
cprint('Magenta color', 'magenta')
cprint('Cyan color', 'cyan')
cprint('White color', 'white')
cprint('Light grey color', 'light_grey')
cprint('Dark grey color', 'dark_grey')
cprint('Light red color', 'light_red')
cprint('Light green color', 'light_green')
cprint('Light yellow color', 'light_yellow')
cprint('Light blue color', 'light_blue')
cprint('Light magenta color', 'light_magenta')
cprint('Light cyan color', 'light_cyan')
print(('-' * 78))

print('Test highlights:')
cprint('On black color', on_color=ON_BLACK)
cprint('On red color', on_color=ON_RED)
cprint('On green color', on_color=termcolor.ON_GREEN)
cprint('On yellow color', on_color=termcolor.ON_YELLOW)
cprint('On blue color', on_color='on_blue')
cprint('On magenta color', on_color='on_magenta')
cprint('On cyan color', on_color='on_cyan')
cprint('On white color', color='grey', on_color='on_white')
print('-' * 78)

print('Test attributes:')
cprint('Bold black color', 'black', attrs=termcolor.ATTR_BOLD)
cprint('Dark red color', 'red', attrs=[termcolor.ATTR_DARK])
cprint('Underline green color', 'green', attrs=[termcolor.ATTR_UNDERLINE])
cprint('Blink yellow color', 'yellow', attrs=['blink'])
cprint('Reversed blue color', 'blue', attrs=['reverse'])
cprint('Concealed Magenta color', 'magenta', attrs=['concealed'])
cprint('Bold underline reverse cyan color', 'cyan', attrs=['bold', 'underline', 'reverse'])
cprint('Dark blink concealed white color', 'white', attrs=['dark', 'blink', 'concealed'])
print(('-' * 78))

print('Test mixing:')
cprint('Underline red on black color', 'red', 'on_black', ['underline'])
cprint('Reversed green on red color', 'green', 'on_red', ['reverse'])
print(('-' * 78))

print('Test 256 colors:')
for i in range(1,256):
    lb = '' if i % 16 != 0 else '\n'
    cprint(format(i, '3'), on_color=i, end=lb)
print()
