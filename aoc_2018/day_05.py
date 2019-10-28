import re

def react_polymer_tail(polymer):
    """
    Figured I'd try a tail recurison solution, too, as I was trapped on a
    plane :p
    -tjachetta
    """

    for this_idx in range(len(polymer) - 1):
        units = polymer[this_idx: this_idx + 2]
        if (units[0].isupper() != units[1].isupper()) and (units[0].lower() == units[1].lower()):
            return react_polymer(polymer[:this_idx] + polymer[this_idx + 2:])
    return polymer


def react_polymer(polymer):

    idx = 0
    while idx < len(polymer) - 1:
        units = polymer[idx: idx + 2]
        assert(len(units) == 2)
        if (units[0].isupper() != units[1].isupper()) and (units[0].lower() == units[1].lower()):
            polymer = polymer[:idx] + polymer[idx + 2:]
            idx = max(0, idx - 1)
        else:
            idx += 1

    return polymer


def part_01(input_data):
    res = react_polymer(input_data.strip())

    return len(res)


def part_02(input_data):

    # the force, it is brute
    polymer = input_data.strip()

    min_polymer_len = float('inf')

    # I /think/ it might be quicker to just make a set of the input data, then
    # lower that, but I don't care enough to check
    for unit_type in set(unit.lower() for unit in set(polymer)):
        resected_polymer = re.sub('[{}{}]'.format(unit_type, unit_type.upper()), '', polymer)

        reacted_len = len(react_polymer(resected_polymer))
        if reacted_len < min_polymer_len:
            min_polymer_len = reacted_len

    return min_polymer_len
