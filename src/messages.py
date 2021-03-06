# -*- coding: UTF-8 -*-

import conf
from sys import exit
from logging import info, debug, error, critical

def closing():
    info(
        '{.app_name}: Closing ...'.format(conf)
    )

def stopped():
    info(
        '{.app_name}: Stopped!'.format(conf)
    )

def starting():
    info(
        '{c.app_name}: '
        'Starting on port {c.port} ...'.format(c=conf)
    )

def welcome():
    print(
        'Welcome to {c.app_name}! Open {c.proxy_url} in '
        'your browser.'.format(c=conf)
    )

def code_related_message(code_path, message, print_f=print):
    print_f(
        '{}: {}'.format(code_path, message)
    )

def code_info(code_path, message):
    code_related_message(code_path, message, print_f=info)

def code_debug(code_path, message):
    code_related_message(code_path, message, print_f=debug)

def code_error(code_path, message):
    code_related_message(code_path, message, print_f=error)

def code_critical(code_path, message):
    code_related_message(code_path, message,
                         print_f=critical)
    closing()
    exit()

def file_not_found(code_path, file_name, print_f=error):
    code_related_message(code_path,
        'file "{}" could not be found!'.format(file_name),
        print_f)

def exhausted_tries(code_path):
    code_critical(code_path,
        'We exhausted all tries in an algorithm and '
        'didn\'t have luck. Try incrementing the maximum'
        'number of tries.')

def impossible_condition(code_path):
    code_critical(code_path,
                  'An impossible condition was met!')

def obj_creation_error(code_path, cls, *args, **kwargs):
    code_error(
        code_path,
        'Unable to create object from class {!r}, '
        'args={!r} and kwargs={!r}'.format(cls, args,
                                           kwargs)
    )
