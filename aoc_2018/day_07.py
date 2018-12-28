"""
day_07.py

solution for day 7 of AoC
"""

import re

_INPUT_RESTR = 'Step (?P<dep>[A-Z]) must be finished before step (?P<target>[A-Z]) can begin.'
_INPUT_RE = re.compile(_INPUT_RESTR)

def _get_proximal_dependencies(input_data):
    dependencies = {}
    for line in input_data.splitlines():
        match = _INPUT_RE.fullmatch(line)
        assert match

        dependencies.setdefault(match.group('target'), set()).add(match.group('dep'))
        # No dependencies is valid
        dependencies.setdefault(match.group('dep'), set())
    return dependencies




def _get_full_dependencies(input_data):
    prox_deps = _get_proximal_dependencies(input_data)
    for step in prox_deps:
    return prox_deps


def part_01(input_data):

    # Don't actually know the desired result, but I'm flying and I have my
    # data already, so going to start working on it.

    for k, v in _get_full_dependencies(input_data).items():
        print(k)
        print('\t' + ', '.join(v))
        print()

    return None
