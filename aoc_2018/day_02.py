"""
day_02.py

code for finding solution of day 2 of the advent of code.

Author: Tyler Jachetta <me@tylerjachetta.net>
"""

from aoc_2018 import util

def part_01(input_data):
    input_vals = util.split_input(input_data)

    doubles = 0
    triples = 0

    for line in input_vals:
        counts = [line.count(char) for char in line]
        if 2 in counts:
            doubles += 1
        if 3 in counts:
            triples += 1
    return doubles * triples

def part_02(input_data):
    box_ids = util.split_input(input_data)

    while box_ids:
        current_box_id = box_ids.pop()

        for other_box_id in box_ids:
            matches = [a == b for a, b in zip(current_box_id, other_box_id)]
            if matches.count(False) == 1:

                return ''.join([current_box_id[i] for i in range(len(current_box_id)) if current_box_id[i] == other_box_id[i]])

