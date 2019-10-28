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


def _get_dependencies_helper(step, proximal_dependencies, full_dependencies):
    newly_computed_dependencies = {step: set(proximal_dependencies[step])}


    for dependency in proximal_dependencies[step]:

        if dependency in full_dependencies:
            newly_computed_dependencies[step].update(full_dependencies[dependency])
            continue
        elif dependency in newly_computed_dependencies:
            newly_computed_dependencies[step].update(newly_computed_dependencies[dependency])
            continue
        update_dependencies = _get_dependencies_helper(dependency, proximal_dependencies, full_dependencies)

        for update_step in update_dependencies:
            newly_computed_dependencies.setdefault(update_step, set()).update(update_dependencies[update_step])
        newly_computed_dependencies[step].update(newly_computed_dependencies[dependency])

    return newly_computed_dependencies


def _get_full_dependencies(input_data):
    proximal_dependencies = _get_proximal_dependencies(input_data)
    full_dependencies = {}
    for step, step_dependencies in proximal_dependencies.items():
        if step in full_dependencies:
            continue
        dependency_update = _get_dependencies_helper(step, proximal_dependencies, full_dependencies)
        assert not set(dependency_update) & set(full_dependencies)
        full_dependencies.update(dependency_update)

    return full_dependencies


def part_01(input_data):

    # Don't actually know the desired result, but I'm flying and I have my
    # data already, so going to start working on it.

    for k, v in _get_full_dependencies(input_data).items():
        print(k)
        print('\t' + ', '.join(v))
        print()

    return None
