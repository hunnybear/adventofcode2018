"""
day_01.py

code for finding solution of day 1 of the advent of code.

Author: Tyler Jachetta <me@tylerjachetta.net>
"""

from aoc_2018 import util


def part_01(input_data):
    print('starting part_01 data: {}'.format(input_data))
    input_split = util.split_input(input_data, int)
    return abs(sum(input_split))


def part_02(input_data):
    print('starting {}'.format(input_data))
    freq = [0]
    input_seq = util.split_input(input_data, int)

    counter = 0
    while True:
        change = input_seq[counter % len(input_seq)]
        new_val = freq[-1] + change
        if new_val in freq:
            print('found {}'.format(new_val))
            return new_val
        freq.append(new_val)
