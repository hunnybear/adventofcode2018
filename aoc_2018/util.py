"""
aoc_2018.util

utilities because I'm [hopefully the right kind of] lazy
"""

import os.path
import pkgutil

def split_input(input_val, cast_type=None):
    ws_split = input_val.split()
    comma_split = [ item for item in sum([val.split(',') for val in ws_split], []) if item]
    if cast_type is not None:
        cast = [cast_type(item) for item in comma_split]
        return cast
    else:
        return comma_split


def get_input(day):

    input_filename = "day_{0:0>2}.input".format(day)
    input_data = pkgutil.get_data('aoc_2018', os.path.join('input', input_filename))
    data_str = input_data.decode('utf-8')
    return data_str
