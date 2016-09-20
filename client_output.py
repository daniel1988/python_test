#!/usr/bin/python
# -*- coding:utf8 -*-

def cli_confirm(text):
    input_str = raw_input((text + "[y/n]"))
    if ( input_str not in ['y', 'n'] ):
        return confirm(text)
    if input_str == 'y':
        return True
    else:
        return False
# print cli_confirm('are you sure?')

def cli_select(text, options):
    print "---------------------------------------\n"
    for key in options:
        print key,":",options[key]
    print "---------------------------------------\n"
    print text + "%s" % options.keys()
    str = raw_input()
    if ( str in options ):
        return options[str]
    else:
        return cli_select(text, options)
# dict_1 = {
#     'a' : 'A Option',
#     'b' : 'B Option',
#     'c' : 'C Option'
# }
# print cli_select('Please Select',dict_1)


def color_text(text, fg_color=None, bg_color=None):
    fg_colors = {
        'black'        : '0;30',
        'dark_gray'    : '1;30',
        'blue'         : '0;34',
        'light_blue'   : '1;34',
        'green'        : '0;32',
        'light_green'  : '1;32',
        'cyan'         : '0;36',
        'light_cyan'   : '1;36',
        'red'          : '0;31',
        'light_red'    : '1;31',
        'purple'       : '0;35',
        'light_purple' : '1;35',
        'brown'        : '0;33',
        'yellow'       : '1;33',
        'light_gray'   : '0;37',
        'white'        : '1;37'
    }
    bg_colors = {
        'black'      : '40',
        'red'        : '41',
        'green'      : '42',
        'yellow'     : '43',
        'blue'       : '44',
        'magenta'    : '45',
        'cyan'       : '46',
        'light_gray' : '47'
    }
    defines = {
        'error'   : ['white', 'red'],
        'success' : ['white', 'green'],
        'warning' : ['white', 'yellow'],
        'info'    : ['white', 'blue'],
        'notice'  : ['green', ''],
        'danger'  : ['red', ''],
        'import'  : ['light_cyan', ''],
        'quote'   : ['purple', ''],
    }
    if (fg_color in defines):
        bg_color    = defines[fg_color][1]
        fg_color    = defines[fg_color][0]

    text_str = ''
    if (fg_color in fg_colors):
        text_str += "\033[" + fg_colors[fg_color] + "m"

    if (bg_color in bg_colors):
        text_str += "\033[" + bg_colors[bg_color] + "m"

    text_str += text + "\033[0m"
    return text_str

# print color_text('this is a color test', 'error', 'green')

def cli_output(text, color=None, bg_color=None):
    print color_text(text, color, bg_color)

#client error output
def cli_error(text):
    cli_output(text, 'error')
    exit()

def cli_waring(text):
    cli_output(text, 'warning')

def cli_success(text):
    cli_output(text, 'success')

cli_success('This is a success message')
cli_waring('this is a warning message')
cli_error('this is a client error message')
