"""
CLI-friendly functions for interacting with code through commandline.
"""

import argparse
import importlib
import sys

from aoc_2018 import util

PACKAGE_NAME = __name__.split('.')[0]
ALL_DAYS = 'all'

def hello_world():
    """
    Is this really necessary?
    """

    print('it dun werqued.')


def run_day(day=None, parts=None):

    if day is None:
        parser = argparse.ArgumentParser()
        parser.add_argument('day')
        parser.add_argument('--part', type=int, default=None)

        args = parser.parse_args()
        day = args.day
        if args.part is None:
            parts = [1, 2]
        else:
            parts = [args.part]

    scripts = []

    if day == ALL_DAYS:
        for day in range(1, 26):
            run_day(day, parts=parts)

        return

    day_string = "day_{0:0>2}".format(day)

    try:
        day_module = importlib.import_module("{}.{}".format(PACKAGE_NAME, day_string))
    except ImportError:
        sys.stderr.write('There is no module for day {}}\n'.format(day))
        # TODO raise a gods-damned exception, trap it in the loop above
        return False

    input_data = util.get_input(day)

    for part in parts:
        try:
            part_function_name = "part_{0:0>2}".format(part)
            run_function = getattr(day_module, part_function_name.format(part))
            res = run_function(input_data)

        except AttributeError:
            print("No solution for {0}: {1}".format(day_string, part_function_name))
        else:
            print("{0}: {1}{2:.>25}".format(day_string, part_function_name, res))








